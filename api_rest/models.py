from django.db import models

class User(models.Model):
    
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_email = models.EmailField(default='')
    user_password = models.CharField(default='', max_length=100)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email} | Password: {self.user_password}'


class UserComments(models.Model):
    airbnb_name = models.CharField(max_length=100, default='')
    user_nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    user_note = models.IntegerField(default=0)
    user_comment = models.CharField(max_length=1000, default='')
    
    class Meta:
        unique_together = ('airbnb_name', 'user_nickname')