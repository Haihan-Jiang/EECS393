from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()


##This is a demo class
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)
        app_label = 'bookinghub'

    def __str__(self):
        return self.title


##This is a user class
class User(models.Model):
    STATUS_CHOICES = (
        ('0', 'checked out'),
        ('1', 'checked in'),
        ('2', 'has a reservation'),
        ('3', 'no reservation')
    )
    userID = models.FloatField(null=True, blank=True, default=None)
    userPassword = models.FloatField(null=True, blank=True, default=None)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,)
    expectedMinPrice = models.IntegerField(null=True, blank=True, default=None)
    expectedMaxPrice = models.IntegerField(null=True, blank=True, default=None)
    reservation = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='reservation')  ## one to many relationship use forign key
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='3')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('expectedMinPrice',)
        app_label = 'bookinghub'

    def __str__(self):
        return self.name


##This is a reservation class
class reservation(models.Model):
    STATUS_CHOICES = (
        ('0', 'UnProcessed'),
        ('1', 'processing'),
        ('2', 'processed'),
    )
    reservationID = models.FloatField(null=True, blank=True, default=None)
    roomNumber = models.IntegerField(null=True, blank=True, default=None)
    hotelName = models.CharField(max_length=250)
    checkIn = models.DateTimeField(default=None)
    checkOut = models.DateTimeField(default=None)
    reserveTime = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank=True, default=None)
    slug = models.SlugField(max_length=250,)
    room = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room') ## one to many relationship use forign key
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='0')
    objects = models.Manager()  # The default manager.
   # published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('reserveTime',)
        app_label = 'bookinghub'

    def __str__(self):
        return self.hotelName


##This is a room class
class room(models.Model):
    STATUS_CHOICES = (
        ('0', 'Occupied'),
        ('1', 'Available'),
        ('2', 'Unavailable'),
    )
    roomType = models.CharField(max_length=250)
    created = models.DateTimeField(null=True, blank=True, default=None)
    hotel = models.CharField(max_length=250)
    roomID = models.FloatField(null=True, blank=True, default=None)
    price = models.IntegerField(null=True, blank=True, default=None)
    slug = models.SlugField(max_length=250,)
    objects = models.Manager()  # The default manager.
    #published = PublishedManager()  # Our custom manager.
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='2')
    class Meta:
        ordering = ('price',)
        app_label = 'bookinghub'

    def __str__(self):
        return self.roomType


##This is a hotel class
class hotel(models.Model):
    hotelName = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    rating = models.IntegerField(null=True, blank=True, default=None)
    price = models.IntegerField(null=True, blank=True, default=None)
    contactEmail = models.EmailField(null=True, blank=True, default=None)
    contactPhoneNumber = models.FloatField(null=True, blank=True, default=None)
    hotelStaff = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='hotelStaff')  ## one to many relationship use forign key
    slug = models.SlugField(max_length=250,)
    objects = models.Manager()  # The default manager.
    #published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('rating',)
        app_label = 'bookinghub'
    def __str__(self):
        return self.hotelName


##This is a hotel staff class
##This is a hotel class
class hotelStaff(models.Model):
    staffID = models.FloatField(max_length=250)
    name = models.CharField(max_length=250)
    contactEmail = models.EmailField(null=True, blank=True, default=None)
    contactPhoneNumber = models.FloatField(null=True, blank=True, default=None)
    slug = models.SlugField(max_length=250, )
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('staffID',)
        app_label = 'bookinghub'

    def __str__(self):
        return self.name
