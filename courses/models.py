from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):

    COURSE_TYPE_CHOICES=[
        ('1', 'online'),
        ('2', 'offline'),
    ]

    PURCHASE_TYPE_CHOICES=[
        ('s', 'single'),
        ('g', 'group'),
    ]

    title = models.CharField(max_length=100)
    course_type = models.CharField(max_length=1, choices=COURSE_TYPE_CHOICES)
    purchase_type = models.CharField(max_length=1, choices=PURCHASE_TYPE_CHOICES, default='s')
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.DurationField()
    picture = models.ImageField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    #for online courses:
    register_deadline = models.DateField(null=True, blank=True)  
    class_link = models.URLField(null=True,blank=True)
    #for offline courses:
    access_expiration = models.DateField(null=True, blank=True)
    offline_video = models.FileField(null=True,blank=True)

    def get_group_price(self, count):
        tier = self.tier_prices.filter(min_members__lte=count, max_members__gte=count).first()

        if tier:
            return tier.price_per_person
        return self.price

    def __str__(self):
        return self.title


class CoursTierPrice(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='tier_prices')
    min_members = models.PositiveIntegerField(default=1)
    max_members = models.PositiveIntegerField(null=True, blank=True)
    price_per_person =  models.PositiveIntegerField()


class GroupMembers(models.Model):
    buyer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | course : {self.course.name} | comment : {self.text} | time : {self.date}'
    

class Enrollment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')


class Ticket(models.Model):

    STATUS_CHOICES=[
        ('1', 'open'),
        ('2', 'in progress'),
        ('3', 'closed'),
    ]

    SECTION_CHOICES=[
        ('1', 'financial'),
        ('2', 'support'),
        ('3', 'educational')
    ]

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class TicketMessage(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)