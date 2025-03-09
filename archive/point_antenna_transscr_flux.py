import math

def run():
	lamda=5.0
	D=10000.0
	I0=10.0
	A=math.sqrt(I0)
	p=1000
	pi=3.1416
	size=1000
	ant=500

	for np in range(-p,p+1):
		RPAT=0
		IPAT=0
		for nl in range(-size,size+1):
			for nb in range(-size,size+1):
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

