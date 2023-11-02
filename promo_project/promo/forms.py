
from .models import Person, Campaign, House
from django import forms
from .models import CustomUser


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'email', 'phone']


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'houses']


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['city', 'street', 'number', 'entrances', 'apartments_per_entrance']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'birth_date', 'address', 'gender')
        widgets = {
            'password': forms.PasswordInput()
        }