from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from account import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from models import UserProfile

# Create your views here.
def login(request):
    context = RequestContext(request)
    dictonary = {}
    view = 'Account/login.html'
    if request.method == 'GET':
        return render_to_response(view, dictonary, context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request,user)
            return redirect('/programs/')
        else :
            #return HttpResponse("brukernavn eller passord er feil <a href='/account/login/'> tilbake </a>")
            dictonary["error"] = 'brukernavn eller passord er feil'
            return render_to_response(view, dictonary, context)


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('Account/login.html', context_dict, context)

def create_user(request):
    context = RequestContext(request)
    view = 'Account/create_user.html'
    dictonary = {'errors' : []}
    user_form = forms.UserForm()

    if request.method == 'GET':
        dictonary['user_form'] = user_form

        return render_to_response(view, dictonary, context)
    elif request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        dictonary['user_form'] = user_form
        if user_form.is_valid():
            if request.POST['confirm'] != request.POST['password']:
                dictonary['errors'] = ["ikke samsvar mellom passord og bekreft passord"]
                return render_to_response(view, dictonary,context )
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = UserProfile()
            profile.user = user
            profile.save()
            return redirect('/account/login/')
        else:
            return render_to_response(view, {'user_form' : user_form}, context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/account/login')