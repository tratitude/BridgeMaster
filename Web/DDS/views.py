from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.sessions.models import Session
from django.views import View
from Member.models import rounds,table
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.http import HttpResponse
from django.db.models	 import Q
from .ddsTable import ddsTable

# Create your views here.
def dds(request):
    ddsTable.ddsTable("Web/DDS/ddsTable/ddsDB.txt", "Web/DDS/ddsTable/ddsResult.txt")
    render(request, "DDS/dds.html", locals())