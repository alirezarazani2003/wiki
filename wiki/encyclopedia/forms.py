from django import forms

class searchform(forms.Form):
    search = forms.CharField(label="")

class addform(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(widget = forms.Textarea)

class editeform(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(widget = forms.Textarea)