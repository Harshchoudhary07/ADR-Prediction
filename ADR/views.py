from django.shortcuts import render

def home(request):
    return render(request, 'ADR/home.html')  # ✅ Correct indentation
