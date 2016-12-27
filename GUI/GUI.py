# -*- coding: utf-8 -*-

import wx


class GUI(wx.App):
    data = []

    # TODO 外部传入数据
    def SetData(self, data=None):
        self.data = data

    def ToString(self, data=None):
        string = '%12s%12s%12s\n' % ('code', 'name', 'increase')
        if data==None:
            # TODO
            pass
        for one_line in data:
            line = ''
            for item in one_line:
                line += str(item).ljust(12)
            string += line + '\n'
        return string

    def tmp0(self, event):
        # TODO
        pass
    def tmp1(self, event):
        # TODO
        pass
    def tmp2(self, event):
        # TODO
        pass
    def tmp3(self, event):
        # TODO
        string = self.ToString(self.data)
        self.contents.SetValue(string)


    def OnInit(self):
        win = wx.Frame(None, title='Stock Kit',
                       size=wx.DefaultSize)

        # TODO add your widget
        bkg = wx.Panel(win)
        self.code = wx.TextCtrl(bkg, -1, '000001')
        self.contents = wx.TextCtrl(
            bkg, -1, '...', style=wx.TE_MULTILINE | wx.HSCROLL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(self.code, proportion=0, flag=wx.EXPAND)
        vbox1.Add(self.contents, proportion=1, flag=wx.EXPAND)
        Button0 = wx.Button(bkg, label='市场分析')
        Button0.Bind(wx.EVT_BUTTON, self.tmp0)
        Button1 = wx.Button(bkg, label='筹码面')
        Button1.Bind(wx.EVT_BUTTON, self.tmp1)
        Button2 = wx.Button(bkg, label='技术面')
        Button2.Bind(wx.EVT_BUTTON, self.tmp2)
        Button3 = wx.Button(bkg, label='自选股')
        Button3.Bind(wx.EVT_BUTTON, self.tmp3)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(Button0, proportion=0, flag=wx.ALL, border=10)
        vbox2.Add(Button1, proportion=0, flag=wx.ALL, border=10)
        vbox2.Add(Button2, proportion=0, flag=wx.ALL, border=10)
        vbox2.Add(Button3, proportion=0, flag=wx.ALL, border=10)

        hbox = wx.BoxSizer()
        hbox.Add(vbox1, proportion=1, flag=wx.EXPAND)
        hbox.Add(vbox2, proportion=0, flag=wx.ALIGN_CENTRE_VERTICAL)
        bkg.SetSizer(hbox)

        win.Show()
        return True



if __name__ == "__main__":
    app = GUI()
    app.MainLoop()
