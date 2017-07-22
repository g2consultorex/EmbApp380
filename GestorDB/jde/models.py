# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class F0101(models.Model):

    ABAN8 = models.IntegerField(primary_key=True)
    ABALPH= models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = u'"CRPDTA"."F0101"'

    # def __str__(self):
    #     return self.clave

    def __unicode__(self):
        return str(self.ABAN8)



class F41001(models.Model):
	CIPRIM = models.CharField(max_length=1)
	CISYM1 = models.CharField(max_length=1)
	CISYM2 = models.CharField(max_length=1)
	CISYM3 = models.CharField(max_length=1)
	CISYM5 = models.CharField(max_length=1)
	CISECD = models.CharField(max_length=1)
	CISEPL = models.CharField(max_length=1)
	CISE01 = models.IntegerField()  
	CISE02 = models.IntegerField()  
	CISE03 = models.IntegerField()  
	CISE04 = models.IntegerField()  
	CISE05 = models.IntegerField()  
	CISE06 = models.IntegerField()  
	CISE07 = models.IntegerField()  
	CISE08 = models.IntegerField()  
	CISE09 = models.IntegerField()  
	CISE10 = models.IntegerField()  
	CILR01 = models.CharField(max_length=1)
	CILR02 = models.CharField(max_length=1)
	CILR03 = models.CharField(max_length=1)
	CILR04 = models.CharField(max_length=1)
	CILR05 = models.CharField(max_length=1)
	CILR06 = models.CharField(max_length=1)
	CILR07 = models.CharField(max_length=1)
	CILR08 = models.CharField(max_length=1)
	CILR09 = models.CharField(max_length=1)
	CILR10 = models.CharField(max_length=1)
	CIAN8  = models.IntegerField()  
	CIPOCS = models.IntegerField()  
	CIINCS = models.IntegerField()  
	CIIALP = models.IntegerField()  
	CIBSDY = models.IntegerField()  
	CIIA1  = models.IntegerField()  
	CIIB1  = models.IntegerField()  
	CIIC1  = models.IntegerField()  
	CIIA2  = models.IntegerField()  
	CIIB2  = models.IntegerField()  
	CIIC2  = models.IntegerField()  
	CIIA3  = models.IntegerField()  
	CIIB3  = models.IntegerField()  
	CIIC3  = models.IntegerField()  
	CIPNC  = models.IntegerField()  
	CIGLPO = models.CharField(max_length=1)
	CIUNGL = models.CharField(max_length=1)
	CICMGL = models.CharField(max_length=1)
	CICSMT = models.CharField(max_length=2)
	CIPCSM = models.CharField(max_length=2)
	CIBACK = models.CharField(max_length=1)
	CICOMH = models.IntegerField()  
	CIICRI = models.CharField(max_length=1)
	CIIARI = models.CharField(max_length=1)
	CIMATY = models.CharField(max_length=1)
	CIXRT  = models.CharField(max_length=2)
	CIXRT2 = models.CharField(max_length=2)
	CIARTG = models.CharField(max_length=12)
	CIDA01 = models.CharField(max_length=1)
	CIDA02 = models.CharField(max_length=1)
	CIDA03 = models.CharField(max_length=1)
	CIDA04 = models.CharField(max_length=1)
	CIDA05 = models.CharField(max_length=1)
	CIDA06 = models.CharField(max_length=1)
	CIDA07 = models.CharField(max_length=1)
	CIDA08 = models.CharField(max_length=1)
	CIDA09 = models.CharField(max_length=1)
	CIDA10 = models.CharField(max_length=1)
	CIDA11 = models.CharField(max_length=1)
	CIDA12 = models.CharField(max_length=1)
	CIDA13 = models.CharField(max_length=1)
	CIDA14 = models.CharField(max_length=1)
	CIDA15 = models.CharField(max_length=1)
	CIDA16 = models.CharField(max_length=1)
	CISYM4 = models.CharField(max_length=1)
	CIWIUM = models.CharField(max_length=2)
	CIVUMD = models.CharField(max_length=2)
	CIUWUM = models.CharField(max_length=2)
	CIULOT = models.CharField(max_length=1)
	CILCTL = models.CharField(max_length=1)
	CIWCTL = models.CharField(max_length=1)
	CIMVER = models.CharField(max_length=3)
	CICLOC = models.CharField(max_length=20)
	CIXLOC = models.CharField(max_length=20)
	CISTPU = models.CharField(max_length=1)
	CIDNTP = models.CharField(max_length=1)
	CITMPS = models.IntegerField()  
	CIUSMT = models.CharField(max_length=1)
	CIOT1Y = models.CharField(max_length=1)
	CIOT2Y = models.CharField(max_length=1)
	CIOT3Y = models.CharField(max_length=1)
	CIOT4Y = models.CharField(max_length=1)
	CIOT5Y = models.CharField(max_length=1)
	CIUSID = models.CharField(max_length=1)
	CIUSER = models.CharField(max_length=10)
	CIPID  = models.CharField(max_length=10)
	CIJOBN = models.CharField(max_length=10)
	CIUPMJ = models.IntegerField()
	CITDAY = models.IntegerField()
	CISY   = models.CharField(max_length=4)
	CIMCU  = models.CharField(max_length=12, primary_key=True)
	CIOT6Y = models.CharField(max_length=1)
	CISCTL = models.CharField(max_length=1)
	CISEPS = models.CharField(max_length=1)
	CISYM6 = models.CharField(max_length=1)
	CILAF  = models.CharField(max_length=1)
	CILTFM = models.CharField(max_length=1)
	CIRWLA = models.CharField(max_length=1)
	CILNPA = models.CharField(max_length=1)
	CINCOOC = models.CharField(max_length=3)
	CICSNBF = models.CharField(max_length=1)

	class Meta:
		managed = False
		db_table = u'"CRPDTA"."F41001"'

	def __unicode__(self):
		return self.CIMCU


