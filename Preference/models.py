from django.db import models

class DataEntry(models.Model):
    end_year = models.CharField(max_length=4, blank=True, null=True)
    intensity = models.DecimalField(max_digits=5, decimal_places=2)
    sector = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=50)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    impact = models.CharField(max_length=50, blank=True, null=True)
    added = models.DateTimeField()
    published = models.DateTimeField(null=True)
    country = models.CharField(max_length=50)
    relevance = models.DecimalField(max_digits=5, decimal_places=2)
    pestle = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    likelihood = models.IntegerField()
    
    def __str__(self):
        return self.title
