from django.shortcuts import redirect
from django.views import generic

class returnToHomeView(generic.View):
    def get(self, request):
        return redirect('home:index')