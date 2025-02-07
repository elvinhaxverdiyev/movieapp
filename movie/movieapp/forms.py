from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}), required=True)
    
    class Meta:
        model = Comment
        fields = ("comment",)
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 4, "placeholder": "Your Comment", "class": "form-control"}),
        }
        labels = {
            "comment": "", 
        }