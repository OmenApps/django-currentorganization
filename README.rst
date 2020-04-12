=============================
django-currentorganization
=============================

----

.. contents:: Conveniently store reference to request organization on thread/db level.

----

Quickstart
----------

Install django-currentorganization::

    pip install django-currentorganization

Add it to the middleware classes in your settings.py::

    MIDDLEWARE = (
        ...,
        'django_currentorganization.middleware.ThreadLocalOrganizationMiddleware',
    )

Then use it in a project::

    from django_currentorganization.middleware import (
        get_current_organization, get_current_authenticated_organization)

    # As model field:
    from django_currentorganization.db.models import CurrentOrganizationField
    class Foo(models.Model):
        created_by = CurrentOrganizationField()
