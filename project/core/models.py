from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = "menu-images/", null=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PREPARING = 'P', 'Preparing'
        READY = 'R', 'Ready'
        SERVED = 'S', 'Served'

    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    total_price = models.DecimalField()
    status = models.CharField(max_length=1, choices=StatusChoices , default=StatusChoices.PREPARING) 

    def __str__(self):
        return f"{self.table} - {self.status}"

class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField()

    def __str__(self):
        return f"{self.menuitem} x {self.quantity} = {self.total}"