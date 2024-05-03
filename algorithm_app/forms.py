from socket import fromshare
from django import forms

class Data(forms.Form):
    Enter_Character=forms.CharField(max_length=100)

class Search_Data(forms.Form):
    Enter_number_or_string=forms.CharField(max_length=100)
    Enter_number_or_string_to_search=forms.CharField(max_length=100)

class BFSForm(forms.Form):
    start_nodes = forms.CharField(label='Enter start nodes (comma-separated)')
    end_nodes = forms.CharField(label='Enter end nodes (comma-separated)')

       