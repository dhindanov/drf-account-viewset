from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import RootView
from api.api import BankAccountViewSet
from api.external import ExternalBankAccountView


# Create a router and register the BankAccountViewSet
router = DefaultRouter()
router.register(r'accounts', BankAccountViewSet)

urlpatterns = [
    *router.urls,
    path('external-accounts/<str:account_number>/', ExternalBankAccountView.as_view(), name='external-account-detail'),
    path('', RootView.as_view(), name='api-root'),
]
