import math

def run():
	lamda=5.0
	D=4665.5920684934835610779461674915
	I0=10.0
	p=50
	
	pi=3.1416
	ant=120

	dist=ant+D

	for np in range(-p,p+1):

		t=dist*dist+np*np		
		PAT=I0/t
		print PAT


