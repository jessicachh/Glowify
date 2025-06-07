from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings  # Import settings
from django.contrib.auth import get_user_model 

# Custom manager for the CustomUser model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password)

# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    objects = CustomUserManager()  

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    