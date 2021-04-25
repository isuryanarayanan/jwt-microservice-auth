from django.urls import path
from engine.views import (
    GenerateTokensView,
    ValidateTokenView,
    RefreshTokenView
)
urlpatterns = [
    path('login/', GenerateTokensView.as_view()),
    path('refresh/', RefreshTokenView.as_view()),
    path('validate/', ValidateTokenView.as_view()),
]
