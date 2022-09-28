from rest_framework.routers import DefaultRouter
from .views import CustomUserViewset


router = DefaultRouter()
router.register(r'auth', CustomUserViewset, basename='auth')
urlpatterns = router.urls

