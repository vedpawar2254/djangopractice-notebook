from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Notes,Like,Dislike,Link,Questions,User,Message,CompletedStatus,UserEnrolled,Test,Test_Message,DiscussionForum
from .forms import PostForm,NotesForm,LinkForm,QuestionsForm,MessageForm,TestForm,Test_MessageForm,DiscussionForumForm
from django.views.generic import DetailView,CreateView
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse








# Create your views here.







def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            username = User.objects.get(username=username)
        except:
            messages.error(request, messages.WARNING, "User does not exist")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,messages.INFO,  'Username OR password does not exit')

    context = {"page": page}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.user.is_authenticated:
        messages.error(request, 'Username OR password does not exit')
        return redirect('home')


    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # user = form.save(commit=False)
                user = form.save()
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    posts = Post.objects.all().order_by('-likes')
    def  get_context_data(self, **kwargs):
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        return context
    
    context = {"posts":posts}
    return render(request, 'base/home.html', context)





def Post_search(request):
    q = request.GET.get('q1') if request.GET.get('q1') != None else ''

    post = Post.objects.filter(
        Q(Author__icontains=q) |
        Q(Title__icontains=q) |
        Q(Description__icontains=q) 
    )

    context = {"post":post}
    return render(request, 'base/home.html', context)

# def new(request,pk):
#     notes = Notes.objects.values_list('post.id')
#     context = {"notes": notes}
#     return render(request, 'base/home.html', context)
@login_required(login_url='login')
def form(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # reply_id = request.POST.get('post_id')
            # reply_qs = None
            # if reply_id:
            #     reply_qs = Post.objects.get(id=reply_id)
            # form = Post.objects.create(reply=reply_qs)
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'base/Form.html', context)



def replyForm(request,pk):
    posts = Post.objects.get(id=pk)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        reply = Post.objects.get(id=pk)
        if form.is_valid():
            
            print(reply,pk, "AAa")
            form = Post.objects.create(
                Title=request.POST.get('Title'),
                Description=request.POST.get('Description'),
                Goal=request.POST.get('Goal'),
                Author=request.user,
                )
            form.reply = reply
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'base/Form.html', context)


@login_required(login_url='login')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')

def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/form.html' ,{"form": form})

@login_required(login_url='login')
def Notesform(request,pk):
    notes_form = NotesForm()
    notes = Notes.objects.filter(post=pk)
    post = Post.objects.filter(id=pk)
    print(post)
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"notes_form":notes_form,"post":post,"notes":notes}
    return render(request, 'base/NotesForm.html', context)

@login_required(login_url='login')
def Notes_Feed(request,pk):
    # user = User.objects.get(id=pk)
    notes = Notes.objects.filter(post=pk).order_by('-created')
    post = Post.objects.filter(id=pk)
    links = Link.objects.filter(Notes=pk)
    questions = Questions.objects.filter(Notes=pk)
    notes_messages = ''
    for posts in post:
        userenrolled = posts.enrolled.all()
    

    for notes_messages in notes_messages:
        notes_messages = notes.message_set.all()
    # if links.exists():
    #     links = links[0]
    # else:
    #     links = links
    post1 = Post.objects.filter(Author=request.user)
    notes1 = Notes.objects.filter(post=pk)
    if notes1.exists():
        notes1 = notes1[0]
    else:
        notes1 = notes1

    # if request.method == "POST":
    #     enrolled = post.enrolled.all()
    
    context = {"notes":notes,"post":post,"notes1":notes1,
    "links":links,"questions":questions,"userenrolled":userenrolled}
    return render(request, 'base/Notes.html', context)

def Notes_Search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    notes = Notes.objects.filter(
        Q(Topic__icontains=q) |
        Q(Notes__icontains=q) |
        Q(questions__icontains=q) |
        Q(Summary__icontains=q) |
        Q(Link__icontains=q) 
    )

    context = {"notes":notes}
    return render(request, 'base/Notes.html', context)

