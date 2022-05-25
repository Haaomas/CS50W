from markdown2 import Markdown
from django.shortcuts import render

from . import util

# List all of the index on a page the page index.html
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Make a dynamique URL for the home list
def entries_url(request, title):
    # Function to convert Markdown to HTML 
    markdown = Markdown()
    
    # Get the content of the page(title)
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/404.html", {
            "title": title
        })
    else:
    # Return the page with the good content 
        return render(request, "encyclopedia/entries.html", {
            "entryContent": markdown.convert(content),
            "title": title
        })