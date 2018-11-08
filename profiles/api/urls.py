from django.urls import path

from .views import (
	ProfileCreateView,
	add_course,
	remove_course,
	get_my_courses,
)

urlpatterns = [
	path('create/', ProfileCreateView.as_view()),
	path('u/', get_my_courses),
	path('add/<int:id>/', add_course),
	path('remove/<int:id>/', remove_course),
]
