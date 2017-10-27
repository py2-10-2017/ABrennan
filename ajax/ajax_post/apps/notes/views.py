from django.shortcuts import render, HttpResponse, redirect
from models import *


# Home
def index(request):
    print Note.objects.all()
    context = {
        "notes": Note.objects.all()
    }
    return render(request, 'notes/index.html', context)

# Partial - note new
def note_new(request):
    n = Note.objects.create(note=request.POST['note'],title=request.POST['title'])
    context = {
        "note": n
    }
    return render(request, 'notes/notes.html', context)

# Partial - note edit
def note_edit(request, note_id):
    print request.POST
    n = Note.objects.get(id=note_id)
    n.note = request.POST['note']
    n.save()
    return redirect('/notes')

# Partial - note delete
def note_delete(request, note_id):
    n = Note.objects.get(id=note_id)
    n.delete()
    return redirect('/notes')
