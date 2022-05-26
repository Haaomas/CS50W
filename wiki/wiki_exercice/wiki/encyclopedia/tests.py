# from django.test import TestCase
# # Formulaire
# from django import forms
# # Redirection
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect, render
# # Check if file already exist 
# import os.path
# from os import listdir
# from os.path import isfile, join
# # Convert Markdown to HTML 
# from markdown2 import Markdown
# # Alert Message
# import tkinter
# from tkinter import messagebox
from util import *
# import random

# Create your tests here.
# nameArrayFiles = os.listdir(r"C:\Users\barre\OneDrive\Bureau\Dev\Perso\GitHub\Harvard\CS50W\wiki\wikiExercice\entries")
# for i in range(len(nameArrayFiles)):
#     nameArrayFiles[i] = nameArrayFiles[i][:-3]

# randomEntry = "wiki/" + random.choice(nameArrayFiles) 
# print(randomEntry)

# # Random page version 
entries =  list_entries()
print(entries) 