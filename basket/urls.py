from django.urls import path
from basket.views import AddBasketItem, BasketItemList, DeleteBasketItem, DiscountAPIView



urlpatterns = [
    path('add-to-basket', AddBasketItem.as_view()),
    path('basket-item-list', BasketItemList.as_view()),
    path('basket-item-delete/<str:pk>', DeleteBasketItem.as_view()),
    path('discount/', DiscountAPIView.as_view()),
]