from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse




class HomepageView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
    
