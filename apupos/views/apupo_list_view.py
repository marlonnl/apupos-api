from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from ..models.apupo import Apupo
from ..serializers.apupo_serializer import ApupoSerializer


PAGE_SIZE = 20


def get_paginated_qs_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = PAGE_SIZE

    paginated_queryset = paginator.paginate_queryset(qs, request)
    serializer = ApupoSerializer(paginated_queryset, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def apupo_list_view(request, *args, **kwargs):
    """
    Returns all posts.
    If a "username" is not provided, it returns all posts.
    """

    queryset = Apupo.objects.all()

    username = request.GET.get("username")  # url.. ?username={username}
    if username is not None:
        queryset = queryset.by_username(username)

    # serializer = ApupoSerializer(queryset, many=True)

    # print(serializer.data)
    # return Response(serializer.data, status=200)
    return get_paginated_qs_response(queryset, request)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def apupo_feed_view(request, *args, **kwargs):
    """
    REST API / GET method
    Returns all posts from the authenticated user.
    """

    user = request.user

    queryset = Apupo.objects.feed(user)
    # serializer = ApupoSerializer(queryset, many=True)

    # return Response(serializer.data, status=200)
    return get_paginated_qs_response(queryset, request)
