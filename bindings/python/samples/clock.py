#!/usr/bin/env python3
# coding: UTF-8
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
import time
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
 
class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="21:52")
 
    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x13.bdf")
        textColor = graphics.Color(100, 100, 255)
        pos = offscreen_canvas.width
        my_text = self.args.text
 
        while True:
            d = datetime.now()
            h = (" " + str(d.hour))[-2:]
            #スペースを頭に着けて最後から2文字背取得。1-9時の間も真ん中に時計が表示されるようにする考慮
            my_text = h + ":" + d.strftime("%M")
            #my_text = "ﾃｽﾄ"
            #logger.debug(my_text)
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, 2, 12, textColor, my_text)
 
            time.sleep(0.01)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
 
 
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()