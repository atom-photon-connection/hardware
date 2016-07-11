import slm
import os
from numpy import *
from matplotlib.pyplot import *
from time import sleep

def ramp(kx, ky):
    x = arange(512.)/2.
    y = arange(512.)/2.
    x, y = meshgrid(x, y)
    return (kx*x + ky*y).astype(uint8)

# Load linear LUT for overdrive
# slm.lut()
# slm.overdrive(ramp(10,0))
# sleep(1)

# Load normal LUT file
filename = os.path.join(os.path.dirname(__file__), 'slm3995_at1064_P8.lut')
slm.lut(filename)

# Spinning beam_profiler
# for theta in arange(0,2*pi,.1):
#     r = 10
#     x = r*cos(theta)
#     y = r*sin(theta)
#     slm.show(ramp(x,y))
#     sleep(.1)

# Moving beam_profiler
# for x in arange(-128,128):
#     slm.show(ramp(x,x))
#     sleep(.1)

# Young's slit
image = zeros([512,512], uint8)
for phi in range(256):
    for x in range(230,240):
        image[:,x] = arange(512)*50
    for x in range(270,280):
        image[:,x] = arange(512)*50 + phi
    slm.show(image)
    sleep(.01)
imshow(image)

slm.kill()

show()