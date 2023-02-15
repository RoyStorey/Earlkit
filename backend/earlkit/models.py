from django.db import models
import uuid
import jsonfield
import PIL

class Earlkit(models.Model):
    uid=models.UUIDField(null=False,default=uuid.uuid4,unique=True,editable=False)
    title=models.CharField(max_length=50)
    url=models.CharField(max_length=100)
    desc=models.TextField(default="",help_text='Please enter a description for the site\nMax 500 characters',max_length=500)
    img=models.ImageField(upload_to='public/images/',max_length=256)
    tags=models.CharField(default="",help_text='Please seperate all tags with a colon (ex tag1 : tag2)\nMax 30 characters',max_length=30)
    
    def __self__(self):
        return self.title