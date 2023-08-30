from __future__ import print_function
from __future__ import absolute_import
from __future__ import division


from compas_ui.rhino.artists import LineArtist
from compas.geometry import Brep
from compas.geometry import Box
from compas.geometry import Rotation
from compas.geometry import Translation
from compas.geometry import cross_vectors
import compas_rhino


class RhinoBeamArtist(LineArtist):
    def draw_brep(self, beam, color=None):
        box = Box.from_width_height_depth(beam.thickness, beam.length, beam.thickness)
        brep = Brep.from_box(box)

        x_axis = cross_vectors(beam.direction, beam.up_axis)
        y_axis = cross_vectors(beam.direction, x_axis)
        rotation = Rotation.from_basis_vectors(x_axis, y_axis)

        brep.transform(Translation.from_vector([0, 0, beam.length/2]))
        brep.transform(rotation)
        brep.transform(Translation.from_vector(beam.start))

        return [compas_rhino.draw_brep(brep, color=color.rgb, layer=self.layer, redraw=False, clear=False)]

    def draw_line(self, beam, color=None):
        start = list(beam.start)
        end = list(beam.end)
        color = color.rgb255
        lines = [{"start": start, "end": end, "color": color}]
        return compas_rhino.draw_lines(
            lines,
            layer=self.layer,
            clear=False,
            redraw=False,
        )
