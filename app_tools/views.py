from django.shortcuts import redirect


def switch_design(request, design):
    print(design)
    return redirect('/')
