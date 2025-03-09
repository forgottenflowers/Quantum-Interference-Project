import math

def run():
	lamda=5.0
	l=30.0	#even
	b=12.0
	d=18
	D=60.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=10.0
	A=math.sqrt(I0)
	p=50
	pi=3.1416
	size=100
	ant=120

	for np in range(-p,p+1):
		RPAT=0
		IPAT=0
		for nl in range(-size,size+1):
			for nb in range(-b-d/2,size+1):
				if ((nb>(-d-b/2)) & (nb<-d)) or ((nb>0) & (nb<b)):
					if (nl>-l/2) & (nl<l/2):
						continue
				y=nb+d/2.0		
				y1=np-y
				y2=np+y
				temp=nl*nl+D*D
				add=math.sqrt(y*y+nl*nl+ant*ant)
				root1=math.sqrt(y1*y1+temp)
				root2=math.sqrt(y2*y2+temp)
				t1=root1+add
				t2=root2+add
				q1=root1*add
				q2=root2*add			
				R1=A*math.cos(2*pi*t1/lamda)/q1
				R2=A*math.cos(2*pi*t2/lamda)/q2
				I1=A*math.sin(2*pi*t1/lamda)/q1
				I2=A*math.sin(2*pi*t2/lamda)/q2
				RPAT=RPAT+R1+R2
				IPAT=IPAT+I1+I2
		print RPAT*RPAT+IPAT*IPAT


