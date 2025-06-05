from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme

from django.conf import settings
from .models import Apupo
from .forms import ApupoForm


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):
    # return HttpResponse("<p>Hello</p>")
    return render(request, "pages/home.html", context={}, status=200)


def apupo_create_view(request, *args, **kwargs):
    form = ApupoForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url is not None and url_has_allowed_host_and_scheme(next_url, allowed_hosts=ALLOWED_HOSTS):
            return redirect(next_url)
        form = ApupoForm()

    return render(request, "components/form.html", context={"form": form})


def apupo_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    """
    queryset = Apupo.objects.all()
    apupos_list = [{"id": i.id, "content": i.content, "likes": 12} for i in queryset]
    data = {"response": apupos_list}

    return JsonResponse(data)


def apupo_detail_view(request, apupo_id, *args, **kwargs):
    """
    REST API VIEW
    returning JSON data
    """

    data = {
        "id": apupo_id,
        # "image_path": obj.image.url
    }
    status = 200

    try:
        obj = Apupo.objects.get(id=apupo_id)
        data["content"] = obj.content
    except Exception as e:
        data["message"] = f"Apupo with id {apupo_id} was not found"
        status = 404
        # worked with HttpResponse
        # raise Http404

    return JsonResponse(data, status=status)
    # returning a page
    # return HttpResponse(f"<h1>Detail of id {apupo_id}</h1><p>{obj.content}</p>")
