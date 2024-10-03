from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager
# Create your models here.

# class User(models.Model):
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.User)




class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Title = models.CharField(max_length=150,blank=True,null=True)
    Description = models.TextField(max_length=650,blank=True,null=True)
    # Subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    # Notes = models.ForeignKey(Notes,on_delete=models.CASCADE,null=True)
    likes = models.ManyToManyField(User, related_name="note_post",blank=True,default=None)
    dislikes = models.ManyToManyField(User, related_name="post_note",blank=True,default=None)
    enrolled = models.ManyToManyField(User, related_name="enrolled",blank=True,default=None)
    # Link = models.ForeignKey(Link,on_delete=models.CASCADE,null=True)
    completed = models.ManyToManyField(User, related_name="completed",blank=True,default=None)
    # DueDate = models.DateTimeField()
    Goal = models.CharField(max_length=1000,blank=True,null=True)
    reply = models.ForeignKey('Post', null=True,blank=True, on_delete=models.DO_NOTHING, related_name="post_reply")


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def total_likes(self):
        return self.likes.all().count()
    
    def __str__(self):
        return str(self.Title) if self.Title else ''

    def get_absolute_url(self):
        return reverse('home')
    
    class Meta:
        ordering = ['updated','-created']

LIKE_CHOICES = (
    ('like','like'),
    ('unlike','unlike')
)
DISLIKE_CHOICES = (
    ('dislike','dislike'),
    ('disunlike','disunlike')
)

ENROLLED_CHOICES = (
    ('enroll','enroll'),
    ('unenroll','unenroll')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=LIKE_CHOICES,default='like', max_length=10)

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=DISLIKE_CHOICES,default='dislike', max_length=10)

class UserEnrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=ENROLLED_CHOICES,default='enrolled', max_length=20)

    def __str__(self):
        return str(self.user) if self.user else ''



class Notes(models.Model):
    # Link = models.URLField(max_length=150,blank=True,null=True)
    # Link = models.ForeignKey(Link,on_delete=models.CASCADE,null=True)
    Topic = models.CharField(max_length=150,blank=True,null=True)
    Notes = RichTextField(blank=True,null=True)
    # Questions = models.TextField(max_length=550,blank=True,null=True)
    Summary = models.TextField(max_length=750,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    # slug = models.SlugField()
    


    class Meta:
        ordering = ['updated','-created']


    
    def __str__(self):
        return self.Topic



class Link(models.Model):
    Link = models.URLField(max_length=350,blank=True,null=True,default='')
    Notes = models.ForeignKey(Notes, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.Link) if self.Link else ''

class Questions(models.Model):
    Questions = models.TextField(max_length=550,blank=True,null=True)
    Notes = models.ForeignKey(Notes, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.Questions) if self.Questions else ''


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.ForeignKey(Notes,related_name="message", on_delete=models.CASCADE,null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


STATUS_CHOICES = (
    ('incomplete','incomplete'),
    ('complete','complete'),
)

class CompletedStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=STATUS_CHOICES,default='incomplete', max_length=10)

    def __str__(self):
        return str(self.user) if self.user else ''



class Test(models.Model):
    Title = models.CharField(max_length=250,null=True) 
    Summary = models.CharField(max_length=3000,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    notes = models.ForeignKey(Notes,related_name="Test_notes", on_delete=models.CASCADE,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.Title) if self.Title else ''



class Test_Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    test = models.ForeignKey(Test,related_name="test_message", on_delete=models.CASCADE,null=True)
    # notes = models.ForeignKey(Notes,related_name="Test_messages", on_delete=models.CASCADE,null=True)
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class DiscussionForum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    notes = models.ForeignKey(Notes,related_name="forum_messages", on_delete=models.CASCADE,null=True)
    reply = models.ForeignKey('DiscussionForum', null=True,blank=True, on_delete=models.DO_NOTHING, related_name="forum_reply")
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]