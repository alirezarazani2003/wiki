from django.shortcuts import render , redirect
from . import models
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def detail(request, name):
    parametr = util.get_entry(name)
    context = {
        "parametr": parametr
    }
    return render(request, "encyclopedia/detail.html", context)


# def change(name):
#     if util.get_entry(name):
#         return  markdown.markdown(util.get_entry(name))
#     else : 
#         name = 'Error'
#         return markdown.markdown(util.get_entry(name))
    
def edit(request,name):
    if request.method == 'POST':
        textarea = request.POST["textarea"]
        util.save_entry(name , textarea)
        return redirect("detail",args=(name))

