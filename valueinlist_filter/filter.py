from django.contrib import admin
from django.db import models
from .forms import ValueInListForm


class ValueInListFilter(admin.filters.FieldListFilter):
    template = 'valueinlist_filter/filter.html'

    def choices(self, cl):
        return []

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.field = field
        self.field_path = field_path
        self.title = getattr(field, 'verbose_name', field_path)
        self.lookup_kwarg_in = '%s__in' % field_path
        self.used_parameters = dict((key, params.pop(key)) for key in self.expected_parameters() if key in params)
        self.form = self.get_form(request)

    def expected_parameters(self):
        return [self.lookup_kwarg_in]

    def get_form(self, request):
        return ValueInListForm(data=self.used_parameters, field_name=self.field_path)

    def queryset(self, request, queryset):
        if self.form.is_valid():
            data = self.form.cleaned_data
            return queryset.filter(**dict((key, data[key].split()) for key in data if data[key]))
        return queryset

admin.filters.FieldListFilter.register(lambda f: isinstance(f, models.CharField), ValueInListFilter)
