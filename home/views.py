from django.shortcuts import render, HttpResponse, Http404
from django.views import generic
from .models import Message

class IndexView(generic.View):
    template_name = 'home/index.html'
    context = {}
    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.POST['message_input_name'] and request.POST['message_input_email'] and request.POST['message_input_text']:
            new_message = Message()
            new_message.name = request.POST['message_input_name']
            new_message.email = request.POST['message_input_email']
            new_message.message = request.POST['message_input_text']
            new_message.save()

            return HttpResponse('Success!') 
        else:
            return Http404('Error!')
    