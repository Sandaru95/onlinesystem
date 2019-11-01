from django.db import models
from accounts.models import Signal_User_Profile
import time

class Book_System(models.Model):
    name = models.CharField(max_length=300, null=True)
    signal_user_profile = models.ForeignKey(Signal_User_Profile, on_delete=models.CASCADE)
    receipt_publisher_name = models.CharField(max_length=500, null=True)
    receipt_publisher_address = models.CharField(max_length=800, null=True)
    receipt_greenting_text = models.CharField(max_length=800, null=True)
    receipt_date = models.BooleanField(default=True, null=True)
    receipt_no_items = models.BooleanField(default=True, null=True)
    receipt_subtotal = models.BooleanField(default=True, null=True)
    receipt_total = models.BooleanField(default=True, null=True)
    # The Totals of the book system
    booksystem_today_total = models.IntegerField(default=0)
    booksystem_total = models.IntegerField(default=0)
    booksystem_drawer_total = models.IntegerField(default=0)

    def __str__(self):
        return self.signal_user_profile.name + ' ~ BookSystem: ' + str(self.pk)

class Session(models.Model):
    day_total      = models.IntegerField()
    ended_at       = models.DateTimeField(auto_now_add=True)
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.owner_book_system.signal_user_profile.name) + ' : ' + str(self.day_total)

class Book_Publisher(models.Model):
    name = models.CharField(max_length=500)
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name) 

class Author(models.Model):
    name        = models.CharField(max_length=1000)
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name) 

class Book_Type(models.Model):
    title = models.CharField(max_length=500)
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.title) 

class Book(models.Model):
    book_name   = models.CharField(max_length=500)
    book_type   = models.ForeignKey(Book_Type, on_delete=models.CASCADE)
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE)
    book_price  = models.IntegerField()
    item_code   = models.IntegerField()
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher   = models.ForeignKey(Book_Publisher, on_delete=models.CASCADE)
    stock       = models.IntegerField()

    def __str__(self):
        return str(self.book_name) + " | Rs." + str(self.book_price) + " | " + str(self.item_code) 

class Bill(models.Model):
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)
    no_items        = models.IntegerField()
    cashier         = models.CharField(max_length=100, default="Common")
    list_of_items   = models.CharField(max_length=10000)
    billed_at       = models.DateTimeField(auto_now_add=True)
    total           = models.IntegerField(default=200)

    class Meta:
            get_latest_by = 'billed_at'

    def __str__(self):
        return str(self.cashier) + " | " + str(self.no_items) + " | " + str(self.billed_at)

class Cashier(models.Model):
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)
    username    = models.CharField(max_length=500)
    password    = models.CharField(max_length=500)
    is_admin    = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username) 

class Receipt(models.Model):
    owner_book_system = models.ForeignKey(Book_System, on_delete=models.CASCADE, blank=True, null=True)
    item_decription = models.TextField(max_length=50000)
    no_items = models.IntegerField()
    sub_total = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(f'Rs.{self.total}')