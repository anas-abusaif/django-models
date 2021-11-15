from django.urls import path
from snacks.views import SnackListView, SnackDetailView

urlpatterns=[
  path("", SnackListView.as_view(), name="snacks_list"),
  path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail")
]