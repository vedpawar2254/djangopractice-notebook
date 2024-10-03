from django import forms
from .models import Post,Notes,Link,Questions,Message,CompletedStatus,UserEnrolled,Test,Test_Message,DiscussionForum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    
    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('likes','dislikes','completed','enrolled','reply')

        widgets = {
            'Title': forms.TextInput(attrs={"class":'form-control'}),
            'Author': forms.TextInput(attrs={"class":'form-control','value':'', "id":"Author", 'type':'hidden'}),
            'Description': forms.Textarea(attrs={"class":'form-control'}),
            'Goal': forms.TextInput(attrs={"class":'form-control'}),
            
        }


# 'age': forms.DateInput(attrs={"class":'form-control'}),
#             'education': forms.Textarea(attrs={"class":'form-control'}),
#             'WorkType': forms.Textarea(attrs={"class":'form-control'}),
        


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        

        widgets = {
            # 'Link': forms.URLInput(attrs={"class":'form-control'}),
            'Topic': forms.TextInput(attrs={"class":'form-control'}),
            'Notes': forms.Textarea(attrs={"class":'input-group-text'}),
            # 'Questions': forms.Textarea(attrs={"class":'form-control'}),
            'Summary': forms.Textarea(attrs={"class":'form-control'}),
            'post': forms.TextInput(attrs={"class":'form-control','value':'', "id":"post", 'type':'hidden'}),
        }

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'

        widgets = {
            'Link': forms.URLInput(attrs={"class":'form-control'}),
            'Notes': forms.TextInput(attrs={"class":'form-control','value':'', "id":"notes", 'type':'hidden'}),
        }



class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

        widgets = {
            'Questions': forms.Textarea(attrs={"class":'form-control'}),
            'Notes': forms.TextInput(attrs={"class":'form-control','value':'', "id":"questions", 'type':'hidden'}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'body': forms.Textarea(attrs={"class":'form-control'}),
            'notes': forms.TextInput(attrs={"class":'form-control','value':'', "id":"message_notes", 'type':'hidden'}),
            'user': forms.TextInput(attrs={"class":'form-control','value':'', "id":"message_user", 'type':'hidden'}),
        }

        # exclude = ('user','notes')


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

        widgets = {
            'Title': forms.TextInput(attrs={"class":'form-control'}),
            'Summary': forms.Textarea(attrs={"class":'form-control'}),
            'notes': forms.TextInput(attrs={"class":'form-control','value':'', "id":"test_notes", 'type':'hidden'}),
            'user': forms.TextInput(attrs={"class":'form-control','value':'', "id":"test_user", 'type':'hidden'}),
        }


class Test_MessageForm(forms.ModelForm):
    class Meta:
        model = Test_Message
        fields = '__all__'
        exclude = ('notes',)

        widgets = {
            'body': forms.Textarea(attrs={"class":'form-control'}),
            'test': forms.TextInput(attrs={"class":'form-control','value':'', "id":"test_message", 'type':'hidden'}),
            'user': forms.TextInput(attrs={"class":'form-control','value':'', "id":"test_message_user", 'type':'hidden'}),
        }


class DiscussionForumForm(forms.ModelForm):
    class Meta:
        model = DiscussionForum
        fields = '__all__'
        

        widgets = {
            'body': forms.Textarea(attrs={"class":'form-control'}),
            'reply': forms.Select(attrs={"class":'form-control','value':''}),
            'user': forms.TextInput(attrs={"class":'form-control','value':'', "id":"discuss_user", 'type':'hidden'}),
            'notes': forms.TextInput(attrs={"class":'form-control','value':'', "id":"discuss_notes", 'type':'hidden'}),
        }