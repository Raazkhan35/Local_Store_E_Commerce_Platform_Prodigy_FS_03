import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    order = Order.objects.get(user=request.user, completed=False)
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=int(order.total_price * 100),
                currency='usd',
                description='Order Payment',
                source=token
            )
            order.completed = True
            order.save()
            return redirect('order_complete')
        except stripe.error.StripeError:
            return render(request, 'checkout.html', {'error': 'Payment failed'})

    return render(request, 'checkout.html', {'order': order})
