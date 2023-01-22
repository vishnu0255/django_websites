from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.
#class HomeView(TemplateView):
#    template_name = "home.html"

def HomeView(request):
    comnt_cnt = {}
    post_reqs = models.NewPost.objects.filter(post_save=True)

    for i in post_reqs:
        comnt_cnt[i.pk] = models.Comment.objects.filter(post_id=i.pk).count()
    return render(request,'main.html',context={'postslist':post_reqs,'comnt_cnt':comnt_cnt})

class AboutView(TemplateView):
    template_name = "about.html"

def LoginView(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user != None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                message = "login failed"
    return render(request,'login.html',context={'form':form,'message':message})

def NewPostView(request):
    newpostform = forms.NewPostForm()
    newpostform.fields['post_author'].choices = [(request.user,request.user),]
    if request.method == 'POST':
        unit_id = request.POST.get('newposform')
        newpostform = forms.NewPostForm(request.POST)
        newpostform.fields['post_author'].choices = [(request.user,request.user),]
        if newpostform.is_valid():
            newpost = newpostform.save()
            return HttpResponseRedirect(reverse('draftview',args=(newpost.pk,)))
    return render(request,'newpost.html',context={'newpostform':newpostform})

def DraftsView(request,pk):
    post = models.NewPost.objects.filter(pk=pk)
    if request.method == 'POST':
        draft_publish = request.POST['Publish']
        models.NewPost.objects.filter(pk=pk).update(post_save=True)
        return HttpResponseRedirect(reverse('post',args=(pk,)))
    return render(request,'draftview.html',{'draftpost':post})

def PostView(request,pk):
    authentication = False
    post = models.NewPost.objects.filter(pk=pk)
    try:
        comment = models.Comment.objects.filter(post_id=pk)
    except:
        comment = None
    if request.user.is_authenticated:
        authentication = True
    return render(request,'postview.html',context={'postview':post,'authentication':authentication,'comment':comment,'comment_exists':comment.exists()})

def DraftsListView(request):
    drafts = models.NewPost.objects.filter(post_author=request.user,post_save=False)
    return render(request,'drafts.html',context={'draftslist':drafts})

def PostListView(request):
    posts = models.NewPost.objects.get(post_save=True)
    print(posts)
    for post in posts:
        print(posts.pk)
    return render(request,'posts.html',context={'postslist':posts})

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def PostListView(request):
    posts = models.NewPost.objects.filter(post_save=True)
    return render(request,'posts.html',context={'postslist':posts})

def EditPostView(request,pk):
    postinstance = models.NewPost.objects.get(pk=pk)
    editpostform = forms.NewPostForm(instance=postinstance)
    editpostform.fields['post_author'].choices = [(postinstance.post_author,postinstance.post_author),]

    if request.method == 'POST':
        editpostform = forms.NewPostForm(request.POST,instance=postinstance)
        editpostform.fields['post_author'].choices = [(postinstance.post_author,postinstance.post_author),]

        if editpostform.is_valid():
            editpostform.save()

            if postinstance.post_save:
                return HttpResponseRedirect(reverse('post',args=(pk,)))
            else:
                return HttpResponseRedirect(reverse('draftview',args=(pk,)))

    return render(request,'editpost.html',context={'editpostform':editpostform})

def DeletePostView(request,pk):
    post = models.NewPost.objects.filter(pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'deletepost.html',context={'postdelete':post[0]})

def NewCommentView(request,pk):
    post = models.NewPost.objects.get(pk=pk)
    commentform = forms.NewCommentForm()
    if request.method == 'POST':
        commentform = forms.NewCommentForm(request.POST)
        if commentform.is_valid():
            newcomment = commentform.save()
            comment = models.Comment.objects.get(pk=newcomment.pk)
            comment.post_id = pk
            comment.post_title = post.post_title
            comment.save()
            return HttpResponseRedirect(reverse('post',args=(pk,)))
    return render(request,'newcomment.html',context={'commentform':commentform})

def ApproveCommentView(request,pk):
        print(pk)
        commt = models.Comment.objects.get(pk=pk)
        commt.comment_approve = True
        commt.save()
        post_pk = commt.post_id
        return HttpResponseRedirect(reverse('post',args=(post_pk,)))

def DeleteCommentView(request,pk):
    commt = models.Comment.objects.get(pk=pk)
    post_pk = commt.post_id
    commt.delete()
    return HttpResponseRedirect(reverse('post',args=(post_pk,)))
