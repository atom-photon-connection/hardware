import os
import time
import slm
from numpy import *
from matplotlib.pyplot import *
from scipy.optimize.minpack import curve_fit
from d2k import DAQ2502

def ramp(kx, ky):
    x = arange(512.)/2.
    y = arange(512.)/2.
    x, y = meshgrid(x, y)
    return (kx*x + ky*y).astype(uint8)
 
def fit_gaussian2d((x, y), x0, y0, w0, h, b):
    return h*exp(-2*((x-x0)**2+(y-y0)**2)/w0**2).ravel() + b

filename = os.path.join(os.path.dirname(__file__), 'slm3995_at1064_P8.lut')
slm.lut(filename)

daq = DAQ2502(0)


n = 16
w = 512/n
profile = zeros([n,n], float64)
for y in range(n):
    for x in range(n):
        mask = zeros([512,512], uint8)
        mask[y*w:(y+1)*w,x*w:(x+1)*w] = 1
        slm.show(ramp(64,0)*mask)
        time.sleep(.03)
        profile[y,x] = daq.read()[0]
    print 'finished row:', y, 'of', n

slm.show(ramp(0,0))

    
px = 0.015*w
x = arange(n)*px
x, y = meshgrid(x, x)
 
 
p = [5,5,2.5,1000,300]
p, pcov = curve_fit(fit_gaussian2d, (x, y), profile.ravel(), p)
print p
print '(x0, y0): (', p[0], p[1],') mm'
print 'Waist:', p[2], 'mm'
f = reshape(fit_gaussian2d((x,y), *p), profile.shape)

figure(1)
imshow(profile, interpolation='none')
colorbar()
savefig(os.path.join(os.path.dirname(__file__),'beam_profile.png'))
savetxt(os.path.join(os.path.dirname(__file__),'beam_profile.txt'), profile)

figure(2)
imshow(f, interpolation='none')

show()
daq.release()