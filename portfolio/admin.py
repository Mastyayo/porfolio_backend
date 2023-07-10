from django.contrib import admin
from .models import (UserDetailModel, UsersociallinkModel, AboutcontentModel, ExperienceModel, ExperienceinputModel, ToolModel, ProjectModel, BlogModel)


admin.site.register(
	(UserDetailModel, UsersociallinkModel, AboutcontentModel, ExperienceModel, ExperienceinputModel, ToolModel, ProjectModel, BlogModel)
)
