from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI
from compas_extension.beam import Beam

__commandname__ = "PLUGIN_NAME_create_beam"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    line = compas_rhino.select_line(message="Select a line to convert to a beam.")
    if not line:
        return
    
    thickness = compas_rhino.rs.GetReal("Thickness of the beam", 2)

    start = compas_rhino.rs.CurveStartPoint(line)
    end = compas_rhino.rs.CurveEndPoint(line)
    beam = Beam(start, end, thickness)

    ui.scene.add(beam, name = "beam")
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
