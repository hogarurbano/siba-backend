from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'appweb/index.html',
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
        'appweb/contact.html',
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
        'appweb/about.html',
        {
            'title': _('Acerca de nosotros'),
            'subtitle': _('Expertos en sistemas para la gestión administrativa de condominios'),
            'message': _('Tus aliados informáticos.'),
            'year': datetime.now().year,
        }
    )

def companyinfo(request):
    return HttpResponse('')

