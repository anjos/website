from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

import settings
from stuff.publications.models import Publication

import time

def index(request):
    """Gives an overview of all articles available."""
    #get all, latest first
    pubs = Publication.objects.all().order_by('-date')
    return render_to_response('publications/index.html',
                              {'publications': pubs,
                               'create_time': time.asctime() })

def get(request, pub_id):
    """Give an overview of the article asked."""

    try:
        pub = Publication.objects.filter(id=pub_id)
    except Publication.DoesNotExist:
        raise Http404
    
    return render_to_response('publications/get.html',
                              {'publication': pub[0],
                               'files': pub[0].files.all(),
                               'MEDIA_URL': settings.MEDIA_URL,
                               'create_time': time.asctime() })
    
