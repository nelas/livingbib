# -*- coding: utf-8 -*-

from django.db.models import signals
from django.template.defaultfilters import slugify
from datetime import datetime

def slug_pre_save(signal, instance, sender, **kwargs):
    '''Create slug before saving.'''
    slug = slugify(instance.name)
    instance.slug = slug

def slug_username(signal, instance, sender, **kwargs):
    '''Create slug before saving.'''
    slug = slugify(instance.user.username)
    instance.slug = slug

def update_delta(signal, instance, sender, **kwargs):
    '''Update variation of total results for taxon query.'''
    try:
        delta = instance.total_results - instance.taxon.total_results
        instance.delta = delta
        # Calculate delta per day ratio.
        today = datetime.now()
        timedelta = today - instance.taxon.timestamp
        instance.factor = delta / float(timedelta.days)
        #XXX Should worry about division by -1 or 0?
    except:
        instance.delta = 0
        instance.factor = float(0)

def update_results(signal, instance, sender, **kwargs):
    '''Update total number of results for taxon query.'''
    instance.taxon.total_results = instance.total_results
    instance.taxon.delta = instance.delta
    instance.taxon.factor = instance.factor
    instance.taxon.save()

