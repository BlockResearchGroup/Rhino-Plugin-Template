from __future__ import print_function
from __future__ import absolute_import
from __future__ import division


from compas.geometry import Line


class Beam(Line):
    """An example beam."""

    def __init__(self, p1, p2, thickness, up_axis=None, **kwargs):
        super(Beam, self).__init__( p1, p2, **kwargs)
        self.thickness = thickness
        self.up_axis = up_axis or [0, 0, 1]