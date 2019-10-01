from django.forms import ModelForm

from quotes.models import Quote


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        exclude = ['published', 'poc', 'user', 'nwa', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nam, field in self.fields.items():
            field.disabled = True
