from django.http import HttpResponseRedirect
from django.shortcuts import render


class Lib:

    def index(self,request):
        if self.verificar(request):
            return HttpResponseRedirect('/admin/')
        return render(request, 'index.html')

    def validar(self,request):
        if self.verificar(request):
            return HttpResponseRedirect('/admin/')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            with open('ControlTareas/data/dataUsuarios.txt','r') as f:
                for line in f:
                    if (username == line.split(',')[0]) and (password == line.split(',')[1]):
                        response = HttpResponseRedirect('/admin/')
                        response.set_cookie('my_cookie', 'my_value')
                        return response
            return HttpResponseRedirect('/')

    def admin(self,request):
        if self.verificar(request):
            return render(request, 'admin.html')
        return HttpResponseRedirect('/')

    def logout(self,request):
        response = HttpResponseRedirect('/')
        response.set_cookie('my_cookie', '')
        return response

    def verificar(self,request):
        my_cookie = request.COOKIES.get('my_cookie')
        if my_cookie == 'my_value':
            return True
        return False
    