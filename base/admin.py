from django.contrib import admin
from .models import Post,Notes,Like,Dislike,Link,Questions,Message,UserEnrolled,CompletedStatus,Test,Test_Message,DiscussionForum

# Register your models here.


admin.site.register(Post)
admin.site.register(Notes)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Link)
admin.site.register(Message)
# admin.site.register(User)
admin.site.register(UserEnrolled)
admin.site.register(CompletedStatus)
admin.site.register(Test)
admin.site.register(Test_Message)
admin.site.register(DiscussionForum)