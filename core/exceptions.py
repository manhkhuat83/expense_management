from rest_framework.response import Response
from rest_framework.views import exception_handler


def core_exception_handler(exc, context):
    response = exception_handler(exc, context)
    handlers = {
        "NotFound": _handle_not_found_error,
        "ValidationError": _handle_generic_error,
    }
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_generic_error(exc, context, response):
    if response:
        if response.status_code == 404:
            response.data = {"detail": "Endpoint not found"}
        else:
            response.data = {"errors": response.data}
    else:
        response = Response({"detail": "Server internal error"}, status=500)
    return response


def _handle_not_found_error(exc, context, response):
    view = context.get("view", None)
    if view and hasattr(view, "queryset") and view.queryset is not None:
        error_key = view.queryset.model._meta.verbose_name
        response.data = {"errors": {error_key: response.data["detail"]}}
    else:
        response = _handle_generic_error(exc, context, response)
    return
