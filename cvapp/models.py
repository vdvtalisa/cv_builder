from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    # start by filling out the info you need
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    # image = models.ImageField(null=True, blank=True)

    # add after starting on templates because it's easier
    @property
    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __str__(self):
        return self.full_name


class ContactDetails(models.Model):
    # start by filling out the info you need 2
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    # def __str__(self):
    #     return self.person
#
#
# DEGREE_CHOICES = [
#     ('Phd', 'Phd'),
#     ('Masters', 'Mtech/MA/MSc/MCom/MBA'),
#     ('Bachelors', 'BE/Btech/BA/BSc/BCom'),
#     ('High_school', 'High School')
#     ]
#
# class Education(models.Model):
#
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
#     institution_name = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#
# class WorkExperience(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     company = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     description = models.TextField()
#
#
# class Skills(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     skill_title = models.CharField(max_length=100)
#     skill_detail = models.TextField()
#
#
# class Hobbies(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)