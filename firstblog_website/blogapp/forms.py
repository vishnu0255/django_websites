from django import forms
from .models import NewPost,Comment

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 32)
    password = forms.CharField(max_length = 32,widget = forms.PasswordInput)

#class NewPostForm(forms.Form):
#    user = ''
    #def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop('user')
        #super(NewPostForm, self).__init__(*args, **kwargs)
        #user = self.user

#    author = forms.ChoiceField(label="Author:")
#    title = forms.CharField(max_length = 32,label="Title:")
#    text = forms.CharField(max_length = 200,label="Text:",widget=forms.Textarea)
class NewPostForm(forms.ModelForm):
    post_author = forms.ChoiceField(label='Author:')
    class Meta:
        model = NewPost
        exclude = ('post_save','post_time',)
        widgets = {
        'post_text':forms.Textarea(attrs={'cols':60,'rows':1}),
        }
        labels = {
        'post_title':'Title',
        'post_text':'Text',
        }

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('comment_approve','post_id','post_title','comment_time')
        widgets = {
        'post_comments':forms.Textarea(attrs={'cols':60,'rows':1}),
        }
        labels = {
        'post_comment_author':'Author',
        'post_comments':'Text',
        }
