from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=25, verbose_name="Name of user")
    age = models.IntegerField(verbose_name="Age of the user")
    object_person = models.Manager()
    DoesNotExist = models.Manager


class Company(models.Model):
    name = models.CharField(max_length=25)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    price = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=25)


class Student(models.Model):
    name = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course)


class User(models.Model):
    name = models.CharField(max_length=25)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Image(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='Description of image')
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Work with images')
    obj_img = models.Manager()

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=100, verbose_name='Description of file')
    file = models.FileField(upload_to='files', null=True, blank=True, verbose_name='File PDF')

    def __str__(self):
        return self.title
    