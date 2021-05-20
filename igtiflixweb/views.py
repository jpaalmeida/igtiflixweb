from django.http import HttpResponseRedirect


def ridirect_root(request):
    return HttpResponseRedirect('/principal/')
