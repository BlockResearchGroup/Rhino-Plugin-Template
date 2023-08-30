from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin
from compas_extension.beam import Beam

from compas_ui.rhino.objects import RhinoObject

from .beamobject import RhinoBeamObject


@plugin(category="ui", requires=["Rhino"])
def register_objects():
    RhinoObject.register(Beam, RhinoBeamObject, context="Rhino")

    print("compas_extension Rhino Objects registered.")


__all__ = [
    "RhinoBeamObject",
]
