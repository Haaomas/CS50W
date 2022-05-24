from django.shortcuts import render

from . import util

# List all of the index on a page the page index.html
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Make a dynamique URL for the home list
def entries_url(request, title):
    return render(request, "encyclopedia/entries.html", {
        "title": title.capitalize()
    })
    
# def entries_content(request, title):
#     # "content": get_entry(title)
#     return render(request, "encyclopedia/entries.html", {
#     })