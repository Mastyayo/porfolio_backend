from rest_framework import serializers
from .models import (UserDetailModel, UsersociallinkModel, AboutcontentModel,
                     ExperienceModel, ExperienceinputModel, ToolModel, ProjectModel, BlogModel)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailModel
        fields = '__all__'


class UsersociallinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersociallinkModel
        fields = '__all__'


class AboutcontentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutcontentModel
        fields = '__all__'


class ExperienceinputSerializer(serializers.ModelSerializer):
    experience = serializers.CharField(read_only=True)
    experience_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ExperienceinputModel
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    experience_inputs = ExperienceinputSerializer(many=True, read_only=True)

    class Meta:
        model = ExperienceModel
        fields = '__all__'


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolModel
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tool = ToolSerializer(many=True, read_only=False)

    class Meta:
        model = ProjectModel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
