# Django bootstrap, sigh.
from django.conf import settings; settings.configure()

import mock
import djpjax
from django.template.response import TemplateResponse
from django.test.client import RequestFactory

# A couple of request objects - one PJAX, one not.
rf = RequestFactory()
regular_request = rf.get('/')
pjax_request = rf.get('/', HTTP_X_PJAX=True)

# Tests.

def test_pjax_sans_template():
    resp = view_sans_pjax_template(regular_request)
    assert resp.template_name == "template.html"
    resp = view_sans_pjax_template(pjax_request)
    assert resp.template_name == "template-pjax.html"

def test_view_with_silly_template():
    resp = view_with_silly_template(regular_request)
    assert resp.template_name == "silly"
    resp = view_with_silly_template(pjax_request)
    assert resp.template_name == "silly-pjax"

def test_view_with_pjax_template():
    resp = view_with_pjax_template(regular_request)
    assert resp.template_name == "template.html"
    resp = view_with_pjax_template(pjax_request)
    assert resp.template_name == "pjax.html"

# The test "views" themselves.

@djpjax.pjax()
def view_sans_pjax_template(request):
    return TemplateResponse(request, "template.html", {})
    
@djpjax.pjax()
def view_with_silly_template(request):
    return TemplateResponse(request, "silly", {})
    
@djpjax.pjax("pjax.html")
def view_with_pjax_template(request):
    return TemplateResponse(request, "template.html", {})

