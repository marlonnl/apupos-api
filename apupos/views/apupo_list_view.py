from django.http import JsonResponse

from ..models.apupo import Apupo


def apupo_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    """
    queryset = Apupo.objects.all()
    apupos_list = [{"id": i.id, "content": i.content, "likes": 12} for i in queryset]
    data = {"response": apupos_list}

    return JsonResponse(data)
