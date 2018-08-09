Batches           = 16
SerpentAxialZones = 1
ShuffleScheme     = [16,1,15,2,14,3,13,4,12,5,11,6,10,7,9,8]

Moves = Batches * SerpentAxialZones

A = []

for axial in range(SerpentAxialZones):

	for batch in ShuffleScheme:

		A.append("Batch" + str(batch) + "Axial" + str(axial+1))

shufflescheme = {}

#print(A)

for move in range(Moves-1):

	A1 = A[move]
	A2 = A[move+1]

	ss = {A1 : A2}
	shufflescheme.update(ss)

print(shufflescheme)

from pylab import *

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

axes([0.025,0.025,0.95,0.95])

plot (X, Y+1, color='blue', alpha=1.00)
fill_between(X, 1, Y+1, color='blue', alpha=.25)

plot (X, Y-1, color='blue', alpha=1.00)
fill_between(X, -1, Y-1, (Y-1) > -1, color='blue', alpha=.25)
fill_between(X, -1, Y-1, (Y-1) < -1, color='red',  alpha=.25)

xlim(-np.pi,np.pi), xticks([])
ylim(-2.5,2.5), yticks([])
savefig('plot_ex.png',dpi=48)
show()
