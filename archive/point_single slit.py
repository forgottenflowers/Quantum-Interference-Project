import math

def run():
	lamda=5.0
	l=30	#even
	b=12
	D=10000.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=10.0
	A=math.sqrt(I0)
	p=1000
	pi=3.1416
	ant=500

	for np in range(-p,p+1):
		RPAT=0
		IPAT=0
		for nl in range(-l/2,l/2+1):
			for nb in range(-b/2,b/2+1):
				y=np-nb                              #vertical displacement y			
				temp=nl*nl+D*D                       #x^2+z^2
				add=math.sqrt(nb*nb+nl*nl+ant*ant)   #antenna to screen
				root=math.sqrt(y*y+temp)             #screen to detector
				t=root+add                           #total path length 
				q=root*add                           #product (intensity to fall)				
				R=A*math.cos(2*pi*t/lamda)/q         #real
				I=A*math.sin(2*pi*t/lamda)/q         #imaginary	
				RPAT=RPAT+R                          #superposition
				IPAT=IPAT+I
		print RPAT*RPAT+IPAT*IPAT

