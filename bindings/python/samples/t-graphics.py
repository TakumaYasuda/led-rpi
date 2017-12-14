#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
from PIL import Image

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        a = ("../../../fonts/shnm8x16a.bdf")
        b = ("../../../fonts/shnm7x14r.bdf")
        c = ("../../../fonts/shnm6x12a.bdf")
        d = ("../../../fonts/k8x12L.bdf")
        font.LoadFont(d)
        red = graphics.Color(255, 0, 0)
        # graphics.DrawLine(canvas, 5, 5, 22, 13, red)

        green = graphics.Color(0, 255, 0)
        # graphics.DrawCircle(canvas, 15, 15, 10, green)

        blue = graphics.Color(0, 0, 255)
        graphics.DrawText(canvas, font, 2, 10, blue, "空室")

        time.sleep(10)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
