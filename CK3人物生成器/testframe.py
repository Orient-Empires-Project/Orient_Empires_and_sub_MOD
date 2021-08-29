# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CK3人物生成器", pos = wx.DefaultPosition, size = wx.Size( 1210,1071 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		ID_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"ID" ), wx.VERTICAL )

		self.ID_textCtrl1 = wx.TextCtrl( ID_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		ID_box.Add( self.ID_textCtrl1, 0, wx.ALL, 5 )


		gbSizer1.Add( ID_box, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		dynasty_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"dynasty" ), wx.VERTICAL )

		dynasty_choice1Choices = [ u"王朝1", u"王朝2" ]
		self.dynasty_choice1 = wx.Choice( dynasty_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dynasty_choice1Choices, 0 )
		self.dynasty_choice1.SetSelection( 0 )
		self.dynasty_choice1.SetToolTip( u"王朝" )

		dynasty_box.Add( self.dynasty_choice1, 0, wx.ALL, 5 )


		gbSizer1.Add( dynasty_box, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		Name_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Name" ), wx.VERTICAL )

		m_comboBox1Choices = [ u"名字1", u"nametest" ]
		self.m_comboBox1 = wx.ComboBox( Name_box.GetStaticBox(), wx.ID_ANY, u"<-请输入或选择->", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		Name_box.Add( self.m_comboBox1, 0, wx.ALL, 5 )


		gbSizer1.Add( Name_box, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		culture_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"culture" ), wx.VERTICAL )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( culture_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		culture_box.Add( self.m_listBox2, 0, wx.ALL, 5 )


		gbSizer1.Add( culture_box, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		religion_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"religion" ), wx.VERTICAL )

		religion_listBox1Choices = [ u"道教", u"佛教", u"儒教" ]
		self.religion_listBox1 = wx.ListBox( religion_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, religion_listBox1Choices, 0 )
		religion_box.Add( self.religion_listBox1, 0, wx.ALL, 5 )


		gbSizer1.Add( religion_box, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		birthday_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"birthday" ), wx.VERTICAL )

		self.m_datePicker4 = wx.adv.DatePickerCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY )
		birthday_box.Add( self.m_datePicker4, 0, wx.ALL, 5 )


		gbSizer1.Add( birthday_box, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		deathday_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"deathday" ), wx.VERTICAL )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		deathday_box.Add( self.m_datePicker1, 0, wx.ALL, 5 )


		gbSizer1.Add( deathday_box, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		eventlist_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"eventlist" ), wx.VERTICAL )


		gbSizer1.Add( eventlist_box, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		parents_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"parents" ), wx.VERTICAL )

		self.father_name = wx.StaticText( parents_box.GetStaticBox(), wx.ID_ANY, u"Father", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.father_name.Wrap( -1 )

		parents_box.Add( self.father_name, 0, wx.ALL, 5 )

		self.father_id = wx.TextCtrl( parents_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		parents_box.Add( self.father_id, 0, wx.ALL, 5 )

		self.mother_name = wx.StaticText( parents_box.GetStaticBox(), wx.ID_ANY, u"Mother", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mother_name.Wrap( -1 )

		parents_box.Add( self.mother_name, 0, wx.ALL, 5 )

		self.mother_id = wx.TextCtrl( parents_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		parents_box.Add( self.mother_id, 0, wx.ALL, 5 )


		gbSizer1.Add( parents_box, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		traitlist_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"traitlist" ), wx.VERTICAL )


		gbSizer1.Add( traitlist_box, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer15.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer15.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer15.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )

		self.m_spinCtrl4 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer15.Add( self.m_spinCtrl4, 0, wx.ALL, 5 )

		self.m_spinCtrl5 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer15.Add( self.m_spinCtrl5, 0, wx.ALL, 5 )

		self.m_spinCtrl6 = wx.SpinCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer15.Add( self.m_spinCtrl6, 0, wx.ALL, 5 )


		gbSizer1.Add( sbSizer15, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		sbSizer12.Add( gbSizer1, 1, wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.Output_ret = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, u"1414076 = { #character to link 大延琳\n\tdynasty = 1000049543 #Balhae Dae\n\tname = \"Geom\"\n\tculture = bohai\n\treligion = buddhist\n\tfather = 1414068 #unknown but possible\n\ttrait = mahayana_buddhist\n\t#Birth and death dates unknown\n\t938.1.1={\n\t\tbirth=yes\n\t}\n\t925.12.28 = { effect = { imprison = 194325 } }\n\t926.9.6 = { employer = 194326 }\n\t975.1.1={\n\t\tdeath=yes\n\t}\n}", wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer13.Add( self.Output_ret, 0, wx.ALL, 5 )


		sbSizer12.Add( sbSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


