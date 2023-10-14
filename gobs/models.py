from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# انشاء اقسام المهمه 
class Category(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    


#  انشاء  مهارات القائم علي الجوب 
class Experience(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

# نوع العمل علي المهمه 
class GobType(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name    
    

    # FULLTIME  = 'fulltime'
    # PARTTIME  = 'PartTime'
    # REMOTE    = 'Remote'
    # FREELANCE = 'Freelance'


# تحديد وقت عمل الجوب 
class WostedWithin(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name   


    # ANY  = 'any'
    # TODAY  = 'Today'
    # LASTWEEK    = 'Lastweek'
    # LASTMONTH = 'Lastmonth'



#  محتوي الجوب 
class Gobs(models.Model):
    user = models.ForeignKey(User, related_name='gob_user', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, related_name='gob_category', on_delete=models.SET_NULL, null=True, blank=True)
    experience = models.ForeignKey(Experience, related_name='gob_Experience', on_delete=models.SET_NULL, null=True, blank=True)
    gobType = models.ForeignKey(GobType , related_name='gob_type', on_delete=models.SET_NULL, null=True, blank=True)
    wosted_within = models.ForeignKey(WostedWithin, related_name='wosted_within', on_delete=models.SET_NULL, null=True, blank=True )
    price_gob = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name


# عرض تفاصيل الجوب 
class GobDetail(models.Model):
    gob_details = models.ForeignKey(Gobs, related_name='gob_details', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

    