from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

user = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


'''
MDP 
- user
- url_origin
- time
- password
'''


class MdpGenere(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url_origin = models.CharField(max_length=30)
    date_enr = models.DateTimeField(default=timezone.now)
    passwords_generate = models.CharField(max_length=300)

    def __str__(self):
        return self.url_origin
