from django.contrib import admin
from django.urls import path

from payments.views import item_detail, buy_detail, success, cancel, index, order_detail, buy_order_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>', item_detail),
    path('buy/<int:id>', buy_detail),
    path('success', success),
    path('cancel', cancel),
    path('', index),
    path('order/<int:id>', order_detail),
    path('buy_order/<int:id>', buy_order_detail)
]
