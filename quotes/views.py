from datatableview.views import DatatableView
from django.db.models import Q
from django.shortcuts import render

from quotes.models import Quote


def index(request):
    return render(request, 'index.html')


def quotes(request):
    return render(request, 'quotes.html')


class QuotesDatatableView(DatatableView):

    class Meta:
        model = Quote
        columns = ['quote_number', 'project', 'modified']

    def get_queryset(self):
        return Quote.objects.only('quote_number', 'project', 'modified')
