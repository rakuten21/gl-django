from django.shortcuts import render

# Create your views here.

def display_users(request):
    return render(request, 'user_management/um_tab_panel.html')
