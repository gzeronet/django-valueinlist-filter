django-valueinlist-filter
=========================

Queryset can be filtered by a given list on the django admin page, just like: qs.filter(field__in=[list]).

Installation
------------

.. code-block:: bash

    cd django-valueinlist-filter
    python setup.py install


Add valueinlist_filter to settings.INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'valueinlist_filter'
    )

And then, set a CharField field in a model like this:

.. code-block:: python

    class Model(models.Model):
        ...
        serial_number = models.CharField(max_length=32)


If you want to filter the **serial_number** field by a given value list(split string by space), you can bind ValueInListFilter to this field:

.. code-block:: python

    from valueinlist_filter.filter import ValueInListFilter
    from django.contrib import admin
    from models import Model

    class ModelAdmin(admin.ModelAdmin):
        list_filter = (
            ('serial_number', ValueInListFilter), # bind filter to CharField
            ...
        )

Finally, you will get a textarea form on the filter side bar, the textarea's change event will trigger form.
