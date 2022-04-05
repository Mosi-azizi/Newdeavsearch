from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from users.models import Profile
# Create your models here.



class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    feautured_image = models.ImageField(default='default.jpg', blank=True,null=True)
    # feautured_image = CloudinaryField('image')
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True , editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Value'),('down','Down Value')
    )
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, null=True,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = ['owner','project']

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name