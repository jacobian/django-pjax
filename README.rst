Django-PJAX
===========

This is a Django helper for `defunkt's jquery-pjax`__. 

Django-PJAX requires Django 1.3.

What's PJAX?
------------

__ https://github.com/defunkt/jquery-pjax

PJAX is essentially AHAH__ ("Asynchronous HTML and HTTP"), except with real
permalinks and a working back button. It lets you load just a portion of a
page (so things are faster) while still maintaining the usability of real
links.

__ http://www.xfront.com/microformats/AHAH.html

A demo makes more sense, so `check out the one defunkt put together`__

__ http://pjax.heroku.com/

Usage
-----

First, read about `how to use jQuery-PJAX`__ and pick one of the techniques there.

__ https://github.com/defunkt/jquery-pjax/blob/master/README

Next, make sure the views you're PJAXing are using TemplateResponse__. You can't use Django-PJAX with a normal ``HttpResponse``; only ``TemplateResponse``. Decorate these views with the ``pjax`` decorator::

    from djpjax import pjax
    
    @pjax()
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

__ http://django.me/TemplateResponse

After doing this, if the request is made via jQuery-PJAX, the ``@pjax()``
decorator will automatically swap out ``template.html`` for
``template-pjax.html``. 

More formally: if the request is a PJAX request, the template used in your
``TemplateResponse`` will be replaced with one with ``-pjax`` before the file
extension. So ``template.html`` becomes ``template-pjax.html``,
``my.template.xml`` becomes ``my.template-pjax.xml``, etc. If there's no file
extension, the template name will just be suffixed with ``-pjax``.

You can also manually pick a PJAX template by passing it as an argument to
the decorator::

    from djpjax import pjax
    
    @pjax("pjax.html")
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

That's it!