import math

def run():
	lamda=0.810
	l=1000	#even
	b=30
	d=100
	D=180000.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=100.0
	A=math.sqrt(I0)
	p=6000
	pi=3.1416
	ant=180000.0

	for np in range(-p,p+1):
		RPAT=0
		IPAT=0
		for nl in range(-l/2,l/2+1):
			for nb in range(d+b/2,(d+3*b/2)+1):			
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


