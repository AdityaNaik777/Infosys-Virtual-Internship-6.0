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
    preferred_difficulty = forms.ChoiceField(
        required=False,
        choices=[('', 'Select difficulty'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High')],
    )

    class Meta:
        model = User
        fields = ("username", "email", "full_name", "avatar_path",
                  "preferred_categories", "preferred_difficulty")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes and placeholders for modern styling
        common_attrs = {
            'class': 'form-input',
        }
        self.fields['username'].widget.attrs.update({**common_attrs, 'placeholder': 'Choose a username'})
        self.fields['email'].widget.attrs.update({**common_attrs, 'placeholder': 'your@email.com'})
        self.fields['full_name'].widget.attrs.update({**common_attrs, 'placeholder': 'Your full name'})
        self.fields['password1'].widget.attrs.update({**common_attrs, 'placeholder': 'Create a password'})
        self.fields['password2'].widget.attrs.update({**common_attrs, 'placeholder': 'Confirm password'})
        self.fields['preferred_categories'].widget.attrs.update({**common_attrs, 'placeholder': 'e.g., Science, Math'})
        self.fields['preferred_difficulty'].widget.attrs.update({'class': 'form-input form-select'})
        self.fields['avatar_path'].widget.attrs.update({'class': 'form-input', 'accept': 'image/*'})


class UserUpdateForm(UserChangeForm):
    password = None  # hide password field in profile edit form

    class Meta:
        model = User
        fields = ("full_name", "email", "avatar_path",
                  "preferred_categories", "preferred_difficulty")
