from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import models, transaction
from django.db.models import F

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View, DetailView

from .forms import RSVPForm
from myupdates.forms import RSVPForm
from myupdates.models import Feed, RSVP

def updates_index(request):
    feeds  = Feed.objects.all()
    context = {"feeds": feeds}
    return render(request, "updates_feed.html", context)

def updates_feed(request, pk):
    feed = Feed.objects.get(pk=pk)
    form = RSVPForm()

    if request.method == "POST":
        form = RSVPForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                feed = Feed.objects.get(pk=pk)
                rsvp = RSVP(
                        sender = form.data.get('sender'),
                        email  = form.data.get('email'),
                        phone  = form.data.get('phone'),
                        )
                rsvp.save()

                feed.call += 1
                feed.save()
                messages.success(request, '신청되었습니다. 세부 일정은 개별 연락드리겠습니다.')
    context = {"feed":feed, "form": form}
    return render(request, "feed_detail.html", context)

# Create your views here.

# Create your views here.
