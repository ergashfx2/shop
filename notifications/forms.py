from django import forms


class Create_Notification_Form(forms.Form):
    title = forms.CharField(label="Sarlavha kiriting", max_length=300)
    body = forms.CharField(
        label='Matn kiriting',
        widget=forms.Textarea(attrs={'placeholder': 'Matn kiriting', 'rows': 10, 'cols': 50}),
    )
