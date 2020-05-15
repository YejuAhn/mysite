from django import forms

from .models import Article
import datetime


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label = '', widget = forms.TextInput(attrs = {"placeholder" : "Title of article"}))
    url = forms.URLField()
    description = forms.CharField(required= True, widget = forms.Textarea(
        attrs = {
            "placeholder": "Article Brief Description",
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows":20,
            "cols": 50,
        }
    ))
    author = forms.CharField(label = '', widget = forms.TextInput(attrs = {"placeholder" : "Name of author"}))
    text = forms.CharField(required= True, widget = forms.Textarea(
        attrs = {
            "placeholder": "Article Text Description",
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows": 20,
            "cols": 100,
        }
    ))
    pub_date = forms.DateField()
    class Meta:
        model = Article
        fields = [
            'title',
            'url',
            'description',
            'author',
            'text',
            'pub_date',
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        #get only recent article
        if not "2020" in title:
            raise forms.ValidationError("This is not a recent article")
        return title

    def clean_url(self, *args, **kwargs):
        cur_url = self.cleaned_data.get('url')
        if "https:" not in cur_url:
            raise forms.ValidationError("This is not a valid url")


    def clean_pub_date(self, *args, **kwargs):
        date = self.cleaned_data.get("date")
        print(date)
        return date










