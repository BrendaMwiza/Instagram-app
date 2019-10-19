from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField(max_length =60)
    user_name = models.ForeignKey(User,on_delete=models.BASCADE, blank=True, related_name="pictures")
    image = models.ImageField(upload_to='pictures/' null=True)
    comment = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_pic(self):
        self.save()  

    def delete_pic(cls,id):
        pic = cls.objects.get(PrimaryKey=id)
        pic.delete()

    @classmethod
    def update_pic(cls,update):
        pic = cls.objects.filter(id=id).update(id=id)
        return pic

    @classmethod
    def get_pic_by_di(cls,id):
        pic = cls.objects.get(PrimaryKey=id)
        return pic

    @classmethod
    def search_user(cls,user_item):
        pic = cls.objects.filter(name__icontains=user_item)

class Follower(models.Model):
    user_name = models.CharField(max_length=30,default="")
    followers = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile)


    