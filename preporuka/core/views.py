from django.shortcuts import render, redirect


def show_home_page(request):
    return render(request, "home.html")