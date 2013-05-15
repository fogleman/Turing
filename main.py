import turing
import wx

WIDTH = 512
HEIGHT = 512
SCALE = 1
STATES = 4
SYMBOLS = 4
SPEED = 10000

COLORS = [
    (69, 114, 167),
    (170, 70, 67),
    (137, 165, 78),
    (110, 84, 141),
    (61, 150, 174),
    (219, 132, 61),
    (142, 165, 203),
    (206, 142, 141),
    (185, 205, 150),
    (165, 151, 185),
]

class View(wx.Panel):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.model = turing.create_model(WIDTH, HEIGHT, STATES, SYMBOLS)
        self.palette = turing.create_palette(COLORS)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.update()
    def on_size(self, event):
        event.Skip()
        self.Refresh()
    def on_left_down(self, event):
        self.model = turing.create_model(WIDTH, HEIGHT, STATES, SYMBOLS)
        self.Refresh()
    def on_paint(self, event):
        data = turing.create_image(self.model, self.palette)
        bitmap = wx.BitmapFromBufferRGBA(WIDTH, HEIGHT, data)
        dc = wx.BufferedPaintDC(self)
        dc.SetUserScale(SCALE, SCALE)
        dc.DrawBitmap(bitmap, 0, 0)
    def update(self):
        turing.updates(self.model, SPEED)
        self.Refresh()
        wx.CallLater(10, self.update)

class Frame(wx.Frame):
    def __init__(self):
        style = wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX
        super(Frame, self).__init__(None, style=style)
        self.SetTitle('Turing Machine')
        self.view = View(self)

def main():
    app = wx.App(False)
    frame = Frame()
    frame.SetClientSize((WIDTH * SCALE, HEIGHT * SCALE))
    frame.Center()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
