from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    category_choices = [
        (1,"Bó Hoa"),(2,"Giỏ Hoa"),
        (3,"Hoa Đám Cưới"),(4,"Hoa Khai Trương"),
        (5,"Hoa Sinh Nhật"),(6,"Hoa Tình Yêu"),
        (7,"Hoa Baby"),(8,"Cúc Mẫu Đơn"),       
        (9,"Chậu Lan Hồ Điệp"),(10,"Hoa Tốt Ngiệp"),
        (11,"Giỏ Trái Cây"),(12,"Mâu Hoa Mới"),
    ]
    name = models.CharField(max_length=50,default="abc",null=True)
    category = models.IntegerField(choices=category_choices, default=1)
    product_code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=3)
    image = models.ImageField(null=True , blank=True)
    description = models.TextField(null=True , max_length=255)
    def __str__(self):
        return self.name

