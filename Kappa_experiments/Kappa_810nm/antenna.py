import math

def run():
	lamda=0.810
	D=180000.0
	I0=100.0
	p=6000
	
	pi=3.1416
	ant=180000.0

	dist=ant+D

	for np in range(-p,p+1):

		t=dist*dist+np*np		
		PAT=I0/t
		print PAT


