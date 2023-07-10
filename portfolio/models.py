from django.db import models


class UserDetailModel(models.Model):
	welcome_title = models.CharField(max_length=120)
	welcome_note = models.CharField(max_length=255)
	welcome_description = models.TextField()
	cv_link = models.TextField()
	user_image = models.ImageField(upload_to='images')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class UsersociallinkModel(models.Model):
	name = models.CharField(max_length=100)
	link = models.TextField()
	icon = models.ImageField(upload_to='icons')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class AboutcontentModel(models.Model):
	paragraph = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class ExperienceModel(models.Model):
	image = models.ImageField(upload_to='experience')
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	start = models.CharField(max_length=100)
	end = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class ExperienceinputModel(models.Model):
	content = models.TextField()
	experience = models.ForeignKey('ExperienceModel', on_delete=models.CASCADE, related_name='experience_inputs')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class ToolModel(models.Model):
	name = models.CharField(unique=True, max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
 
	def __str__(self):
		return self.name
	



class ProjectModel(models.Model):
	title = models.CharField(max_length=255)
	about = models.TextField()
	tool = models.ManyToManyField('ToolModel', related_name='project_tool')
	cover = models.ImageField(upload_to='cover')
	link = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
 
	class Meta:
		ordering = ('-created_at', )
 

	def __str__(self):
		return self.title
	



class BlogModel(models.Model):
	title = models.CharField(max_length=150)
	cover = models.ImageField(upload_to='cover')
	link = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at', )
 

	def __str__(self):
		return self.title