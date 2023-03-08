from calendar import timegm
from tkinter.font import nametofont
from django.shortcuts import render,redirect
from . import util
import markdown
from .forms import addform
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import random

def change(name):
    if util.get_entry(name):
        return  markdown.markdown(util.get_entry(name))
    else : 
        name = 'Error'
        return markdown.markdown(util.get_entry(name))

def index(request):
    entrys = util.list_entries()
    if request.method == "POST":
        cd = request.POST['q']
        entrys = filter(lambda x : x.upper().find(cd.upper())!=-1 ,entrys)
    return render(request, "encyclopedia/index.html", {
        "entries": entrys, 
    })
    

def MtoH(request, name):
    entrys = util.list_entries()
    context={
        "html":change(name),  "name":name, "entries":entrys
    }
    return render(request, "encyclopedia/details.html",context)

def New(request):
    if request.method == "POST":
        form = addform(request.POST)
        if form.is_valid():
            titles = form.cleaned_data["title"]
            contents = form.cleaned_data["content"]
            if util.get_entry(titles):
                return render(request, "encyclopedia/new.html",{
                    "new": form,
                    "Error": "* This page is already exist",
                })
            util.save_entry(titles, contents)
            messages.success(request, 'New page Added Successfully')
            return HttpResponseRedirect(reverse("encl:mtoh", args=(titles,)))
    return render(request, "encyclopedia/new.html",{
        "new": addform()
    })

def edite(request,name):
    if request.method == "POST":
        textarea = request.POST['textarea']
        util.save_entry(name, textarea)
        messages.success(request, 'Changes Saved!')
        return HttpResponseRedirect(reverse("encl:mtoh", args=(name,)))
    
    context={
        "head": name,
        "body": util.get_entry(name),
    }
    return render(request, "encyclopedia/edite.html",context)

def delete (request, name):
    util.delete_entry(name)
    messages.success(request, 'Content Deleted!')
    return redirect("encl:index")
    

def random1(request):
    entries = util.list_entries()
    name = random.choice(entries)
    return HttpResponseRedirect(reverse("encl:mtoh", args=(name,)))