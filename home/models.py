from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField( max_length = 180, default = "", null=False, blank=False)
    description = models.TextField(default = "", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=24, null=True, blank=True)
    sale_price = models.DecimalField(decimal_places=2, max_digits=24, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, null=True, on_delete=True)
    image = models.ImageField(upload_to='home/static/img', default="home/static/images/2.jpg")
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        #return '%s' % self.event.title
        #return str(self.event.title)
        return self.event.title