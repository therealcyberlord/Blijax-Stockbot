from django.db import models

# Create your models here.
from django.db import models

class Text(models.Model):
	text = models.CharField(max_length = 500, blank = False)
	time_sent = models.DateTimeField(auto_now_add = True) 