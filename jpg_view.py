import wx
import glob


class MyApp(wx.Frame):


    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)


        self.init_ui()


    def init_ui(self):
        self.SetTitle('gazou')
        self.SetSize((1400, 1000))
        self.Show()


        files = glob.glob('../jpg/*.jpg')#直下のjpgファイルのリストを取得
        x=0
        y=0
        for picture in files:
            panel_ui = wx.Panel(self, -1, pos=(50+x, 50+y), size=(200, 100))


            image = wx.Image(picture)
            image = image.Scale(200,100,wx.IMAGE_QUALITY_HIGH)
            bitmap = image.ConvertToBitmap()


            wx.StaticBitmap(panel_ui, -1, bitmap, pos=(0, 0), size=image.GetSize())
            x = x + 200
            if x > 1000:
                x=0
                y= y + 100    


app = wx.App()
MyApp(None)
app.MainLoop()