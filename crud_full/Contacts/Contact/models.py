from django.db import models

# Create your models here.
class Person(models.Model):
    aadhar = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    mobile = models.CharField(max_length=30)
    dp_pic = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        ret = f"""
        aadhar: {self.aadhar}
        name: {self.name}
        DOB: {self.dob}
        email: {self.email}
        mobile: {self.mobile}
        dp pic: {self.dp_pic}
        """
        return ret