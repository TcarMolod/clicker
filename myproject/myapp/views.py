from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Fruits, Note
from .forms import NoteForm

def test(request):
    return HttpResponse('test page')

def Katia(request):
    return render(request, 'katia.html')

"""def index(request):
    notes = [f'{note.title} {note.text} {note.price}; ' for note in Fruits.objects.all()]
    return HttpResponse(notes)"""

"""def index(request):
    notes_list = Note.objects.all()
    return render(request, 'index.html', {'notes': notes_list})"""

def index(request):
    return render(request, 'add_note.html')

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})
    