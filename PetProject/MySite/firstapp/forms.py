from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Name user', empty_value='Input your name', max_length=25,
                           help_text='Maximum 25 symbols',
                           widget=forms.TextInput(attrs={'class': 'myfield'}))
    age = forms.IntegerField(label='Age user', min_value=1, max_value=130,
                             help_text='No less 1 symbols and no more 130 symbols',
                             widget=forms.NumberInput(attrs={'class': 'myfield'}))