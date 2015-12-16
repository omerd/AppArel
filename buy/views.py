from django.shortcuts import redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import Template, RequestContext
import datetime
from .models import *


def index(request):
    raise Http404("Page not found you idiot!")
	
@csrf_protect
def logged(request):
	if not request.user.is_authenticated():
		raise PermissionDenied
	# This bit of code adds the CSRF bits to your request.
	
	c = RequestContext(request,{'result':'Good'})
	t = Template("{{result}}") # A dummy template
	response = HttpResponse(t.render(c))
	return response
	#return HttpResponse('You are logged - %s !' % request.user)

@csrf_exempt #TODO: fix. http://stackoverflow.com/questions/6412813/do-login-forms-need-tokens-against-csrf-attacks
def login_handler(request):
	if not request.method == "POST":
		return HttpResponse("POST, not GET!", status = 400)
	form = AuthenticationForm(request, data=request.POST)
	if not form.is_valid():
		return HttpResponse("Invalid login", status = 400)
	login(request, form.get_user())
	return redirect('logged_view')

#thread safety
def reg(request):
	if not request.method == "POST":
		return HttpResponse("POST, not GET!", status = 400)
	form = UserCreationForm(request, data=request.POST)
	if not form.is_valid():
		return HttpResponse("Invalid registration", status = 400)
	if request.user.is_authenticated():
		logout(request)
	user = User.objects.create_user(form.username, '', form.password)
	user.save()
	login(request, form.get_user())
	return redirect('logged_view')

#TODO: it should be nicer if the users won't be able to know about the ID things. just send an encrypted buffer of the ID so no one can manipulate it.
def getProductDetails(request, id):
	pid_integer = int(id)
	if not Product.objects.filter(pid = pid_integer).exists():
		return HttpResponse("ID does not exist", status = 200)
	prod =  Product.objects.get(pid = pid_integer)
	return HttpResponse(id + ";" + str(prod.catalog.price) + ";" + prod.catalog.name, status = 200)
	
#thread safety, check input, try except
@csrf_protect
def pay(request):
	if not request.user.is_authenticated():
		raise PermissionDenied
	if not request.method == "POST":
		return HttpResponse("POST, not GET!", status = 400)
	try:
		products = request.POST['products']
	except KeyError:
		return HttpResponse("Invalid payment", status = 400)
	products = products.split(',')
	for prod_id in products:
		if (BuyHistory.objects.filter(product = int(prod_id)).count() != 0):
			return HttpResponse("Already Paid", status = 200)
	for prod_id in products:
		p  = Product.objects.get(pid = int(prod_id))
		buy = BuyHistory(customer = request.user, product =p)
		buy.save()
	#charge customer account <-----------
	return redirect('logged_view')