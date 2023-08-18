from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, password_validation
from django import forms
from django.core.exceptions import ValidationError

from profile_app.models import Profile, Company

ROLE_CHOICES = (
    (False, "Работник"),
    (True, "Работодатель"),
)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail',
        label_suffix='',
        widget=forms.EmailInput()
    )

    password1 = forms.CharField(
        label="Пароль",
        strip=True,
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html(),
        label_suffix="",
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(),
        strip=True,
        help_text="Enter the same password as before, for verification.",
        label_suffix="",
    )

    role = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        label="",
        choices=(('0', 'Ищу работу'), ('1', 'Ищу сотрудника')),
        widget=forms.RadioSelect(),
        initial='0'
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'role') 


class SignUpForm1(forms.Form):
    role = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        label="",
        choices=((0, 'Ищу работу'), (1, 'Ищу сотрудника')),
        widget=forms.RadioSelect(),
        initial=1
    )


class SignUpForm2(forms.ModelForm):
    email = forms.EmailField(
        label='E-mail',
        label_suffix='',
        widget=forms.EmailInput()
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)


class SignUpForm3(forms.ModelForm):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label="Пароль",
        strip=True,
        widget=forms.PasswordInput(),
        label_suffix="",
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(),
        strip=True,
        label_suffix="",
    )

    class Meta:
        model = get_user_model()
        fields = ('password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SignUpForm4Profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'birth_date', 'gender')


class SignUpForm4Company(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='E-mail',
        label_suffix='',
        widget=forms.EmailInput(attrs={
            "class": "input is-primary",
            "type": "email",
            "placeholder": "Электронная почта",
        }
        ))

    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "input is-primary",
            "type": "password",
            "placeholder": "Пароль",
        }),
        help_text=password_validation.password_validators_help_text_html(),
        label_suffix="",
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)
