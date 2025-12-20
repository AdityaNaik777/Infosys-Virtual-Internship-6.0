# quizzes/ai_service.py
import json
import re
import requests
from django.conf import settings


OPENAI_API_KEY = settings.OPENAI_API_KEY
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_URL = "https://api.openai.com/v1/chat/completions"



def clean_json(text: str) -> str:
    """
    Removes markdown code fences and extracts JSON array from text.
    """
    text = text.strip()

    # Remove ```json or ``` fences
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
    if text.endswith("```"):
        text = text[:-3].strip()

    # Extract JSON array using regex
    match = re.search(r"(\[\s*\{.*\}\s*\])", text, flags=re.DOTALL)
    if match:
        return match.group(1)

    return text


def validate_questions(questions, count):
    """
    Ensures JSON array is valid.
    """
    if not isinstance(questions, list):
        raise ValueError("AI did not return a JSON array.")

    if len(questions) != count:
        raise ValueError(f"Expected {count} questions, got {len(questions)}.")

    required = ["question", "option_a", "option_b", "option_c", "option_d", "correct_answer"]

    for q in questions:
        for f in required:
            if f not in q:
                raise ValueError(f"Missing field: {f}")

        if q["correct_answer"] not in ["A", "B", "C", "D"]:
            raise ValueError("correct_answer must be A/B/C/D")

    return questions


def generate_quiz_questions(
    topic,
    category,
    difficulty,
    count=10,
    concepts=None
):
    """
    Generate MCQs using OpenAI
    """

    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY not found in settings.")

    # 🔹 CONCEPT AWARE PROMPT ADDITION
    concept_block = ""
    if concepts:
        concept_block = "\n".join(
            f"{i+1}. {concept}" for i, concept in enumerate(concepts)
        )

    prompt = f"""
You are an expert exam question setter.

Topic: {topic}
Category: {category}
Difficulty: {difficulty}

STRICT RULES:
1. Generate exactly {count} UNIQUE multiple choice questions.
2. Generate EXACTLY ONE question per concept.
3. Use ONLY the concepts listed below.
4. Do NOT repeat or rephrase questions.
5. Each question must test a different idea.
6. Keep difficulty strictly at {difficulty} level.

CONCEPT LIST:
{concept_block}

Each item must follow EXACTLY this JSON structure:

[
  {{
    "question": "text",
    "option_a": "A option",
    "option_b": "B option",
    "option_c": "C option",
    "option_d": "D option",
    "correct_answer": "A",
    "explanation": "why the answer is correct"
  }}
]

Return ONLY the JSON array.
No text outside JSON.
"""

    try:
        response = requests.post(
            OPENAI_URL,
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": OPENAI_MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                # 🔹 IMPORTANT: INCREASE TEMPERATURE FOR VARIETY
                "temperature": 0.85,
            },
            timeout=45
        )

        response.raise_for_status()
        data = response.json()

        # Extract text from model response
        message = data["choices"][0]["message"]["content"]

        # Clean and extract JSON
        cleaned = clean_json(message)

        # Parse JSON array
        questions = json.loads(cleaned)

        # Validate structure
        return validate_questions(questions, count)

    except Exception as e:
        raise Exception(f"Failed to generate quiz questions: {e}")

