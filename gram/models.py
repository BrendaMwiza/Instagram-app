from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField(max_length =60)
    user_name = models.ForeignKey(User,on_delete=models.BASCADE, blank=True, related_name="pictures")
    pic = models.ImageField(upload_to='pictures/' null=True)
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

class Profile(models.Model):
    profile = models.ImageField(upload_to='pictures/',blank=True,null=True)
    user_name = models.OneToOneFiled(User, on_delete=models.CASCADE,blank=True,related_name="profile")
    boi = models.TextField(max_length=300,null=True,default="bio")
    follower = models.ManyToManyField(User,related_name="follower",blank=True)
    following = models.ManyToManyField(User,related_name="following",blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def following(self,follower):
        return self.following.add(follower)

    def follows(self,checkuser):
        return checkuser in self.following.all()

    def follow_numb(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def unfollowing(self.unfollow):
        return self.following.remove(unfollow)

    @classmethod
    def search_profile(cls,profile_item):
        pro = cls.objects.filter(user_name__name__icontains=profile_item)

    def __str__(self):
        return self.user_name.username

class Comments(models.Model):
    user_name = models.OneToOneFiled(User, on_delete=models.CASCADE,blank=True,related_name="user_name")
    pic = models.ForeignKey(Image, on_delete=models.CASCADE,blank=True,related_name="comment")
    comment = models.TextField()

    def save_comment(self,id):
        self.save()

    def get_comment_id(self,id):
        comment = Comments.objects.filter(Image_id=id)
        return comment

    def __str__(self):
        return self.user_name.comment