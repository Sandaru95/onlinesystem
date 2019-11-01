from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Author, Book_Publisher, Book_Type, Cashier, Book, Receipt, Book_System, Session
from accounts.models import Signal_User_Profile


# Forward Interface
class IndexView(generic.View):
    context = {
        'code_to_execute': "",
    }

    def get(self, request, pk):
        # Getting the Current book system
        self.context['current_book_system'] = Book_System.objects.get(pk=pk)
        # End of getting Current book system
        # The Context
        self.context['book_list'] = Book.objects.filter(owner_book_system=self.context['current_book_system'])
        self.context['receipt_list'] = Receipt.objects.filter(owner_book_system=self.context['current_book_system'])
        # End of the Context ==================================================
        self.context['code_to_execute'] = "console.log('GET SO NOTHING HERE!')"
        return render(request, 'booksystem/index.html', self.context)

    def post(self, request, pk):
        book_pk_list = []
        book_qty_list = []
        receipt_description = '['
        for post in request.POST:
            if 'book_pk' in post:
                book_pk_list.append(request.POST[post])
            if 'book_qty' in post:
                book_qty_list.append(request.POST[post])

        for pk in book_pk_list:
            # Subtracting the qty from stock
            book_ins_filtered = Book.objects.get(pk=int(pk))
            book_ins_filtered.stock -= int(book_qty_list[book_pk_list.index(pk)])
            book_ins_filtered.save()
            # Making the receipt description
            receipt_description += "{bookName: '" + book_ins_filtered.book_name + "', qty: " + str(book_qty_list[book_pk_list.index(pk)]) + ', price:' + str(book_ins_filtered.book_price) + '},'
        receipt_description += ']'
        # Making the Receipt
        new_receipt = Receipt()
        new_receipt.item_decription = receipt_description
        new_receipt.no_items = len(book_pk_list)
        new_receipt.sub_total = request.POST['subtotal-input']
        new_receipt.total = request.POST['total-input']
        print(pk)
        new_receipt.owner_book_system = Book_System.objects.get(pk=int(request.POST['current_book_system_pk']))
        new_receipt.save()
        # Receipt Saved
        current_book_system = Book_System.objects.get(pk=int(request.POST['current_book_system_pk']))
        current_book_system.booksystem_total += int(request.POST['total-input'])
        current_book_system.booksystem_today_total += int(request.POST['total-input'])
        current_book_system.booksystem_drawer_total += int(request.POST['total-input'])
        current_book_system.save()
        
        # The Code to Execute is to Print the Last Receipt
        the_code_to_execute = "window.open('/booksystem/" + str(request.POST['current_book_system_pk']) + "/receipts/last/')"
        self.context['code_to_execute'] = the_code_to_execute

        return render(request, 'booksystem/index.html', self.context)    
# ======================================================================================




# Backend
class BackendView(generic.TemplateView):
    template_name = 'booksystem/backend.html'

    def get_context_data(self, **kwargs):
        context = super(BackendView, self).get_context_data(**kwargs)
        context['author_list'] = Author.objects.filter(owner_book_system = self.kwargs['pk'])
        context['publisher_list'] = Book_Publisher.objects.filter(owner_book_system = self.kwargs['pk'])
        context['book_type_list'] = Book_Type.objects.filter(owner_book_system = self.kwargs['pk'])
        # The Owner Book System
        context['current_book_system'] = Book_System.objects.get(pk=self.kwargs['pk'])
        return context

class CreateAuthorView(generic.View):
    def post(self, request):
        new_author = Author(name=request.POST['author_name'])
        # The Owner Book System
        new_author.owner_book_system = Book_System.objects.get(pk=request.POST['current_book_system_pk'])
        new_author.save()
        return HttpResponse('Success')

class CreatePublisherView(generic.View):
    def post(self, request):
        new_pub = Book_Publisher(name=request.POST['book_publisher_name'])
        # The Owner Book System
        new_pub.owner_book_system = Book_System.objects.get(pk=request.POST['current_book_system_pk'])
        new_pub.save()
        return HttpResponse('Success')

class CreateBookTypeView(generic.View):
    def post(self, request):
        new_type = Book_Type(title=request.POST['book_type_name'])
        # The Owner Book System
        new_type.owner_book_system = Book_System.objects.get(pk=request.POST['current_book_system_pk'])
        new_type.save()
        return HttpResponse('Success')

class createCashierView(generic.View):
    def post(self, request):
        new_cashier = Cashier(
            username=request.POST['cashier_username'], 
            password=request.POST['cashier_password'],
            # The Owner Book System
            owner_book_system = Book_System.objects.get(pk=request.POST['current_book_system_pk']) 
        )
        new_cashier.save()
        return HttpResponse('Success')

class createBookView(generic.View):
    def post(self, request):
        new_book = Book()
        new_book.book_name = request.POST['book_name']
        new_book.book_type = Book_Type.objects.get(title__contains=request.POST['book_type'])
        new_book.book_price = int(request.POST['book_price'])
        new_book.item_code = int(request.POST['book_item_code'])
        new_book.author = Author.objects.get(name__contains=request.POST['book_author'])
        new_book.publisher = Book_Publisher.objects.get(name__contains=request.POST['book_publisher'])
        new_book.stock = int(request.POST['book_stock'])
        # The Owner Book System
        new_book.owner_book_system = Book_System.objects.get(pk=request.POST['current_book_system_pk'])

        new_book.save()
        return HttpResponse('Success')
# ======================================================================================




