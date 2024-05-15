from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail, ToyList, ToyDetail, AddToyToCat, RemoveToyFromCat, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
  path('',Home.as_view(), name='home'),
  path('cats/', CatList.as_view(), name='cat-list'),
  path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),
  path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name = 'feeding-list-create'),
  path('cats/<int:cati_id>/feedings/<int:id>/', FeedingDetail.as_view(), name = 'feeding-detail'),
  path('toys/', ToyList.as_view(), name='toy-list'),
  path('toys/<int:id>/', ToyDetail.as_view(), name = 'toy-detail'),
  path('cats/<int:cat_id>/add-toy/<int:toy_id>/', AddToyToCat.as_view(), name='add-toy-to-cat'),
  path('cats/<int:cat_id>/remove-toy/<int:toy_id>/', RemoveToyFromCat.as_view(), name='remove-toy-from-cat'),
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
]