# class Notes_Feed(DetailView):
#     model = Notes
#     template_name = 'Notes.html'
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'


@login_required(login_url='login')
def DeleteNotes(request,pk):
    notes = Notes.objects.get(id=pk)
    notes.delete()
    return redirect('home')


@login_required(login_url='login')
def UpdateNotes(request,pk):
    notes = Notes.objects.get(id=pk)
    notes_form = NotesForm(instance=notes)
    post = Post.objects.filter(id=pk)
    links = Link.objects.filter(Notes=pk)
    if request.method == 'POST':
        notes_form = NotesForm(request.POST, request.FILES, instance=notes)
        if notes_form.is_valid():
            notes_form.save()
            return redirect('home')
    context = {"notes_form": notes_form,"links":links,"post":post}
    return render(request, 'base/Notesform.html' ,context)


@login_required(login_url='login')
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        like, created = Like.objects.get_or_create(user=user,post_id=post_id)

        if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'

        like.save()

    return redirect('home')


@login_required(login_url='login')
def dislike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        if user in post.dislikes.all():
            post.dislikes.remove(user)
        else:
            post.dislikes.add(user)

        dislike, created = Dislike.objects.get_or_create(user=user,post_id=post_id)

        if not created:
            if dislike.value == 'dislike':
                dislike.value = 'undislike'
            else:
                dislike.value = 'dislike'

        dislike.save()

    return redirect('home')




@login_required(login_url='login')
def Linkform(request,pk):
    notes = Notes.objects.filter(post=pk)
    Links = Link.objects.filter(id=pk)
    link_form = LinkForm()
    post = Post.objects.filter(id=pk)
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes',pk=pk)
    context = {"link_form":link_form,"Links":Links,"post":post,"notes":notes}
    return render(request, 'base/LinkForm.html', context)


@login_required(login_url='login')
def Questions_Form(request,pk):
    notes = Notes.objects.filter(post=pk)
    questions = Questions.objects.filter(id=pk)
    questions_form = QuestionsForm()
    post = Post.objects.filter(id=pk)
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes',pk=pk)
    context = {"questions_form":questions_form,"questions":questions,"post":post,"notes":notes}
    return render(request, 'base/QuestionsForm.html', context)

@login_required(login_url='login')
def Profile(request,pk):
    post = Post.objects.all()
    user = User.objects.get(id=pk)
    context={"user":user,"post":post}
    return render(request, 'base/Profile.html', context)




@login_required(login_url='login')
def AddMessage(request,pk,pk2):
    # message = Message.objects.get(id=pk)
    
    notes = Notes.objects.get(id=pk)
    post = Post.objects.get(id=pk2)
    
    message_form = MessageForm()
    if request.method == "POST":
        notes = Notes.objects.get(id=pk)
        
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.user = request.user
            message_form.save()
            return redirect('notes',pk2)

    context = {"message_form":message_form,"notes":notes}

    return render(request, 'base/AddMessage.html',context)



@login_required(login_url='login')
def DeleteMessage(request,pk,pk2):
    message = Message.objects.get(id=pk2)
    post = Post.objects.get(id=pk)
    message.delete()
    # notes = Notes.objects.get(id=pk)
    return redirect('notes', pk)
    

@login_required(login_url='login')
def UpdateMessage(request,pk,pk2,pk3):
    post = Post.objects.get(id=pk)
    notes = Notes.objects.get(id=pk3)
    message = Message.objects.get(id=pk2)
    message_form = MessageForm(instance=message)
    if request.method == 'POST':
        message_form = MessageForm(request.POST, request.FILES, instance = message)
        notes = Notes.objects.get(id=pk)
        if message_form.is_valid():
            message_form.save()
            return redirect('notes', pk)
    return render(request, 'base/AddMessage.html' ,{"message_form": message_form,"notes":notes})


