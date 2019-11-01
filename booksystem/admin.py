from django.contrib import admin
from .models import Author, Book_Publisher, Book_Type, Book, Bill, Cashier, Receipt, Book_System, Session

admin.site.register(Book_System)
admin.site.register(Author)
admin.site.register(Book_Publisher)
admin.site.register(Book_Type)
admin.site.register(Book)
admin.site.register(Bill)
admin.site.register(Cashier)
admin.site.register(Receipt)
admin.site.register(Session)