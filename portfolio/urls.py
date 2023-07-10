from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserDetailView, UsersociallinkView, AboutcontentView, ExperienceView, ExperienceinputView, ToolView, ProjectView, BlogView)


router = DefaultRouter()
router.register('user-detail-url', UserDetailView, basename='user-detail-url')
router.register('usersociallink-url', UsersociallinkView, basename='usersociallink-url')
router.register('aboutcontent-url', AboutcontentView, basename='aboutcontent-url')
router.register('experience-url', ExperienceView, basename='experience-url')
router.register('experienceinput-url', ExperienceinputView, basename='experienceinput-url')
router.register('tool-url', ToolView, basename='tool-url')
router.register('project-url', ProjectView, basename='project-url')
router.register('blog-url', BlogView, basename='blog-url')

urlpatterns = [
	path('', include(router.urls)),
]
