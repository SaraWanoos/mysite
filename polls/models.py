from django.db import models

class Parties(models.Model):
	Pa_id=models.IntegerField(default=0,unique=True,primary_key=True)
	Name=models.CharField(max_length=90)
		



class People(models.Model):
	Fname=models.CharField(max_length=50)
	Mname=models.CharField(max_length=20)
	Lname=models.CharField(max_length=20)
	P_id=models.IntegerField(default=0,unique=True,primary_key=True)
	MobilePhone=models.IntegerField(default=0,unique=True)
	Email=models.CharField(max_length=50)
	Password=models.CharField(max_length=50)
	Sex=models.SlugField(blank = True)
    


class Candidates(models.Model):
	Pa_id=models.ForeignKey(Parties,on_delete=models.CASCADE)
	Fname=models.CharField(max_length=50)
	Mname=models.CharField(max_length=20)
	Lname=models.CharField(max_length=20)
	Link_Image=models.SlugField(blank=True)
	C_id=models.IntegerField(default=0,unique=True,primary_key=True)
	Prog=models.TextField(default='Election program')
                

class Election(models.Model):
	P_id=models.OneToOneField(People,on_delete=models.CASCADE,unique=True)
	C_id=models.ForeignKey(Candidates,on_delete=models.CASCADE)
	Election_date=models.DateTimeField(auto_now=True,verbose_name='Election_date')



class Employee(models.Model):
	E_id=models.IntegerField(default=0,unique=True,primary_key=True)
	Username=models.CharField(max_length=50)
	Password=models.CharField(max_length=50)

		
