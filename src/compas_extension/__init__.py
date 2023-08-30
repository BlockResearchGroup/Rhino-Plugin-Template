"""
********************************************************************************
compas_extension
********************************************************************************

.. currentmodule:: compas_extension


.. toctree::
    :maxdepth: 1


"""

from __future__ import print_function

import os

# import compas


__author__ = ["Li Chen"]
__copyright__ = "Block Research Group - ETH Zurich"
__license__ = "MIT License"
__email__ = "li.chen@arch.ethz.ch"
__version__ = "0.1.0"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]

__all_plugins__ = [
    "compas_extension.rhino.install",
    "compas_extension.rhino.artists",
    "compas_extension.rhino.objects",
    "compas_extension.rhino.register",
]
