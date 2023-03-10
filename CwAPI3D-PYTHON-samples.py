import sys
import utility_controller as uc
import attribute_controller as ac
import cadwork
import element_controller as ec
import geometry_controller as gc
import visualization_controller as vc

# get userprofil path
USERPROFIL = uc.get_3d_userprofil_path()

# appending a path
sys.path.append("C:/Users/michael.brunner/PycharmProjects/testCWAPI/CwAPI3D-PYTHON-samples/Lib/site-packages")

import pydevd_pycharm

pydevd_pycharm.settrace('localhost', port=5001, stdoutToServer=True, stderrToServer=True)

# printing all paths
print(sys.path)

beam_width = 120
beam_height = 240
beam_p1 = cadwork.point_3d(0, 0, 0)
beam_p2 = cadwork.point_3d(0, 0, 1000)
beam_p3 = cadwork.point_3d(0, 1, 0)

panel_width = beam_p1.distance(beam_p2)
panel_height = 27


def main():
    # beam
    beam = ec.create_rectangular_beam_points(beam_width, beam_height, beam_p1, beam_p2, beam_p3)
    ac.set_name([beam], "Beam")
    vc.set_color([beam], 10)
    # panel
    panel_p1 = gc.get_p1(beam)
    panel_p2 = gc.get_p2(beam)
    beam_zl = gc.get_zl(beam)
    panel_p1 -= beam_zl * (beam_height + panel_height) * .5
    panel_p2 -= beam_zl * (beam_height + panel_height) * .5
    panel = ec.create_rectangular_panel_points(panel_width, panel_height, panel_p1, panel_p2, beam_p3)
    ac.set_name([panel], "panel")
    vc.set_color([panel], 5)


if __name__ == '__main__':
    main()
