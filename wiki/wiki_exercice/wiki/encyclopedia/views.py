# Formulaire
from django import forms
# Redirection
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
# Check if file already exist 
import os.path
from os import listdir
from os.path import isfile, join
# Convert Markdown to HTML 
from markdown2 import Markdown
# Alert Message
import tkinter
from tkinter import messagebox
# Random
import random
from . import util


# List all of the index on a page the page index.html
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "randomEntries": randomEntry()
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
        
# Create a dynamique Form
class NewEntryForm(forms.Form):
    entryTitle = forms.CharField(label="Title", required=True)
    entryContent = forms.CharField(widget=forms.Textarea, label="Content", required=True)
    
    
def add_entry(request):
    # if the form is submit
    if request.method == "POST":
        # Save all the data of the form in the variable form 
        form = NewEntryForm(request.POST)
        # if all the field are valid in te client side 
        if form.is_valid():
            # Get the data of the form
            entryTitle = form.cleaned_data["entryTitle"]
            entryContent = form.cleaned_data["entryContent"]
            # Check if the file already exist
            if os.path.exists(f'./entries/{entryTitle}.md'):
                messagebox.showinfo("Alert", "The entry already exist.")
            else:
                # Create the file 
                with open(f'./entries/{entryTitle}.md', 'w') as newEntry:
                    # Write the information of the entry
                    newEntry.write(f'{entryContent}')
                # Send the user back t the entry 
                return redirect(f'/wiki/{entryTitle.capitalize()}')
        else:
            # if not valid render the same page with their form
            return render(request, "encyclopedia/add.html", {
                "form": form
            })
            
    return render(request, "encyclopedia/add.html", {
        "form": NewEntryForm()
})
    
    
def randomEntry():
    nameArrayFiles = os.listdir(r"C:\Users\barre\OneDrive\Bureau\Dev\Perso\GitHub\Harvard\CS50W\wiki\wikiExercice\entries")

    for i in range(len(nameArrayFiles)):
        nameArrayFiles[i] = nameArrayFiles[i][:-3]
    
    randomEntry = "wiki/" + random.choice(nameArrayFiles) 
    
    return randomEntry

