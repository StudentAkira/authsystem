from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None):
        user = self.model(username=username,)
        if not password:
            password = username
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email=None):
        user = self.create_user(username, password, email)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
