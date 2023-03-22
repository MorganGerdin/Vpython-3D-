# Morgan Gerdin

from vpython import *

# hat - cone

firstCone = cone(pos=vector(5,1,0), axis=vector(0,4,0), radius=.75, color=color.red)
secondCone = cone(pos=vector(5,0,1), axis=vector(0,0,1), radius=.3, color=color.orange)


# body - sphere
firstSphere = sphere(pos = vector(5,0,0), color = vector(0.5,0.5,0.5), radius = 1)
secondSphere = sphere(pos = vector(5,-2,0), color = vector(0.5,0.5,0.5), radius = 1.5)

# eyes - tiny sphere
firstEye = sphere(pos = vector(4, 0,2),  color=color.blue,  radius = .1)
secondEye = sphere(pos = vector(4.5,0,2), color=color.blue, radius = .1)

# hat - Helix
firstHelix = helix(pos=vector(5,5,0), axis=vector(3,1,0), radius=0.2)
secondHelix = helix(pos=vector(5,5,0), axis=vector(2.5,-1.5,.3), radius=0.2)
thirdHelix = helix(pos=vector(5,5,0), axis=vector(-1, .7 ,-.7), radius=0.2)
fourthHelix = helix(pos=vector(5,5,0), axis=vector(2, 0 ,1), radius=0.1)
fithHelix = helix(pos=vector(5,5,0), axis=vector(-.8, 1.6 , .2), radius=0.3)
sixthHelix = helix(pos=vector(5,5,0), axis=vector(-1.8, -.9 , -.4), radius=0.3)

