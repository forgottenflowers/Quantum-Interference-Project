import math

def run():
	lamda=5.0
	l=30	#even
	b=12
	D=60.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=10.0
	A=math.sqrt(I0)
	p=50
	pi=3.1416
	ant=60

	for np in range(-100,161):
		RPAT=0
		IPAT=0
		for nl in range(-l/2,l/2+1):
			for nb in range(-b/2,b/2+1):					
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
		print RPAT*RPAT+IPAT*IPAT
