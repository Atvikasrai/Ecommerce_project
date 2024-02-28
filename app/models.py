from django.db import models
from django.contrib.auth.models import User
from user.models import Customer

# Create your models here.
#-------------------------------------------Product-Model-------------------------------------------------------

CATEGORY_CHOICES = (
    ('WT', 'Smartwatch'),
    ('SM', 'Smartphone'),
    ('LAP', 'Laptop'),
)
   
class Product(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    company = models.CharField(max_length = 60)
    owner = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    os = models.CharField(max_length = 30,blank = True)
    description = models.TextField(default = '5G-Smartphone')
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return str(self.title) 

#-------------------------------------------Cart-Model-------------------------------------------------------

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

#-------------------------------------------Payment-Model-------------------------------------------------------
    
class Payment(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True,null=True)
    paid = models.BooleanField(default=False)

    
#-------------------------------------------Order-Model-------------------------------------------------------
STATUS_CHOICES =(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
                 
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_dateb = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='Pending',choices=STATUS_CHOICES)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

