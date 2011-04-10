import functools

def pjax(pjax_template=None):
    def pjax_decorator(view):
        @functools.wraps(view)
        def _view(request, *args, **kwargs):
            resp = view(request, *args, **kwargs)
            # this is lame. what else though?
            # if not hasattr(resp, "is_rendered"):
            #     warnings.warn("@pjax used with non-template-response view")
            #     return resp
            if request.META.get('HTTP_X_PJAX', False):
                if pjax_template:
                    resp.template_name = pjax_template
                elif "." in resp.template_name:
                    resp.template_name = "%s-pjax.%s" % tuple(resp.template_name.rsplit('.', 1))
                else:
                    resp.template_name += "-pjax"
            return resp
        return _view
    return pjax_decorator