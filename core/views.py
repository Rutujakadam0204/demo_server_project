from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.contrib import messages
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Create your views here.

class SignInView(APIView):

    def get(self, request):
        groups = Group.objects.all()
        data = {'groups': groups}
        return Response([{'hi':'hi'}])

    def post(self, request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']
        
        print(email)
        # If user doesn't exist return None
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if User.objects.filter(email=email).exists():  
                correct_password = check_password(password, user.password)
                if correct_password:
                    login(request, user)
                    if email == 'maindash@gmail.com':
                        return Response(data={'redirect_url':'/login2',"message": "Product Successfully Created"})  # reverse of module selection
                    elif email == 'module@gmail.com':
                        return Response(data={'redirect_url':'module',"message": "Product Successfully Created"})
                    else:
                        # return HttpResponseRedirect(reverse('settings:module-permissions', args={"new"}))
                        return Response( data={
                                "status": 201,
                                "message": "Product Successfully Created",                
                                "redirect_url": '/dashboard2',                
                                },
                                status=status.HTTP_201_CREATED,
                                # headers=headers
                                )
                else:
                    messages.error(request, "Please Check your password and email are registered or not.")

            else:
                messages.error(request, "Please renew license or request for license from admin")
        else:
            messages.error(request, 'Sorry something went wrong.')
            return Response([{'hi':'hi'}])
        return Response([{'hi':'hi'}])


from .forms import DocForm
from django.views import View

class DocumentCreateView(View):

    @staticmethod
    def get(request):
        data = {'form':DocForm()}
        return render(request, 'document_form.html', data)

    @staticmethod
    def post(request):
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("ok")
        return render(request, 'document_form.html')
