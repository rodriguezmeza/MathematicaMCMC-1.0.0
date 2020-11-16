
# C1::
# NagBody :: Numerical Algorithms for General Body Dynamics and data analysis

#MathematicaMCMC code

#Author:
#Mario A. Rodríguez-Meza
#Instituto Nacional de Investigaciones Nucleares
#marioalberto.rodriguez@inin.gob.mx
#Ciudad de México. January 1st, 2019
#Updated: 2020-11-5

# C2::
from __future__ import print_function
#Show plots inline, and load main getdist plot module and samples class
#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'
import sys, os
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
import numpy as np
from getdist import plots, MCSamples, chains
import getdist, IPython
print('Version: ',getdist.__version__)
# use this *after* importing getdist if you want to use interactive plots
# %matplotlib notebook
import matplotlib.pyplot as plt
import IPython
print('GetDist Version: %s, Matplotlib version: %s'%(getdist.__version__, plt.matplotlib.__version__))
# matplotlib 2 may not work very well without usetex on, can uncomment
# plt.rcParams['text.usetex']=True

# C3::
# Configure according to your needs
download_dir = "./Results/getdist_analysis/"
confidenceL_dir="confidenceRegions/"
posteriors_dir="posteriors/"
chainsDir="./Results/Chains/"
fileStr="IC2574_PISO"
chainLoadSample=chainsDir+fileStr+"-MCExt"

# C4::
#Load from file
from getdist import loadMCSamples, chains, MCSamples

# Load individual samples:
#samples = loadMCSamples(chainLoadSample, settings={'ignore_rows':0.3})
# It was already burned
samples = loadMCSamples(chainLoadSample)

# C5::
# PDF files of the posteriors:
posteriors = download_dir+posteriors_dir+fileStr+"_histograms.pdf"

# C6::
# PDF files of the confidence regions files:
confidenceL = download_dir+confidenceL_dir+fileStr+"_confidence.pdf"

# C7::
# Multiple 1D subplots

g = plots.get_subplot_plotter(width_inch=10)

# Plot and save to a file:
g.plots_1d(samples, ['p1', 'p2', 'p3', 'p4','p5','p6'], nx=6);
g.export(posteriors)

# C8::
# Multiple 2D subplots
g = plots.get_subplot_plotter(subplot_size=2.0)
g.settings.scaling = False # prevent scaling down font sizes even though small subplots

# Plot and save to a file:
g.plots_2d(samples, param_pairs=[['p1', 'p2'], ['p1', 'p3'],['p1', 'p4'], ['p2', 'p3'], ['p2', 'p4'], ['p3', 'p4']], 
           nx=6, filled=True);
g.export(confidenceL)

# C9::
# Triangle plot
g = plots.get_subplot_plotter()
g.triangle_plot([samples], filled=True)


# C10::
# LaTeX format of parameters:
#
print(samples.getInlineLatex('p1',limit=1))

print(samples.getInlineLatex('p2',limit=1))

print(samples.getInlineLatex('p3',limit=1))

print(samples.getInlineLatex('p4',limit=2))

print(samples.getInlineLatex('p5',limit=1))

print(samples.getInlineLatex('p6',limit=1))

# C11::
# Principal component analysis results:
print(samples.PCA(['p1','p2','p3','p4','p5','p6']))

# C12::
# Covariance matrix:
print(samples.cov())





