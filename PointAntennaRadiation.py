# Generate radiation pattern of point antenna

import math

def run():
	lamda=5.0       # Wavelength
	I0=10.0         # Intensity amplitude
	p=1000000       # number of data points
	pi=3.1416
	dist=1000500    # distance of detection

	for np in range(-p,p+1):

		t=dist*dist+np*np		
		PAT=I0/t
		print PAT      # PAT stands for pattern
