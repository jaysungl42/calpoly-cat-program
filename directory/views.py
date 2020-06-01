from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.db.models import OuterRef, Subquery
import datetime

from .forms import IntakeForm
from .forms import DocumentForm 
from .models import Cat
from .models import Document 
from .models import Photo
from .models import Event

def index(request):
    cats = Cat.objects.all()

    current_time = datetime.datetime.now()
    start_date = current_time - datetime.timedelta(hours=12)
    end_date = current_time + datetime.timedelta(days=5)
    names = Cat.objects.filter(id=OuterRef('cat_id'))
    events = Event.objects.filter(datetime__range=(start_date, end_date)).annotate(name=Subquery(names.values('name')))

    return render(request, 'landing.html', {'cats': cats, 'events': events})

def cat_profile(request):
    cat_id = request.GET.get('id')
    cat = Cat.objects.get(id=cat_id)
    if request.GET.get('action') == "edit":
        return render(request, 'edit_profile.html', {'cat': cat})
    document_form = DocumentForm()
    documents = Document.objects.filter(cat_id=cat_id)
    photos = Photo.objects.filter(cat_id=cat_id)
    return render(request, 'cat_profile.html', {'cat': cat, 'document_form': document_form, 'documents': documents, 'photos': photos})

def help(request):
    return render(request, 'help.html')

def intake_form(request):
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cat = Cat(
                    name = data.get('name'),
                    gender = data.get('gender'),
                    age = data.get('age'),
                    description = data.get('description'),
                    breed = data.get('breed'),
                    itype = data.get('itype'),
                    status = data.get('status'),
                    arrival_date = data.get('arrival_date'),
                    arrival_details = data.get('arrival_details'),
                    medical_history = data.get('medical_history'),
                    vaccinations = data.get('vaccinations'),
                    is_microchipped = data.get('is_microchipped'),
                    flea_control_date = data.get('flea_control_date'),
                    deworming_date = data.get('deworming_date'),
                    fiv_felv_date = data.get('fiv_felv_date'),
                    special_needs = data.get('special_needs'),
                    personality = data.get('personality'),
                    more_personality = data.get('more_personality'),
                    comments = data.get('comments'),
                    personal_exp = data.get('personal_exp'))

            cat.save()
            return HttpResponseRedirect('/cat/?id=' + str(cat.id))
    else:
        form = IntakeForm()
    return render(request, 'intake.html', {'form': form})

def update_cat(request):
    if request.method == 'POST':
        cat_id = request.POST.get('id')
        form = IntakeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cat = Cat(
                    id = cat_id, # should UPDATE with specified key
                    name = data.get('name'),
                    gender = data.get('gender'),
                    age = data.get('age'),
                    description = data.get('description'),
                    breed = data.get('breed'),
                    itype = data.get('itype'),
                    status = data.get('status'),
                    arrival_date = data.get('arrival_date'),
                    arrival_details = data.get('arrival_details'),
                    medical_history = data.get('medical_history'),
                    vaccinations = data.get('vaccinations'),
                    is_microchipped = data.get('is_microchipped'),
                    flea_control_date = data.get('flea_control_date'),
                    deworming_date = data.get('deworming_date'),
                    fiv_felv_date = data.get('fiv_felv_date'),
                    special_needs = data.get('special_needs'),
                    personality = data.get('personality'),
                    more_personality = data.get('more_personality'),
                    comments = data.get('comments'),
                    personal_exp = data.get('personal_exp'))

            cat.save()
            return HttpResponseRedirect('/cat/?id=' + str(cat.id))
    else:
        return redirect('/')

def document_upload(request):
    cat_id = request.POST.get('cat')
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            document = Document(
                    cat_id = cat_id,
                    document = data.get('document'),
                    name = request.FILES['document'].name,
                    description = data.get('description')
            )

            document.save()
    return redirect('/cat/?id=' + str(cat_id))

def photo_upload(request):
    cat_id = request.POST.get('cat')
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            photo = Photo(
                    cat_id = cat_id,
                    photo = data.get('photo'),
                    name = request.FILES['photo'].name,
            )

            photo.save()
    return redirect('/cat/?id=' + str(cat_id))

# TODO add confirmation before delete
# TODO delete the actual file from the system
def delete_document(request):
    doc_id = request.GET.get('id')
    doc = Document.objects.get(id=doc_id)
    cat_id = doc.cat_id
    doc.delete()
    return redirect('/cat/?id=' + str(cat_id))
    
