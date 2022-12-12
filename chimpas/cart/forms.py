from django import forms

#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#SIZE = [
      #  ('XS', 'Xs'),
       # ('S', 'S'),
       # ('M', 'M'),
       # ('L', 'L'),
        #('XL', 'Xl'),
   # ]

class CartAddProductForm(forms.Form):

    #sizes = forms.TypedChoiceField( choices=SIZE )
    quantity = forms.IntegerField(min_value= 1, label='Количество', widget=forms.NumberInput(attrs={'class': 'inpt_class'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
