from django.shortcuts import render, redirect
from .models import Category, MenuItem, Order
from .forms import OrderForm

# Create your views here.

def menu(request):
    menu_item = MenuItem.objects.all()
    category = Category.objects.all()
    context = {
        'product':menu_item,
        'categories':category
    }
    return render(request, template_name='aksaray_restaurant/menu.html', context=context)

def order(request):
    menu_items = MenuItem.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            items = request.POST.getlist('items')
            for item_id in items:
                item = MenuItem.objects.get(pk=item_id)
                order_item = Order.objects.create(order=order, item=item, price=item.price)
            return redirect('aksaray_restaurant:order_confirmation', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'aksaray_restaurant/order.html', {'form': form, 'menu_items': menu_items})

def order_confirmation(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'aksaray_restaurant/order.html', {'order': order})