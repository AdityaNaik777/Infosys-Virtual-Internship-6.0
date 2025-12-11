# accounts/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=False)
    avatar_path = forms.ImageField(required=False)
    preferred_categories = forms.CharField(required=False)
    preferred_difficulty = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "full_name", "avatar_path",
                  "preferred_categories", "preferred_difficulty")


class UserUpdateForm(UserChangeForm):
    password = None  # hide password field in profile edit form

    class Meta:
        model = User
        fields = ("full_name", "email", "avatar_path",
                  "preferred_categories", "preferred_difficulty")