# Receipts
class receiptsView(generic.TemplateView):
    template_name = 'booksystem/receipts.html'
    
    def get_context_data(self, **kwargs):
        context = super(receiptsView, self).get_context_data(**kwargs)
        # Related Receipt for current book system
        context['receipt_list'] = Receipt.objects.filter(owner_book_system=(self.kwargs['pk']))
        # The Current Book System for essential Pass
        context['current_book_system'] = Book_System.objects.get(pk=self.kwargs['pk'])
        return context

class lastReceiptsView(generic.TemplateView):
    template_name = 'booksystem/last_receipts.html'

    def get_context_data(self, **kwargs):
        context = super(lastReceiptsView, self).get_context_data(**kwargs)
        context['last_receipt'] = Receipt.objects.filter(owner_book_system=(self.kwargs['pk'])).order_by('-id')[0]
        # The Current Book System for essential Pass
        context['current_book_system'] = Book_System.objects.get(pk=self.kwargs['pk'])
        return context

class ReceiptsSettingsView(generic.View):
    template_name = 'booksystem/receipts_settings.html'
    context = {}

    def get(self, request, pk):
        self.context['current_book_system'] = Book_System.objects.get(pk=pk)
        return render(request, self.template_name, self.context)

    def post(self, request, pk):
        book_system = Book_System.objects.get(pk=request.POST['current_book_system_pk'])
        book_system.receipt_publisher_name = request.POST['publisherName']
        book_system.receipt_publisher_address = request.POST['publisherAddress']
        book_system.receipt_greenting_text = request.POST['greentingText']
        # Enable or Disable Things 
        book_system.receipt_date = request.POST['DateBoolean']
        book_system.receipt_no_items = request.POST['noItemsBoolean']
        book_system.receipt_subtotal = request.POST['subTotalBoolean']
        book_system.receipt_total = request.POST['totalBoolean']

        book_system.save()
        return HttpResponse("window.close()")
# ====================================================================================== 


# Without Stock
class WithoutStockView(generic.View):
    context = {
        'receipt_list': Receipt.objects.all(),
        'code_to_execute': "",
    }

    def get(self, request, pk):
        self.context['code_to_execute'] = "'GET SO NOTHING HERE!'"
        print(Book_System.objects.get(pk=pk))
        self.context['current_book_system'] = Book_System.objects.get(pk=pk)
        return render(request, 'booksystem/without_stock.html', self.context)

    def post(self, request, pk):
        book_price_list = []
        book_qty_list = []
        receipt_description = '['
        for post in request.POST:
            if 'book_price' in post:
                book_price_list.append(request.POST[post])
            if 'book_qty' in post:
                book_qty_list.append(request.POST[post])

        for price in book_price_list:
            # Making the receipt description
            receipt_description += "{bookName: " + "'other'" + ", qty: " + str(book_qty_list[book_price_list.index(price)]) + ", price:" + str(price) + "},"
        receipt_description += "]"
        # Making the Receipt
        for i in request.POST:
            print(i + ' : ' + request.POST[i])
        new_receipt = Receipt()
        new_receipt.item_decription = receipt_description
        new_receipt.no_items = len(book_price_list)
        new_receipt.sub_total = request.POST['without-stock-subtotal-input']
        new_receipt.total = request.POST['without-stock-total-input']
        new_receipt.owner_book_system = Book_System.objects.get(pk=pk)
        new_receipt.save()
        # Receipt Saved
        current_book_system = Book_System.objects.get(pk=pk)
        current_book_system.booksystem_total += int(request.POST['without-stock-total-input'])
        current_book_system.booksystem_today_total += int(request.POST['without-stock-total-input'])
        current_book_system.booksystem_drawer_total += int(request.POST['without-stock-total-input'])
        current_book_system.save()

        # The Code to Execute is to Print the Last Receipt
        the_code_to_execute = "window.open('/booksystem/" + str(pk) + "/receipts/last/')"
        self.context['code_to_execute'] = the_code_to_execute
        return render(request, 'booksystem/without_stock.html', self.context)    
# ====================================================================================== 


# Shortcut
class ShortCutView(generic.TemplateView):
    template_name = 'booksystem/shortcuts.html'

    def get_context_data(self, **kwargs):
        context = super(ShortCutView, self).get_context_data(**kwargs)
        context["current_book_system"] = Book_System.objects.get(pk=self.kwargs['pk']) 
        return context
    

# ====================================================================================== 

# Reports

class ReportsView(generic.TemplateView):
    template_name = 'booksystem/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportsView, self).get_context_data(**kwargs)
        context['current_book_system'] = Book_System.objects.get(pk=self.kwargs['pk'])
        return context

class ReportsAddCashView(generic.View):
    def post(self, request, pk):
        amount_added = int(request.POST['amount_added'])
        current_book_system = Book_System.objects.get(pk=int(request.POST['current_book_system_pk']))
        current_book_system.booksystem_drawer_total += amount_added
        current_book_system.save()
        return HttpResponse('Success!')

class ReportsDrawCashView(generic.View):
    def post(self, request, pk):
        amount_drawed = int(request.POST['amount_drawed'])
        current_book_system = Book_System.objects.get(pk=int(request.POST['current_book_system_pk']))
        current_book_system.booksystem_drawer_total -= amount_drawed
        current_book_system.save()
        return HttpResponse('Success!')
# ======================================================================================

# End Day
class EndDayView(generic.View):
    def post(self, request, pk):
        # Current book system
        current_book_system = Book_System.objects.get(pk=int(request.POST['current_book_system_pk']))
        # new sessions
        new_session = Session()
        new_session.day_total = current_book_system.booksystem_today_total
        new_session.owner_book_system = current_book_system
        new_session.save()
        # Resetting current book system total
        current_book_system.booksystem_today_total = 0
        current_book_system.save()
        print('We got end day success!')
        return HttpResponse('Success!')