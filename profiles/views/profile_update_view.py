from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ..models.profile import Profile


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def profile_update_view(request, *args, **kwargs):
    # print(request.data)
    # print("image" in request.FILES)
    # print(request.FILES)
    # print(request.FILES.get("image"))

    user = request.user
    qs = Profile.objects.filter(user__username=request.user).first()

    if not qs:
        return Response({"profile": "perfil não existe"}, status=404)

    # fields = ["name", "bio", "site", "location"]

    qs.name = request.data["name"]
    qs.bio = request.data["bio"]
    qs.site = request.data["site"]
    qs.location = request.data["location"]

    user.first_name = request.data["name"]

    qs.image = request.FILES.get("image")
    # uploaded_avatar = request.data["image"]
    # new_avatar: UploadedFile = Profile(pk=qs.id, image=uploaded_avatar)
    # new_avatar.save()

    # TODO: validação
    qs.save()
    user.save()

    return Response({"profile": "updated"}, status=201)
