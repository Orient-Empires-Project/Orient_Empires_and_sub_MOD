import wx
import wx.xrc
import testframe

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()

    main_win = testframe.MyFrame1(None)
    main_win.Show()

    app.MainLoop()