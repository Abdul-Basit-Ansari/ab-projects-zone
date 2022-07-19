from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
	"""Model definition for Project."""
	sno = models.AutoField(primary_key=True)
	cover = models.ImageField(upload_to="img/projectcover")
	title = models.CharField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	link = models.TextField()
	desc = models.TextField()
	keyword = models.CharField(max_length=40)
	date = models.DateTimeField(auto_now_add=True)



	class Meta:
		"""Meta definition for Project."""

		verbose_name = 'Project'
		verbose_name_plural = 'Projects'

	def __str__(self):
		"""Unicode representation of Project."""
		return self.title


class Contactus(models.Model):
	"""Model definition for Contactus."""
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50 , blank=True , null=True)
	number = models.CharField(max_length=20)
	msg = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		"""Meta definition for Contactus."""

		verbose_name = 'Contactus'
		verbose_name_plural = 'Messages'

	def __str__(self):
		"""Unicode representation of Contactus."""
		return self.name + "  " + str(self.date)

class Feedback(models.Model):
	"""Model definition for Contactus."""
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	msg = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		"""Meta definition for Contactus."""

		verbose_name = 'Feedback'
		verbose_name_plural = 'Feedbacks'

	def __str__(self):
		"""Unicode representation of Contactus."""
		return self.name + "  " + str(self.date)






class Skill(models.Model):
	"""Model definition for Project."""
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	range = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)



	class Meta:
		"""Meta definition for Project."""

		verbose_name = 'Skill'
		verbose_name_plural = 'Skills'

	def __str__(self):
		"""Unicode representation of Project."""
		return self.title
