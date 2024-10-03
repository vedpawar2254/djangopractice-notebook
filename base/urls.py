from django.urls import path,include
from . import views
from .views import Notes_Feed


urlpatterns = [
    path('', views.home, name='home'),
    path('Post-form/', views.form, name="form"),
    path('Post-delete/<str:pk>/', views.deletePost, name="delete"),
    path('Post-update/<str:pk>/', views.updatePost, name="update"),
    path('', views.Post_search, name='post_search'),
    path('Post-reply/<str:pk>/', views.replyForm, name="reply"),

    path('Notes/<str:pk>', Notes_Feed, name='notes'),
    path('Notes/', views.Notes_Search, name='notes_search'),
    path('Notes/<str:pk>/Notes-form/', views.Notesform, name='Notes_form'),
    path('Notes-delete/<str:pk>/', views.DeleteNotes, name="delete_notes"),
    path('Notes-update/<str:pk>/', views.UpdateNotes, name="update_notes"),


    path('register/' ,views.registerPage, name="register"),
    path('login/' ,views.loginPage, name="login"),
    path('logout/' ,views.logoutPage, name="logout"),

    path('like/', views.like_post, name="like-post"),
    path('dislike/', views.dislike_post, name="dislike-post"),
    path('complete/<str:pk>', views.completed, name="complete-post"),

    path('Notes/<str:pk>/link-form/', views.Linkform, name='Link_form'),
    path('Notes/<str:pk>/questions-form/', views.Questions_Form, name='questions_form'),

    path('profile/<str:pk>', views.Profile, name="profile"),


    path('Notes/enroll/<str:pk>', views.Enroll, name="enroll"),

    path('Notes/<str:pk2>/add_comment/<str:pk>', views.AddMessage, name="add_comment"),
    path('Notes/<str:pk>/delete_comment/<str:pk2>', views.DeleteMessage, name="delete_comment"),
    path('Notes/<str:pk>/<str:pk3>/update_comment/<str:pk2>', views.UpdateMessage, name="update_message"),


    path('Notes/<str:pk2>/add_testcomment/<str:pk>/<str:pk3>/', views.AddTestMessage, name="add_testcomment"),
    


    path('post/notcompletedyetby/<str:pk>',views.Acountability, name='acountability'),
    path('post/discussion-forum/<str:pk>',views.Discussion, name='discussion'),
    
    path('post/<str:pk>/test-form/<str:pk2>/',views.Test_Form, name='test_form'),
    path('post/<str:pk2>/tests/<str:pk>/',views.Tests, name='tests'),
    path('post/<str:pk2>/delete_test/<str:pk>/',views.DeleteTests, name='delete_test'),

]