class F4211(models.Model):
 SDKCOO=models.CharField(max_length=5)
 SDDOCO=models.IntegerField(primary_key=True)
 SDDCTO=models.CharField(max_length=2)
 SDLNID=models.IntegerField()
 SDMCU=models.CharField(max_length=12)
 SDAN8=models.IntegerField()
 SDSHAN=models.IntegerField()
 SDPA8=models.IntegerField()
 SDTRDJ=models.IntegerField()
 SDCNDJ=models.IntegerField()
 SDDGL=models.IntegerField()
 SDITM=models.IntegerField()
 SDLITM=models.CharField(max_length=25)
 SDDSC1=models.CharField(max_length=30)
 SDDSC2=models.CharField(max_length=30)
 SDNXTR=models.CharField(max_length=3)
 SDLTTR=models.CharField(max_length=3)
 SDASN=models.CharField(max_length=8)
 SDKCO=models.CharField(max_length=5)
 SDDOC=models.IntegerField()
 SDDCT=models.CharField(max_length=2)

 class Meta:
  	managed = False
  	db_table = u'"CRPDTA"."F4211"'

 def __unicode__(self):
 	return self.SDMCU

class F42119(models.Model):
 SDKCOO=models.CharField(max_length=5)
 SDDOCO=models.IntegerField(primary_key=True)
 SDDCTO=models.CharField(max_length=2)
 SDLNID=models.IntegerField()
 SDMCU=models.CharField(max_length=12)
 SDAN8=models.IntegerField()
 SDSHAN=models.IntegerField()
 SDPA8=models.IntegerField()
 SDTRDJ=models.IntegerField()
 SDCNDJ=models.IntegerField()
 SDDGL=models.IntegerField()
 SDITM=models.IntegerField()
 SDLITM=models.CharField(max_length=25)
 SDDSC1=models.CharField(max_length=30)
 SDDSC2=models.CharField(max_length=30)
 SDNXTR=models.CharField(max_length=3)
 SDLTTR=models.CharField(max_length=3)
 SDASN=models.CharField(max_length=8)
 SDKCO=models.CharField(max_length=5)
 SDDOC=models.IntegerField()
 SDDCT=models.CharField(max_length=2)

 class Meta:
  	managed = False
  	db_table = u'"CRPDTA"."F42119"'

 def __unicode__(self):
 	return self.SDMCU


class F0116(models.Model):
	ALAN8=models.IntegerField(primary_key=True)
	ALADD1=models.CharField(max_length=40)
	ALADD2=models.CharField(max_length=40)
	ALADD3=models.CharField(max_length=40)
	ALADD4=models.CharField(max_length=40)
	ALADDZ=models.CharField(max_length=12)
	ALCTY1=models.CharField(max_length=25)
	ALADDS=models.CharField(max_length=3)
	ALCTR=models.CharField(max_length=3)
	class Meta:	
 		managed = False
 		db_table = u'"CRPDTA"."F0116"'
	def __unicode__(self):
 		return str(self.ALAN8)

class F0005(models.Model):
	DRSY=models.CharField(max_length=4,primary_key=True)
	DRRT=models.CharField(max_length=2)
	DRKY=models.CharField(max_length=10)
	DRDL01=models.CharField(max_length=30)
	DRDL02=models.CharField(max_length=30)
	class Meta:
 		managed = False
 		db_table = u'"CRPCTL"."F0005"'
	def __unicode__(self):
 		return self.DRSY

class F0115(models.Model):
	WPAN8=models.IntegerField(primary_key=True)
	WPAR1=models.CharField(max_length=6)
	WPPH1=models.CharField(max_length=20)
	class Meta:
 		managed = False
 		db_table = u'"CRPDTA"."F0115"'
	def __unicode__(self):
 		return str(self.WPAN8)

class F0111(models.Model):
	WWAN8=models.IntegerField(primary_key=True)
	WWMLNM=models.CharField(max_length=40)
	WWALPH=models.CharField(max_length=40)
	class Meta:
 		managed = False
 		db_table = u'"CRPDTA"."F0111"'
	def __unicode__(self):
 		return str(self.WWAN8)

class F01151(models.Model):
	EAAN8=models.IntegerField(primary_key=True)
	EAEMAL=models.CharField(max_length=256)     # ojo NVARCHAR(256)
	class Meta:
		managed = False
		db_table = u'"CRPDTA"."F01151"'
	def __unicode__(self):
		return str(self.EAAN8)





