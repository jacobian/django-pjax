# Django bootstrap, sigh.
from django.conf import settings; settings.configure()

import djpjax
from django.template.response import TemplateResponse
from django.test.client import RequestFactory
from django.views.generic import View

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

def test_view_with_template_tuple():
    resp = view_with_template_tuple(regular_request)
    assert resp.template_name == ("template.html", "other_template.html")
    resp = view_with_template_tuple(pjax_request)
    assert resp.template_name == ("template-pjax.html", "other_template-pjax.html")

def test_class_pjax_sans_template():
    view = NoPJAXTemplateVew.as_view()
    resp = view(regular_request)
    assert resp.template_name[0] == "template.html"
    resp = view(pjax_request)
    assert resp.template_name[0] == "template-pjax.html"

def test_class_with_silly_template():
    view = SillyTemplateNameView.as_view()
    resp = view(regular_request)
    assert resp.template_name[0] == "silly"
    resp = view(pjax_request)
    assert resp.template_name[0] == "silly-pjax"

def test_class_with_pjax_template():
    view = PJAXTemplateView.as_view()
    resp = view(regular_request)
    assert resp.template_name[0] == "template.html"
    resp = view(pjax_request)
    assert resp.template_name[0] == "pjax.html"

def test_pjaxtend_default():
    resp = view_default_pjaxtend(regular_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['parent'] == "base.html"
    resp = view_default_pjaxtend(pjax_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['parent'] == "pjax.html"

def test_pjaxtend_default_parent():
    resp = view_default_parent_pjaxtend(regular_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['parent'] == "parent.html"
    resp = view_default_parent_pjaxtend(pjax_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['parent'] == "pjax.html"

def test_pjaxtend_custom_parent():
    resp = view_custom_parent_pjaxtend(regular_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['parent'] == "parent.html"
    resp = view_custom_parent_pjaxtend(pjax_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['parent'] == "parent-pjax.html"

def test_pjaxtend_custom_context():
    resp = view_custom_context_pjaxtend(regular_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['my_parent'] == "parent.html"
    resp = view_custom_context_pjaxtend(pjax_request)
    assert resp.template_name == "template.html"
    assert resp.context_data['my_parent'] == "parent-pjax.html"

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

@djpjax.pjax()
def view_with_template_tuple(request):
    return TemplateResponse(request, ("template.html", "other_template.html"), {})

@djpjax.pjaxtend()
def view_default_pjaxtend(request):
    return TemplateResponse(request, "template.html", {})

@djpjax.pjaxtend('parent.html')
def view_default_parent_pjaxtend(request):
    return TemplateResponse(request, "template.html", {})

@djpjax.pjaxtend('parent.html', 'parent-pjax.html')
def view_custom_parent_pjaxtend(request):
    return TemplateResponse(request, "template.html", {})

@djpjax.pjaxtend('parent.html', 'parent-pjax.html', 'my_parent')
def view_custom_context_pjaxtend(request):
    return TemplateResponse(request, "template.html", {})

class NoPJAXTemplateVew(djpjax.PJAXResponseMixin, View):
    template_name = 'template.html'

    def get(self, request):
        return self.render_to_response({})

class SillyTemplateNameView(djpjax.PJAXResponseMixin, View):
    template_name = 'silly'

    def get(self, request):
        return self.render_to_response({})

class PJAXTemplateView(djpjax.PJAXResponseMixin, View):
    template_name = 'template.html'
    pjax_template_name = 'pjax.html'
    
    def get(self, request):
        return self.render_to_response({})
