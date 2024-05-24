from django.db import models


class Invitation(models.Model):

	id = models.CharField(primary_key=True, max_length=255)
	email = models.EmailField()
