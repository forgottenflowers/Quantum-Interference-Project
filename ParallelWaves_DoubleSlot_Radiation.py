# Generate radiation pattern, when antenna is infinitely far away and radiation is blocked by a double slot (inverse of double slit)plane_doubleslot.txt
import math

def run():
	lamda=5.0
	l=30.0	#even
	b=12.0
	d=100.0
	D=10000.0
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=10.0
	A=math.sqrt(I0)
	p=1000
	pi=3.1416
	size=1500

	for np in range(-p,p+1):
		RPAT=0
		IPAT=0
		for nl in range(-size,size+1):
			for nb in range(-size,size+1):
				if (nl>=-l/2) & (nl<=l/2):
					if (nb>=-b-d/2) & (nb<=-d/2):
						continue

					if (nb>=d/2) & (nb<=b+d/2):
						continue		
				y=np-nb			
				temp=nl*nl+D*D
				root=math.sqrt(y*y+temp)
				R=A*math.cos(2*pi*root/lamda)/root
				I=A*math.sin(2*pi*root/lamda)/root	
				RPAT=RPAT+R
				IPAT=IPAT+I
		print RPAT*RPAT+IPAT*IPAT
