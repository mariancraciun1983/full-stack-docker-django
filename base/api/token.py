import jwt
import datetime
from rest_framework import authentication
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from django.utils.functional import SimpleLazyObject


def token_decode(token):
    """
    decode token
    """
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])


def token_encode(data, exp_time=60 * 60 * 24):
    """
    create token
    """
    # We should add soon the exp_time
    return jwt.encode(
        data,
        settings.SECRET_KEY,
        algorithm="HS256",
        headers={
            "exp": str(
                datetime.datetime.utcnow() + datetime.timedelta(seconds=exp_time)
            )
        },
    )


def token_for_user(user):
    return token_encode({"user": user.id})


def token_for_user_id(user_id):
    return token_encode({"user": user_id})


def get_user(request, user_id):
    if not hasattr(request, "_cached_user"):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = AnonymousUser()
        request._cached_user = user
    return request._cached_user


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_X_AUTHORIZATION", "")
        if token:
            try:
                data = token_decode(token)
                if "user" in data:
                    request.user = SimpleLazyObject(
                        lambda: get_user(request, data["user"])
                    )
            except jwt.InvalidTokenError:
                pass
            except:  # noqa: E722
                pass
