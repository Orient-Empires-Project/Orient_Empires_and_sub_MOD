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

trait_education_dict = {
	'education_intrigue_1':"业余阴谋家",   'education_intrigue_2':"浮夸的欺诈师",  'education_intrigue_3':"暗中策划者",     'education_intrigue_4':"难以捉摸的影子",
	'education_diplomacy_1':"天真的绥靖者",'education_diplomacy_2':"合格的谈判者", 'education_diplomacy_3':"魅力非凡的说客", 'education_diplomacy_4':"幕后操控人",
	'education_stewardship_1':"放荡的浪子",'education_stewardship_2':"节俭的职员", 'education_stewardship_3':"财富创造者",  'education_stewardship_4':"点石成金者",
	'education_martial_1':"鲁莽的战士",    'education_martial_2':"坚强的战士",     'education_martial_3':"优秀战术家",      'education_martial_4':"天才军事家",
	'education_learning_1':"尽责的书吏",   'education_learning_2':"有见地的思想家",'education_learning_3':"明睿的智者",      'education_learning_4':"哲学大师"
}

trait_education_list = list(trait_education_dict.keys())
trait_education_list_str = list(trait_education_dict.values())

class trait_dialog ( wx.Dialog ):

	def __init__( self, parent , newChar):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"特性列表", pos = wx.DefaultPosition, size = wx.Size( 194,276 ), style = wx.DEFAULT_DIALOG_STYLE )
		self.newChar = newChar
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.TODO_staticText = wx.StaticText( self, wx.ID_ANY, u"以后再做", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TODO_staticText.Wrap( -1 )

		bSizer1.Add( self.TODO_staticText, 0, wx.ALL, 5 )

		Education_Traits_choiceChoices =trait_education_list_str# [ u"教育特质1", u"教育特质" ]
		self.Education_Traits_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Education_Traits_choiceChoices, 0 )
		self.Education_Traits_choice.SetSelection( 0 )
		for item in trait_education_list:
			if item in self.newChar.traitlist:
				self.Education_Traits_choice.SetSelection( trait_education_list.index(item) )
		bSizer1.Add( self.Education_Traits_choice, 0, wx.ALL, 5 )

		Lifestyle_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Lifestyle_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Lifestyle_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Lifestyle_Traits_listBox, 0, wx.ALL, 5 )

		Personality_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Personality_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Personality_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Personality_Traits_listBox, 0, wx.ALL, 5 )

		Stress_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Stress_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Stress_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Stress_Traits_listBox, 0, wx.ALL, 5 )

		Health_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Health_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Health_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Health_Traits_listBox, 0, wx.ALL, 5 )

		Physical_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Physical_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Physical_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Physical_Traits_listBox, 0, wx.ALL, 5 )

		Fame_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Fame_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Fame_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Fame_Traits_listBox, 0, wx.ALL, 5 )

		Revolting_Leader_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Revolting_Leader_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Revolting_Leader_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Revolting_Leader_Traits_listBox, 0, wx.ALL, 5 )

		Commander_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.Commander_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Commander_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.Commander_Traits_listBox, 0, wx.ALL, 5 )

		State_Traits_listBoxChoices = [ u"特质1", u"特质2" ]
		self.State_Traits_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, State_Traits_listBoxChoices, wx.LB_MULTIPLE )
		bSizer1.Add( self.State_Traits_listBox, 0, wx.ALL, 5 )

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
		bSizer1.Fit( self )

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
		self.newChar.traitlist.add(trait_education_list[self.Education_Traits_choice.GetSelection()])
		event.Skip()


