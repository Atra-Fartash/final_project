from django.urls import path
from accounts.views import ProfileListCreate, ProfileRetrieveUpdateDestroy, TransactionView



urlpatterns = [
    path('profile-list-create', ProfileListCreate.as_view()),
    path('profile-retrieve-update-destroy/<str:pk>', ProfileRetrieveUpdateDestroy.as_view()),
    path('new-transaction', TransactionView.as_view()),
]