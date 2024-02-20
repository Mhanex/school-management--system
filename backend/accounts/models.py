# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# # Create your models here.
# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)

#         user.set_password(password)
#         user.save()

#         return user
    
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

    
# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)


#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     # def get_full_name(self):
#     #     return f"{self.first_name} {self.last_name}"
    
#     def get_short_name(self):
#         return self.username

#     def __str__(self):
#         return self.email
    
    



















# # class Staff(models.Model):
    
# #     TITLE_CHOICES = [
# #         ("MR", "Mr"),
# #         ("MRS", "Mrs"),
# #         ("MISS", "Miss"),
# #     ]

# #     GENDER_CHOICES = [
# #         ("M", "Male"),
# #         ("F", "Female"),
# #         ("O", "Other")
# #     ]

# #     QUALIFICATION_CHOICES = [
# #         ("PHD", "PhD"),
# #     ]

# #     ROLE_CHOICES = [
# #         ("SA", "Super Admin"),
# #         ("A", "Junior Admin"),
# #         ("I", "Instructor"),
# #     ]

# #     title = models.CharField(max_length=4, choices=TITLE_CHOICES)
# #     first_name = models.CharField(max_length=100, null=True, blank=True)
# #     middle_name = models.CharField(max_length=100)
# #     last_name = models.CharField(max_length=100)
# #     gender =  models.CharField(max_length=1, choices=GENDER_CHOICES)
# #     dob = models.DateField()
# #     phone = models.CharField(max_length=50)
# #     email = models.CharField(max_length=150)
#     # nationality = 
#     # state = 
#     # contact =
#     # qualification = models.CharField(max_length=4, choices=QUALIFICATION_CHOICES)
#     # role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    








from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# inheriting from the abstract user to have more control of the fields


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_deactivated = models.BooleanField(default=False)

