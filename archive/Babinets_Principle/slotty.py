import math

def run():
	lamda=2.0
	l=30	#even
	b=6
	d=12
	D=800.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=100.0
	A=math.sqrt(I0)
	p=400
	pi=3.1415926535897932384626433832795
	ant=10000.0

	dist=ant+D

	for np in range(-p,p+1):
		RPAT=0
		IPAT=0
		for nl in range(-l/2+1,l/2):
			for nb in range(d+b/2+1,d+3*b/2):			
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

		tac=math.sqrt(dist*dist+np*np)
		real=(A*math.cos(2*pi*tac/lamda)/tac)-RPAT
		imaginary=(A*math.sin(2*pi*tac/lamda)/tac)-IPAT
		print real*real+imaginary*imaginary


