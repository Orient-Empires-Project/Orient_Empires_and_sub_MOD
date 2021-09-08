# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
# import wxLocale 
# 研读 https://www.cnblogs.com/zhongtang/p/5929860.html
###########################################################################
## Class trait_dialog
###########################################################################

class trait_dialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"特性列表", pos = wx.DefaultPosition, size = wx.Size( 194,276 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"以后再做", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		m_choice5Choices = [ u"教育特质1", u"教育特质" ]
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		bSizer1.Add( self.m_choice5, 0, wx.ALL, 5 )

		m_listBox4Choices = [ u"特质1", u"特质2" ]
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, wx.LB_MULTIPLE )
		bSizer1.Add( self.m_listBox4, 0, wx.ALL, 5 )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		bSizer1.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.closeTheResultCancel )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.closeTheResultOK )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def closeTheResultCancel( self, event ):
		event.Skip()

	def closeTheResultOK( self, event ):
		event.Skip()


