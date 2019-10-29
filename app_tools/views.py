from django.shortcuts import redirect, render_to_response
from django.http import HttpResponseRedirect
from base.helpers import set_cookie


def switch_design(request, design):
    print(design)
    response = HttpResponseRedirect('/')
    set_cookie(response, '__theme', design)
    return response
    return redirect('/')

