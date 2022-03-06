import matplotlib.pyplot as plt
import pyart
import netCDF4
import glob

print('Money..!')

# filename='KASPR_20130912-084548_rppvasu.nc'
# # filename = 'T_HAHA00_C_VABB_20200603155923_RAWsweep2.nc'
#
# # radar = pyart.io.read(filename)
# radar = pyart.io.read(filename)
# display = pyart.graph.RadarDisplay(radar)
#
# display.plot('DBZ')
# plt.show()




# Author: Jonathan J. Helmus (jhelmus@anl.gov)
# License: BSD 3 clause

import matplotlib.pyplot as plt
import pyart

# filename = 'T_HAHA00_C_VABB_20200603155923_RAWsweep2.nc'
filename='KASPR_20130912-084548_rppvasu.nc'


# create the plot using RadarDisplay (recommended method)
radar = pyart.io.read(filename)
display = pyart.graph.RadarDisplay(radar)
fig = plt.figure()
ax = fig.add_subplot(111)
display.plot('VEL', 0, vmin=-32, vmax=64.)
display.plot_range_rings([5,10,15,20,25,30])
display.plot_cross_hair(5.)
plt.show()



