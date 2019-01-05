from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLogin(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, ** kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This User Does not Exist')
            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")
            if not user.is_active:
                raise forms.ValidationError("User not Active")
        return super(UserLogin, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.EmailField(label='Email Address')
    Password = forms.CharField(widget=forms.PasswordInput,label='Enter Password')

    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
        ]

    def checkemail(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("this email is already being used")
        return email
