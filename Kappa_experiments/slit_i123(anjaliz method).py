import math

def run():
	lamda=5.0
	l=30	#even
	b=12
	d=18.0
	D=60.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=10.0
	A=math.sqrt(I0)
	p=50
	pi=3.1416
	ant=120

	for np in range(-p,p+1): #do more than or equal to later  
		RPAT=0
		IPAT=0
		for nl in range(-100,100+1):
			for nb in range(-100,100+1):
				if ((nl>-l/2 and nl<l/2) and ((nb>-d-3*b/2 and nb<-d-b/2) or (nb>-b/2 and nb<b/2) or (nb>d+b/2 and nb<d+3*b/2))):
					y=np-nb			
					temp=nl*nl+D*D
					add=math.sqrt(nb*nb+nl*nl+ant*ant)
					root=math.sqrt(y*y+temp)
					t=root+add
					q=root*add				
					R=A*math.cos(2*pi*t/lamda)/q
					I=A*math.sin(2*pi*t/lamda)/q	
					RPAT=RPAT+R
					IPAT=IPAT+I
				else:
					continue
		print RPAT*RPAT+IPAT*IPAT


