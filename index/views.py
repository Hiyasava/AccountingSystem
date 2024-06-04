from django.shortcuts import render, HttpResponseRedirect

def index_(request):
    return HttpResponseRedirect('/main')
