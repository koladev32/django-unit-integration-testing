from rest_framework import routers

from discount.viewsets import DiscountViewSet
from cart.viewsets import CartViewSet

router = routers.SimpleRouter()

router.register(r'discount', DiscountViewSet, basename='discount')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = router.urls
