from rest_framework import routers

from discount.viewsets import DiscountViewSet

router = routers.SimpleRouter()

router.register(r'discount', DiscountViewSet, basename='discount')

urlpatterns = router.urls
