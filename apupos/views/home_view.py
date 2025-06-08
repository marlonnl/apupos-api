from django.shortcuts import render

def home_view(request, *args, **kwargs):
    # return HttpResponse("<p>Hello</p>")
    return render(request, "pages/home.html", context={}, status=200)