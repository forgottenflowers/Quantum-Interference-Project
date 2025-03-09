import math

def run():
	lamda=5.0
	I0=10.0
	p=1000
	pi=3.1416
	dist=1000500

	for np in range(-p,p+1):

		t=dist*dist+np*np		
		PAT=I0/t
		print PAT

