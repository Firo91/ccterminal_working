from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Equipment, CustomUser

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('bax_nr', 'name', 'tid', 'terminal_type', 'city', 'serial_number')       

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','name', 'country', 'city', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.country = self.cleaned_data['country']
        if commit:
            user.save()
        return user
    
class CustomPasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
