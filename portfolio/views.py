from rest_framework.viewsets import ModelViewSet
from my_portfolio.utils import Helper
from .models import (UserDetailModel, UsersociallinkModel, AboutcontentModel, ExperienceModel, ExperienceinputModel, ToolModel, ProjectModel, BlogModel)
from .serializers import (UserDetailSerializer, UsersociallinkSerializer, AboutcontentSerializer, ExperienceSerializer, ExperienceinputSerializer, ToolSerializer, ProjectSerializer, BlogSerializer)


class UserDetailView(ModelViewSet):
	queryset = UserDetailModel.objects.all()
	serializer_class = UserDetailSerializer


class UsersociallinkView(ModelViewSet):
	queryset = UsersociallinkModel.objects.all()
	serializer_class = UsersociallinkSerializer


class AboutcontentView(ModelViewSet):
	queryset = AboutcontentModel.objects.all()
	serializer_class = AboutcontentSerializer


class ExperienceView(ModelViewSet):
	queryset = ExperienceModel.objects.all()
	serializer_class = ExperienceSerializer


class ExperienceinputView(ModelViewSet):
	queryset = ExperienceinputModel.objects.all()
	serializer_class = ExperienceinputSerializer


class ToolView(ModelViewSet):
	queryset = ToolModel.objects.all()
	serializer_class = ToolSerializer


class ProjectView(ModelViewSet):
	queryset = ProjectModel.objects.all()
	serializer_class = ProjectSerializer


class BlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
