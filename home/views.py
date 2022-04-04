from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .forms import *
from .tasks import update_wiki_views
from .utils import generate_description



# Create your views here.
def home(request):
    wiki_items_query = WikiSearch.objects.all().filter(is_published=True)[:50]
    paginator = Paginator(wiki_items_query, 5)
    page_number = request.GET.get('page')
    wiki_found_items = paginator.get_page(page_number)
    args = {'wiki_found_items':wiki_found_items}
    return render(request, 'home/home.html',args)


def search(request):
    search_key = request.GET['search_key']
    wiki_items_query = WikiSearch.objects.all().filter(is_published=True).filter(
		Q(title__icontains=search_key) | Q(description__icontains=search_key) | Q(unique_id__icontains=search_key) |
        Q(external_link__icontains=search_key)
    )[:10]
    paginator = Paginator(wiki_items_query, 5)
    page_number = request.GET.get('page')
    wiki_found_items = paginator.get_page(page_number)
    args = {'wiki_found_items':wiki_found_items}
    return render(request, 'home/home.html',args)



def new_page(request,unique_id):
    wiki_object = WikiSearch.objects.get(unique_id=unique_id)
    data = {'unique_id':unique_id}
    update_wiki_views.delay(data)
    args = {'wiki_object':wiki_object}
    return render(request, 'home/new_page.html',args)


def fetch_description(request,unique_id):
    wiki_object = WikiSearch.objects.get(unique_id=unique_id)
    if not wiki_object.description:
        description = generate_description()
    else:
        description = wiki_object.description
    args = {'wiki_object':wiki_object,'description':description}
    return render(request, 'home/view_detailed_description.html',args)



@login_required(login_url='/auth/sign-in/')
def edit_wiki_object(request,unique_id):
    instance = WikiSearch.objects.get(unique_id=unique_id)
    if request.method == 'POST':
        form = WikiObjectForm(request.POST,instance=instance)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            messages.success(request, 'Edited Successfully!.')
            return redirect('new_page',unique_id=unique_id)
        else:
            return render(request, 'home/edit_wiki_object.html', {"form": form})
    else:
        form = WikiObjectForm(instance=instance)
        args = {'form': form}
        args.update(csrf(request))
        return render(request, 'home/edit_wiki_object.html', args)