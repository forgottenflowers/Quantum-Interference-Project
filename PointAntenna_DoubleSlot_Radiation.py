# Generate radiation pattern, when point antenna radiation is blocked by a double slot (inverse of double-slit).

import math

def run():
	lamda=5.0       			# Wavelength
	l=30.0					# length of slit (even)
	b=12.0					# breadth of slit (even)
	d=100.0					# distance between slits
	D=1000000.0				# distance of detection from screen
	F=(b*b)/(D*lamda)
	print "Fresnel number = ",F,":"
	I0=10.0         			# Intensity amplitude
	A=math.sqrt(I0)
	p=1000000      				# number of data points
	pi=3.1416
	size=1000000				# size of open space we are calculating for
	ant=500					# distance of antenna from screen

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
