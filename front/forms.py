from django import forms

class SettingsForm(forms.Form):
    git_repo = forms.CharField(max_length=100)
    test_path = forms.CharField(max_length=100)
    sel_host = forms.GenericIPAddressField(protocol='IPv4')
    sel_port = forms.IntegerField(max_value= 60000, min_value = 1024)
    browser = forms.CharField(max_length=100)
    sel_os = forms.CharField(max_length=100)