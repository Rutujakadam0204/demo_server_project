from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views import View

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


# create_random_user_accounts.delay(). This way we are instructing Celery to execute this function in the background.
class GenerateRandomUserView(View):
    # template_name = 'document_form.html'
    # form_class = GenerateRandomUserForm
    def get(self, request):
        form_class = GenerateRandomUserForm
        return render(request, "document_form.html", {'form':form_class})

    def post(self, request):
        total = request.POST.get('total')
        print(total)
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return HttpResponse('hii')