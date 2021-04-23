from django.urls import path
from engine.views import (
    GenerateTokensView,
    RefreshTokenView,
    ValidateTokenView
)
urlpatterns = [
    path('token/', GenerateTokensView.as_view()),
    path('token/refresh/', RefreshTokenView.as_view()),
    path('token/validate/', ValidateTokenView.as_view()),
]
