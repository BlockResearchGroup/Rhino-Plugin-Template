from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin
from compas_rhino.artists import RhinoArtist

from compas_extension.beam import Beam

from .beamartist import RhinoBeamArtist


@plugin(category="factories", requires=["Rhino"])
def register_artists():
    RhinoArtist.register(Beam, RhinoBeamArtist, context="Rhino")
    print("compas_extension Rhino Artists registered.")


__all__ = [
    "RhinoBeamArtist",
]
