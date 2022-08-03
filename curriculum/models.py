from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os

#functions to save images in media directory
def save_subject_image(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]
    # get filename
    if instance.subject_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id,ext)
    return os.path.join(upload_to,filename)

def save_lesson_files(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]
    # get filename
    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id,ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id,new_name,ext)
    return os.path.join(upload_to,filename)



#creating the standard model
class Standard(models.Model):
    standard_id = models.CharField(unique=True,max_length=100,null=True)
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=500,blank = True)

    def save(self,*args,**kwargs): 
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

#creating the Subject model
class Subject(models.Model):
    subject_id = models.CharField(unique=True,max_length=100)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE,related_name='subjects')
    image = models.ImageField(upload_to = save_subject_image, verbose_name='Subject Image')
    description = models.TextField(max_length=500,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

#creating the Lesson model
class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100,unique=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lessons' )
    name = models.CharField(max_length=500)
    position = models.PositiveSmallIntegerField(verbose_name='chapter no')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name='video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lesson_files,verbose_name='Presentations',blank=True,null=True)
    Notes = models.FileField(upload_to=save_lesson_files,verbose_name='Notes',blank=True,null=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position']
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
