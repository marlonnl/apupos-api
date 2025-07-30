from rest_framework_simplejwt.authentication import JWTAuthentication


class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("accessToken")
        # print("access:", access_token)
        # print(request.body)

        if not access_token:
            return None

        validated_token = self.get_validated_token(access_token)
        # print("validated:", validated_token)

        try:
            user = self.get_user(validated_token)

        except Exception as e:
            return None

        # print(user, access_token)
        return (user, access_token)