@login_required(login_url='login')
def completed(request,pk):
    user = request.user
    
    if request.method == 'POST':
        post_id = Post.objects.get(id=pk)
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        if user in post.completed.all():
            post.completed.remove(user)
        else:
            post.completed.add(user)

        completed, created = CompletedStatus.objects.get_or_create(user=user,post_id=post_id)

        if not created:
            if completed.value == 'completed':
                completed.value = 'incomplete'
            else:
                completed.value = 'completed'

        completed.save()

    return redirect('notes', pk)


@login_required(login_url='login')
def Enroll(request,pk):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        if user in post.enrolled.all():
            post.enrolled.remove(user)
        else:
            post.enrolled.add(user)

        enroll, created = UserEnrolled.objects.get_or_create(user=user,post_id=post_id)

        if not created:
            if enroll.value == 'enroll':
                enroll.value = 'unenroll'
            else:
                enroll.value = 'enroll'

        enroll.save()

    return redirect('notes', pk)



@login_required(login_url='login')
def Acountability(request,pk):
    post = Post.objects.get(id=pk)
    completedusers = post.completed.all()
    # for completedusers in completedusers_id:
    enrolledusers = post.enrolled.all()
    notcompleted = enrolledusers.difference(completedusers)
    # enrolledusers = (p.id for p in enrolledusers)
    # completedusers = (p.id for p in completedusers)
    # enrolledusers = enrolledusers.exclude(enrolledusers = completedusers)
    context={"enrolledusers":enrolledusers,"completedusers":completedusers,"notcompleted":notcompleted}
    return render(request, 'base/Acountability.html',context)


@login_required(login_url='login')
def Discussion(request,pk):
    
    messages = DiscussionForum.objects.filter(id=pk)
    message_form = DiscussionForumForm()
    notes = Notes.objects.get(id=pk)
    if request.method == "POST":
        message_form = DiscussionForumForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            return redirect('discussion',pk)
    context = {"message_form":message_form,"notes":notes,"messages":messages}
    return render(request, 'base/DiscussionForum.html',context)



@login_required(login_url='login')
def Test_Form(request,pk,pk2):
    test_message = Test_Message.objects.all()
    post = Post.objects.filter(id=pk)
    test_form = TestForm()
    notes = Notes.objects.filter(id=pk2)
    
    if request.method == "POST":
        test_form = TestForm(request.POST)
        notes = Notes.objects.filter(id=pk2)
        if test_form.is_valid():
            test_form.user = request.user
            test_form.save()
            return redirect('tests',pk, pk2)
    context = {"test_form":test_form,"post":post,"notes":notes,"test_message":test_message}
    return render(request, 'base/testForm.html',context)



@login_required(login_url='login')
def Tests(request,pk,pk2):
    notes = Notes.objects.filter(id=pk2)
    post = Post.objects.filter(id=pk)
    tests = Test.objects.filter(notes=pk)
    Tests_messages =  Test_Message.objects.all()
    
    # for tests_messages in tests_messages:
    #     tests_messages = 

    print(Tests_messages)
    context = {"tests":tests,"post":post,"notes":notes,"Tests_messages":Tests_messages}
    return render(request, 'base/test.html',context)



@login_required(login_url='login')
def AddTestMessage(request,pk,pk2,pk3):
    # message = Message.objects.get(id=pk)
    
    test = Test.objects.get(id=pk3)
    
    test_messageForm = Test_MessageForm()
    if request.method == "POST":
        test = Test.objects.get(id=pk3)
        
        test_messageForm = Test_MessageForm(request.POST)
        if test_messageForm.is_valid():
            test_messageForm.user = request.user
            test_messageForm.save()
            return redirect('tests', pk,pk2 )

    context = {"test_messageForm":test_messageForm,"test":test}

    return render(request, 'base/AddTest_Message.html',context)



def DeleteTests(request,pk,pk2):
    print(pk2)
    tests = Test.objects.get(id=pk2)
    tests.delete()
    
    return redirect('tests',pk,pk2)