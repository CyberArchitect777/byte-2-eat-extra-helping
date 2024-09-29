from django.urls import path
from . import views

urlpatterns = [

    # User dashboard page where they can see all their review
    path("takeaway_dashboard/", views.takeaway_dashboard, name="takeaway_dashboard"),

    # So User can add a new review
    path("add_review/", views.add_review, name="add_review"),

    # So User can edit their existing review
    path("edit_review/<int:pk>/", views.edit_review, name="edit_review"),

    # So User can delete their existing review
    path("delete_review/<int:pk>/", views.delete_review, name="delete_review"),
]
