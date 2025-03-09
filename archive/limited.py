def bun():
	A=10.0
	d=1000
	lim=100
	increment=0.01
	num=lim/increment
	sum=A/d
	sumr=0
	sumi=0
	for i in range(0,num+1):
		ri=i*increment
		z=math.sqrt(d*d+ri*ri)
		sumr=sumr+(2*A*math.cos(d/z))/z
		sumi=sumi+(2*A*math.sin(d/z))/z
	print sum+sumi*sumi+sumr*sumr
