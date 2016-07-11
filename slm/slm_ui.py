'''
Created on 7 Jul 2016

@author: dustin
'''
import os

os.environ['ETS_TOOLKIT'] = 'qt4'
from enable.component_editor import ComponentEditor
from chaco.plot import Plot, ImagePlot, ArrayPlotData
from chaco.default_colormaps import jet
from numpy import *
from traits.api import HasTraits, Range, Instance, on_trait_change
from traitsui.api import View, Item
import slm

class SLM_UI(HasTraits):
    plot = Instance(Plot)
    focus = Range(-.01,.01)
    spherical = Range(-.1,.1)
    a = Range(0.,1.)

    view = View(
                Item('plot', editor=ComponentEditor(), show_label=False),
                Item('focus'),
                Item('spherical'),
                Item('a'), resizable=True)

    def __init__(self):
        super(SLM_UI, self).__init__()
        filename = os.path.join(os.path.dirname(__file__), 'slm3995_at1064_P8.lut')
        slm.lut(filename)
        
        self.focus = 0
        self.spherical = 0
        self.a = 1
        
        x = arange(512)
        self.x, self.y = meshgrid(x, x)
        self.r2 = (self.x - 256.)**2 + (self.y - 256.)**2
        self.r4 = self.r2**2
        self.plotdata = ArrayPlotData(x=self.x, y=self.y)
        self.calculate()
        plot = Plot(self.plotdata)
        plot.img_plot('series1', colormap=jet)
        self.plot = plot
    
    @on_trait_change('focus, a, spherical')    
    def calculate(self):
        mask = zeros([512,512])
        mask[self.r2 > (256*self.a)**2] = 1
        self.z = ((1-mask)*(self.focus*self.r2 + self.spherical*self.r4/256.**2) + mask*self.x*50).astype(uint8)
        
        self.plotdata.set_data('series1', self.z)
        slm.show(self.z)
        
if __name__ == '__main__':
    SLM_UI().configure_traits()
    slm.kill()