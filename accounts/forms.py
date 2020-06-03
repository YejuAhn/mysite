from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .backends import UserBackend

class LoginForm(forms.Form):
    username = forms.EmailField(label = "Email")
    full_name = forms.CharField(widget = forms.Textarea)


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label = "Email")
    full_name = forms.CharField(widget= forms.Textarea)

    class Meta:
        model = User
        fields = ('email','full_name',)

    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit=False)
        email = self.cleaned_data["email"]
        full_name = self.cleaned_data["full_name"]
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            print("good email")
            # user = UserBackend.authenticate(email=user.email, full_name= full_name)
            user.email = email
            user.full_name = full_name
            user.active = True  # change to false if using email activation
            if commit:
                user.save()
                # login(self.request, user)
            return user


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
