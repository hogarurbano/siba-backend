from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'siba/index.html',
        {
            'title': 'Inicio de página',
            'year': datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'siba/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'siba/about.html',
        {
            'title': _('Acerca de nosotros'),
            'subtitle': _('Expertos en sistemas para la gestión administrativa de condominios'),
            'message': _('Tus aliados informáticos.'),
            'year': datetime.now().year,
        }
    )

def companyinfo(request):
    return HttpResponse('')

