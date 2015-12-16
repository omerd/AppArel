from django.shortcuts import redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
import datetime
from buy.models import *


def index(request):
    raise Http404("Page not found you idiot!")
	
#thread safety
def check(request, id):
	#if not request.user.is_authenticated():
	#	raise PermissionDenied
	pid_integer = int(id)
	if not Product.objects.filter(pid = pid_integer).exists():
		return HttpResponse("ID does not exist", status = 200)
	if (BuyHistory.objects.filter(product =pid_integer).count() == 0):
		return HttpResponse("BAD", status = 200)
	return HttpResponse("OK", status = 200)