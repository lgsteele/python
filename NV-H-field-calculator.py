import numpy as np

# We have an Igor procedure that will take the emission spectra from the NV-centre and calculate the orientation of the applied field relative to the NV-centre axis.  Here, enter in the field orientation calculated by this procedure.
#Bxnv = float(raw_input('What is Bx relative to the NV center?'))
#Bynv = float(raw_input('What is By relative to the NV center?'))
#Bznv = float(raw_input('What is Bz relative to the NV center?'))
#Bnv = [Bxnv,Bynv,Bznv]
Bnv = [-1.87488,1.03261,6.13815]
# What we want to do is rotate the magnetic field calculated in Igor onto the NV-centre axis, along [0,0,1], i.e.:
Bnvz = [0,0,np.linalg.norm(Bnv)]

# To do this, we will use Rodrigues' Formula to calculate the new location of the field specified in the Helmholtz coils.  First, we enter the initial magnetic field conditions for the H.C.:
#Bxhc = float(raw_input('What is Bx relative to the Helmholtz coils?'))
#Byhc = float(raw_input('What is By relative to the Helmholtz coils?'))
#Bzhc = float(raw_input('What is Bz relative to the Helmholtz coils?'))
#Bhc = [Bxhc,Byhc,Bzhc]
Bhc = [0,0,10]
print 'Bnv =',Bnv
print 'Bnvz =',Bnvz
print 'Bhc =',Bhc

# This function finds the rotation vector and angle that will rotate r1 into r2, then applies that rotation to a vector r3.  The idea is this: calculate the rotation that will take the Igor field (Bnv) and rotate it onto the Helmholtz coil field (Bhc) (i.e.: this is a rotation from the NV coordinate system to the Helmholtz coordinate system), then apply that rotation to rotate the NV center axis (along the z-direction in the NV coordinate system) into the Helmholtz coordinate system.

def fieldcalculation(r1,r2,r3):
# 'Define rotation vector and angle that will rotate r1 into r2'
	rotation_vector = np.cross(r1,r2)
	K = rotation_vector / np.linalg.norm(rotation_vector)

	dp = np.dot(r1,r2)
	dpnorm = dp / (np.linalg.norm(r1)*np.linalg.norm(r2))
	theta = np.arccos(dpnorm)
# Rotate vector r3 about the rotation vector and angle defined above
	norm = (np.linalg.norm(r2)/np.linalg.norm(r3))
	R1 = np.dot(np.cos(theta),r3)
	R2 = np.sin(theta)*np.cross(K,r3)
	R3 = (1-np.cos(theta))*(np.dot(K,r3))*K
	Rsum = R1+R2+R3
	return Rsum*norm

print 'Plug the following vector in for the Helmholtz coils to align the magnetic field along the NV-center axis: ',fieldcalculation(Bnv,Bhc,Bnv)

a1 = [1,0,0]
print 'Assume the NV-center axis is along (1,0,0): ',fieldcalculation(Bnv,Bhc,a1)
a2 = [1,1,0]
print 'Assume the NV-center axis is along (1,1,0): ',fieldcalculation(Bnv,Bhc,a2)
a3 = [1,0,1]
print 'Assume the NV-center axis is along (1,0,1): ',fieldcalculation(Bnv,Bhc,a3)
a4 = [0,1,1]
print 'Assume the NV-center axis is along (0,1,1): ',fieldcalculation(Bnv,Bhc,a4)
a5 = [1,1,1]
print 'Assume the NV-center axis is along (1,1,1): ',fieldcalculation(Bnv,Bhc,a5)
