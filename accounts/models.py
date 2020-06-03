from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password= None, full_name = None, is_active = True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name
        )
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_staffuser(self, email, password):
        if password is None:
            raise TypeError('Staffusers must have a password.')
        user = self.create_user(
            email,
            password,
            full_name = None,
            is_staff = True
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(
            email,
            password,
            full_name = None,
            is_staff = True,
            is_admin = True
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        default = "",
        verbose_name= 'email address',
        max_length = 255,
        unique= True
    )
    full_name = models.CharField(max_length = 225, blank = True, null = True, default = "")
    active = models.BooleanField(default =True)
    staff = models.BooleanField(default= False) #staff user non superuser
    admin = models.BooleanField(default = False) #superuser
    objects= UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email and passwords are required by default

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.full_name

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
