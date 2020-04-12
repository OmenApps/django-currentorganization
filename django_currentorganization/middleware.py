from django.conf import settings
from threading import local
from watervize.organizations.models.models import Organization

ORGANIZATION_ATTR_NAME = getattr(settings, 'LOCAL_ORGANIZATION_ATTR_NAME', '_current_organization')

_thread_locals = local()


def _do_set_current_organization(organization_fun):
    setattr(_thread_locals, ORGANIZATION_ATTR_NAME, organization_fun.__get__(organization_fun, local))


def _set_current_organization(organization=None):
    '''
    Sets current organization in local thread.

    Can be used as a hook e.g. for shell jobs (when request object is not
    available).
    '''
    _do_set_current_organization(lambda self: organization)


class ThreadLocalOrganizationMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.organization_context closure; asserts laziness;
        # memorization is implemented in
        # request.organization_context (non-data descriptor)
        _do_set_current_organization(lambda self: getattr(request, 'organization_context', None))
        response = self.get_response(request)
        return response


def get_current_organization():
    current_organization = getattr(_thread_locals, ORGANIZATION_ATTR_NAME, None)
    if callable(current_organization):
        return current_organization()
    return current_organization


def get_current_verified_organization():
    current_organization = get_current_organization()
    if current_organization is None:
        return None
    if isinstance(current_organization, Organization):
        return current_organization
    return None
