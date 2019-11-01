from django.shortcuts import render, HttpResponse
from django.views import generic

from booksystem.models import Book_System

class IndexView(generic.View):
    template_name = 'dashboard/index.html'
    context = {}
    def get(self, request):
        self.context['book_system_list'] = Book_System.objects.filter(signal_user_profile=request.user.signal_user_profile)
        return render(request, self.template_name, self.context)

class CreateInstanceView(generic.View):
    template_name = 'dashboard/create.html'
    context = {}
    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        sys_type = request.POST['sysType']
        sys_name = request.POST['sysName']
        selected_img = request.POST['selectedImg']
        if sys_type == 'book':
            new_book_system = Book_System()
            new_book_system.name = sys_name
            new_book_system.signal_user_profile = request.user.signal_user_profile
            new_book_system.save()
            return HttpResponse('Success in creation!')
