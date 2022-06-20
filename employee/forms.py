from django import forms
from .models import WorkUpdate, FertilizerStockDetail,TestingReports


class employeLogineForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    loginId = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))


class WorkUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkUpdate
        fields = ['date',
                  'department',
                  'work',
                  'description']



class FertilizerStockDetailForm(forms.ModelForm):
    class Meta:
        model = FertilizerStockDetail
        fields = '__all__'


class TestingReportsForm(forms.ModelForm):
    class Meta:
        model = TestingReports
        fields = '__all__'