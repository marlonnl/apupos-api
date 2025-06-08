from django.http import JsonResponse

from ..models.apupo import Apupo


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
