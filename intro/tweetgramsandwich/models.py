from django.db import models

class Search(models.Model):
	ip_address = models.IPAddressField()
	query = models.CharField(max_length=200)
	query_time = models.DateTimeField(False, True)
	twitter_url = models.URLField()
	instagram_url = models.URLField()
