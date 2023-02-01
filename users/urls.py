from .views import SignupView, ProfileView, UpdateProfileView, AddRemoveSavedView, SavedView, RecentlyViewedView
from django.urls import path

app_name='users'
urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('update', UpdateProfileView.as_view(), name='update'),
    path('addremovesaved/<int:product_id>', AddRemoveSavedView.as_view(), name='addremovesaved'),
    path('saveds', SavedView.as_view(), name='saveds'),
    path('recently-viewed', RecentlyViewedView.as_view(), name='recently_viewed')
]