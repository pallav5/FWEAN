from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def get_month(self):
        return self.updated_at.strftime('%b')

    def get_date(self):
        return self.updated_at.strftime('%d')

    def get_year(self):
        return self.updated_at.strftime('%y')

    def get_week(self):
        return self.updated_at.strftime('%a')

    def get_time(self):
        return self.updated_at.strftime('%I'":"'%M%p')

    class Meta:
        abstract = True


class Organization(TimeStamp):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='organization')
    address = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=200)
    alt_contact_no = models.CharField(max_length=200, null=True, blank=True)
    map_location = models.CharField(max_length=2000, null=True, blank=True)
    email = models.EmailField()
    alt_email = models.EmailField(null=True, blank=True)
    slogan = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    viber = models.CharField(max_length=200, null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class OrganzationStructure(TimeStamp):
    pass


class Programmes(TimeStamp):
    pass


class Projects(TimeStamp):
    pass


class GeographicalCoverage(TimeStamp):
    pass


class SuccessStories(TimeStamp):
    pass

class Gallery(TimeStamp):
    pass

class NewsAndMedia(TimeStamp):
    pass


class Videos(TimeStamp):
    pass

class Donors(TimeStamp):
    pass

class Subscription(TimeStamp):
    pass

class FAQS(TimeStamp):
    pass

class FooterImportantLinks(TimeStamp):
    pass


class FweanInMedia(TimeStamp):
    pass


class AboutUs(TimeStamp):
    pass


class Slider(TimeStamp):
    image = models.ImageField(upload_to='Sliders')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

