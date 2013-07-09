from django import forms
from django.utils.translation import ugettext as _


class ValueInListForm(forms.Form):

    def __init__(self, *args, **kwargs):
        field_name = kwargs.pop('field_name')
        super(ValueInListForm, self).__init__(*args, **kwargs)
        self.fields['%s__in' % field_name] = forms.CharField(label=_('in'), required=False,
                widget=forms.Textarea(attrs={
                    'placeholder': _('%(fn)sA %(fn)sB ... %(fn)sN') % {'fn': field_name}
                    }))
