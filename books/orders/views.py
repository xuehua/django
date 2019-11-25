from django.views.generic import TemplateView

# Create your views here.
class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
