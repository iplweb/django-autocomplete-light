from dal import autocomplete

from django.contrib.auth.models import Group

from .models import TModel


class TForm(autocomplete.FutureModelForm):
    test = autocomplete.GenericM2MQuerySetSequenceField(
        queryset=autocomplete.QuerySetSequence(
            Group.objects.all(),
            TModel.objects.all(),
        ),
        required=False,
        widget=autocomplete.QuerySetSequenceSelect2Multiple(
            'select2_generic_m2m'),
    )

    class Meta:
        model = TModel
        fields = ('name',)
