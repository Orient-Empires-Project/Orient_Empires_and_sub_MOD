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
trait_education_list_str = [
	"业余阴谋家","浮夸的欺诈师","暗中策划者","难以捉摸的影子",
	"天真的绥靖者","合格的谈判者","魅力非凡的说客","幕后操控人",
	"放荡的浪子","节俭的职员","财富创造者","点石成金者",
	"鲁莽的战士","坚强的战士","优秀战术家","天才军事家",
	"尽责的书吏","有见地的思想家","明睿的智者","哲学大师"
	]
trait_education_list=[
	'trait_education_intrigue_1','trait_education_intrigue_2','trait_education_intrigue_3','trait_education_intrigue_4',
	'trait_education_diplomacy_1','trait_education_diplomacy_2','trait_education_diplomacy_3','trait_education_diplomacy_4',
	'trait_education_stewardship_1','trait_education_stewardship_2','trait_education_stewardship_3','trait_education_stewardship_4',
	'trait_education_martial_1','trait_education_martial_2','trait_education_martial_3','trait_education_martial_4',
	'trait_education_learning_1','trait_education_learning_2','trait_education_learning_3','trait_education_learning_4'
]
class trait_dialog ( wx.Dialog ):

	def __init__( self, parent , newChar):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"特性列表", pos = wx.DefaultPosition, size = wx.Size( 194,276 ), style = wx.DEFAULT_DIALOG_STYLE )
		self.newChar = newChar
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"以后再做", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		m_choice5Choices = trait_education_list_str #[ u"教育特质1", u"教育特质" ]
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		for item in trait_education_list:
			if item in self.newChar.traitlist:
				self.m_choice5.SetSelection( trait_education_list.index(item) )
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
		self.newChar.traitlist.clear()
		self.newChar.traitlist.add(trait_education_list[self.m_choice5.GetSelection()])
		event.Skip()


