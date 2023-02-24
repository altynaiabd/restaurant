from django import forms
from .models import Order, MenuItem

class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    customer_email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    customer_phone = forms.CharField(
        label='Your Phone',
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    delivery_address = forms.CharField(
        label='Delivery Address',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    delivery_date = forms.DateField(
        label='Delivery Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    delivery_time = forms.TimeField(
        label='Delivery Time',
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    items = forms.ModelMultipleChoiceField(
        label='Select Menu Items',
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    total_price = forms.DecimalField(
        label='Total Price',
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'delivery_address', 'delivery_date', 'delivery_time', 'items', 'total_price']

    # Override the default form template to include the Bootstrap styles
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
