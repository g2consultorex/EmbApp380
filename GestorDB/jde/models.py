# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class F0101(models.Model):


	clave = models.IntegerField(db_column='ABAN8', primary_key=True)
	nombre = models.CharField(db_column='ABALPH', max_length='ABALPH')

	class Meta:
		managed = False
		db_table = u'"CRPDTA"."F0101"'

	