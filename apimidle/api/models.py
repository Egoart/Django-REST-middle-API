from django.db import models


# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=50)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    catchPhrase = models.TextField(blank=True, null=True)
    bs = models.TextField(blank=True, null=True)

    @property
    def company(self):
        return self.company_set.all()


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50)


class Geo(models.Model):
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="geo"
    )
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


class Todos(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField()


class Photo(models.Model):
    albumId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField()
    thumbnailUrl = models.URLField()


class Album(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)


class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()


class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True, blank=True)
    body = models.TextField()
