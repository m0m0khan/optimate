"""
********
Optimate
********
Optimate is an automatic parameter optimizer for different material models with the ability to optimize creep and relaxation experiments simultaneously. It utilizes minimization algorithms, such as Nelder-Mead and L-BFGS-B, for the minimization of the residual function. It is created within the scope of the project "Maintenance concepts for flanges and bolted joint connections operated at high temperateres under flexible load conditions" (German short: Relaxationsverhalten II).

The residual function is basically the difference between the measured and computed creep strain values, where the first computation curve is generated by providing an initial guess to the optimizer. Therefore, for utilizing optimate, an initial guess file with model parameters and the measured creep strain data is required.

Optimate is completely command line based user-friendly tool. User has the choice of experiments to be optimized as well as the choice of optimizer. As a result, a csv file of optimized parameters are generated at the end of a successful run.

Supported Material Models
#########################
Currently following material models are supported:

1. Norton-Bailey
2. KORA - Chaboche type viscoplastic material model developed at MPA / IfW
3. Implicit Garofalo Model - Developed at MPA / IfW
4. Modified Garofalo Model - Developed at MPA / IfW
"""

# importing module
import sys, os
from . import utilities
from .utilities import *

rootdir = os.path.dirname(os.path.abspath(__file__))
path = rootdir + '/utilities/'
sys.path.append(path)

exec(open(os.path.join(rootdir, 'version.py')).read())


submodules = [
    '__version__'
 ]
 
__all__ = submodules
__all__.extend(utilities.__all__)
__version__ = version


def __dir__():
    return list(globals().keys())

import importlib as _importlib

def __getattr__(__name__):
    if __name__ in submodules:
        return _importlib.import_module(f'optimate.{__name__}')
    else:
        try:
            return globals()[__name__]
        except KeyError:
            raise AttributeError(
                f"Module 'optimate' has no attribute '{__name__}'"
            )

# Pytest testing
from optimate._pytesttester import PytestTester
test = PytestTester(__name__)
del PytestTester