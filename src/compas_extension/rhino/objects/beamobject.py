from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_ui.rhino.objects import RhinoLineObject
from compas.colors import Color
from compas_ui.values import Settings
from compas_ui.values import BoolValue
from compas_ui.values import ColorValue
from compas_ui.values import StrValue


class RhinoBeamObject(RhinoLineObject):
    SETTINGS = Settings(
        {
            "layer": StrValue("compas_extension::Beam"),
            "show.line": BoolValue(True),
            "show.brep": BoolValue(True),
            "color.line": ColorValue(Color.blue()),
            "color.brep": ColorValue(Color.red()),
        }
    )

    def __init__(self, beam, **kwargs):
        super(RhinoBeamObject, self).__init__(beam, **kwargs)
        self.beam = beam

    def draw(self):
        self.artist.layer = self.settings["layer"]

        self.clear()
        if not self.visible:
            return

        line_guids = []
        brep_guids = []

        if self.settings["show.line"]:
            line_guids += self.artist.draw_line(self.beam, color=self.settings["color.line"])
        if self.settings["show.brep"]:
            brep_guids += self.artist.draw_brep(self.beam, color=self.settings["color.brep"])

        self.guids += line_guids + brep_guids
