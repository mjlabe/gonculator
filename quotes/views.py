from datatableview import Datatable, helpers, columns
from datatableview.views import DatatableView

from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from quotes.models import Quote, Armory
from quotes.forms import QuoteForm


def index(request):
    return render(request, 'index.html')


def quote(request, q):
    quote_obj = get_object_or_404(Quote, quote_number=q)
    armorys = Armory.objects.filter(quote=quote_obj)
    return render(request, 'quote.html', {'quote': quote_obj, 'armorys': armorys})


class QuoteDatatable(Datatable):
    qt = columns.TextColumn("Quote", sources=None, processor='get_quote_link')

    class Meta:
        model = Quote
        ordering = ['-modified']
        columns = ['qt', 'project', 'modified']
        search_fields = ['quote_number', 'project']
        processors = {
            'modified': helpers.format_date('%Y-%m-%d at %H:%M')
        }
        # unsortable_columns = ['n_comments']
        # hidden_columns = ['n_pingbacks']
        # structure_template = 'datatableview/default_structure.html'

    def get_quote_link(self, instance, *args, **kwargs):
        quote_url = reverse('quote', args=(instance.quote_number, ))
        return "<a href={url}>{qn}</a>".format(url=quote_url, qn=instance.quote_number)


class QuotesDatatableView(DatatableView):
    model = Quote
    datatable_class = QuoteDatatable

    def get_queryset(self):
        qs = Quote.objects.filter(user__exact=self.request.user, published=True)
        return qs

    # def get_quote_link(self, instance, *args, **kwargs):
    #     return "<a href={% url 'quote' p={qn} %}>{qn]</a>".format(qn=instance.qoute_number)
