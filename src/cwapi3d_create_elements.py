import os
import sys

import utility_controller as uc
import attribute_controller as ac
import cadwork
import element_controller as ec
import geometry_controller as gc
import visualization_controller as vc


# set python path for the plugin - add dependencies like numpy to the python path
# assume your packages are int .venv/Lib/site-packages
os.environ['PYTHONPATH'] = os.pathsep.join([
    os.path.join(os.path.dirname(__file__), '.venv', 'Lib', 'site-packages'),
    os.path.join(os.path.dirname(__file__), 'src'),
    os.path.dirname(__file__),
    os.path.join(uc.get_plugin_path()),
])

sys.path.extend(os.environ['PYTHONPATH'].split(os.pathsep))

# use pydevd_pycharm to debug the plugin - set the host and port to your pycharm debugger
# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=5001, stdoutToServer=True, stderrToServer=True)

# printing all paths
print(sys.path)

from abc import ABC, abstractmethod

class CadworkObject(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

class Beam(CadworkObject):
    def __init__(self, width, height, p1, p2, p3):
        self.width = width
        self.height = height
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.beam = self.create_beam()

    def create_beam(self):
        return ec.create_rectangular_beam_points(self.width, self.height, self.p1, self.p2, self.p3)

    def set_name(self, name):
        ac.set_name([self.beam], name)

    def set_color(self, color):
        vc.set_color([self.beam], color)

class Panel(CadworkObject):
    def __init__(self, relating_beam, width, height):
        self.beam = relating_beam
        self.width = width
        self.height = height
        self.panel = self.create_panel()

    def create_panel(self):
        beam_p1 = gc.get_p1(self.beam.beam)
        beam_p2 = gc.get_p2(self.beam.beam)
        beam_zl = gc.get_zl(self.beam.beam)
        offset = beam_zl * (self.beam.height + self.height) * 0.5
        panel_p1 = beam_p1 - offset
        panel_p2 = beam_p2 - offset
        beam_p3 = self.beam.p3
        return ec.create_rectangular_panel_points(self.width, self.height, panel_p1, panel_p2, beam_p3)

    def set_name(self, name):
        ac.set_name([self.panel], name)

    def set_color(self, color):
        vc.set_color([self.panel], color)

class BeamPanelCreator:
    def __init__(self, beam_width, beam_height, beam_p1, beam_p2, beam_p3, panel_height):
        self.beam_width = beam_width
        self.beam_height = beam_height
        self.beam_p1 = beam_p1
        self.beam_p2 = beam_p2
        self.beam_p3 = beam_p3
        self.panel_height = panel_height

    def create_beam_and_panel(self):
        beam = Beam(self.beam_width, self.beam_height, self.beam_p1, self.beam_p2, self.beam_p3)
        beam.set_name("Beam")
        beam.set_color(10)

        panel_width = self.beam_p1.distance(self.beam_p2)
        panel = Panel(beam, panel_width, self.panel_height)
        panel.set_name("Panel")
        panel.set_color(5)

        return beam, panel

def main():
    beam_width = 120
    beam_height = 240
    beam_p1 = cadwork.point_3d(0, 0, 0)
    beam_p2 = cadwork.point_3d(0, 0, 1000)
    beam_p3 = cadwork.point_3d(0, 1, 0)
    panel_height = 27

    creator = BeamPanelCreator(beam_width, beam_height, beam_p1, beam_p2, beam_p3, panel_height)
    creator.create_beam_and_panel()

if __name__ == '__main__':
    main()


