from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from base.helpers import set_cookie


def switch_design(request, design):
    response = HttpResponseRedirect('/')
    set_cookie(response, '__theme', design)
    return redirect('/')
