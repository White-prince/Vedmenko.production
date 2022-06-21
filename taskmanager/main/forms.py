from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    from_email = forms.EmailField(label='from_email', max_length=100)
    message = forms.CharField(label='message', widget=forms.Textarea, required=True)
    cc_myself = forms.BooleanField(required=False)
