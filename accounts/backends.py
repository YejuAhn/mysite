from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist

from .models import User

#customizing authentication to work only with email and username
class UserBackend(ModelBackend):
    def authenticate(self, request, email = None, password = None, **kwargs):
        email = email
        password = password
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except ObjectDoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

