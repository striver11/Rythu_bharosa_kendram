from django import forms
from .models import FarmerRegistrationModel, PurchaseAgroProduct, FarmerFeedback


class FarmerRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           required=True, max_length=100)

    login_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True, max_length=100)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', 'class': 'form-control',
                                          'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
        required=True, max_length=100)

    mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[56789][0-9]{9}', 'class': 'form-control'}),
                             required=True,
                             max_length=100)

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True, max_length=100)

    locality = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True, max_length=100)

    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 22, 'class': 'form-control'}),
                              required=True, max_length=250)

    city = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only ',
               'class': 'form-control'}), required=True,
        max_length=100)

    state = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only ',
               'class': 'form-control'}), required=True,
        max_length=100)

    class Meta:
        model = FarmerRegistrationModel
        fields = '__all__'


class PurchaseAgroProductForm(forms.ModelForm):
    class Meta:
        model = PurchaseAgroProduct
        fields = ['products', 'phone', "address"]


class FarmerFeedbackForm(forms.ModelForm):
    class Meta:
        model = FarmerFeedback
        fields = ['feedBack']
