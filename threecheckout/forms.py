from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i,i) for i in range(1,12)]
    YEAR_CHOICES = [(i,i) for i in range(2016, 2036)]

    credit_card_number = forms.CharField(label="Credit card Number", required=False)
    cvv = forms.CharField(label = "Security Code (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Month",choice=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year",choice=YEAR_CHOICES, requried=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm)
    class Meta:
        model = Order
        fields = ('full_name','phone_number','country','postcode','town_or_city','street_address1','street_address2','country')