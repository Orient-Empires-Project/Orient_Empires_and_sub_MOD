# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
from wx.core import TextCtrl
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################
from 人物生成器test1 import *

class MyBirthdayValidator(wx.Validator):
	def __init__(self, parent ):
		super().__init__(parent)# TODO ???

	def Clone(self):
		return MyBirthdayValidator()

	def Validate(self):
		# super().Validate()
		TextCtrl= self.GetWindow()
		text = TextCtrl.GetValue()
		if int(text)>=800 and int(text)<=1444:
			return True
		else:
			return False

	
	def TransferToWindow(self):
		return True

	def TransferFromWindow(self):
		return True

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CK3人物生成器", pos = wx.DefaultPosition, size = wx.Size( 1210,1071 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL )
		self.newChar = Person()
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		ID_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"ID" ), wx.VERTICAL )

		self.ID_textCtrl1 = wx.TextCtrl( ID_box.GetStaticBox(), wx.ID_ANY, u"000001", wx.DefaultPosition, wx.DefaultSize, 0 )
		ID_box.Add( self.ID_textCtrl1, 0, wx.ALL, 5 )


		gbSizer1.Add( ID_box, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		dynasty_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"dynasty" ), wx.VERTICAL )

		dynasty_choice1Choices = [ u"宗族1", u"宗族2" ]
		self.dynasty_choice1 = wx.Choice( dynasty_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dynasty_choice1Choices, 0 )
		self.dynasty_choice1.SetSelection( 0 )
		self.dynasty_choice1.SetToolTip( u"王朝" )

		dynasty_box.Add( self.dynasty_choice1, 0, wx.ALL, 5 )

		house_choice4Choices = [ u"家族1", u"家族2", u"家族1" ]
		self.house_choice4 = wx.Choice( dynasty_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, house_choice4Choices, 0 )
		self.house_choice4.SetSelection( 0 )
		self.house_choice4.SetToolTip( u"家族" )

		dynasty_box.Add( self.house_choice4, 0, wx.ALL, 5 )


		gbSizer1.Add( dynasty_box, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		Name_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Name" ), wx.VERTICAL )

		m_comboBox1Choices = [ u"名字1", u"nametest" ]
		self.m_comboBox1 = wx.ComboBox( Name_box.GetStaticBox(), wx.ID_ANY, u"<-请输入或选择->", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		Name_box.Add( self.m_comboBox1, 0, wx.ALL, 5 )


		gbSizer1.Add( Name_box, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		culture_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"culture" ), wx.VERTICAL )

		m_listBox2Choices = [ u"中原", u"胡人" ]
		self.m_listBox2 = wx.ListBox( culture_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		culture_box.Add( self.m_listBox2, 0, wx.ALL, 5 )

		self.culture_tree = wx.TreeCtrl( culture_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT )
		root = self.culture_tree.AddRoot(u"文化")
		zhongyuan = self.culture_tree.AppendItem(root, u"中原")
		self.culture_tree.AppendItem(zhongyuan, u"长安")
		self.culture_tree.AppendItem(zhongyuan, u"洛阳")
		huren = self.culture_tree.AppendItem(root, u"胡人")
		culture_box.Add( self.culture_tree, 0, wx.ALL, 5 )


		gbSizer1.Add( culture_box, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		religion_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"religion" ), wx.VERTICAL )

		religion_listBox1Choices = [ u"道教", u"佛教", u"儒教" ]
		self.religion_listBox1 = wx.ListBox( religion_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, religion_listBox1Choices, 0 )
		religion_box.Add( self.religion_listBox1, 0, wx.ALL, 5 )


		gbSizer1.Add( religion_box, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		birthday_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"birthday" ), wx.HORIZONTAL )

		self.m_textCtrl5 = wx.TextCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, u"867", wx.DefaultPosition, wx.DefaultSize, 0)
		# self.m_textCtrl5.SetValidator(MyBirthdayValidator)
		birthday_box.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		birthday_box.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		birthday_box.Add( self.m_textCtrl7, 0, wx.ALL, 5 )


		gbSizer1.Add( birthday_box, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )

		deathday_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"deathday" ), wx.HORIZONTAL )

		self.m_textCtrl8 = wx.TextCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, u"1444", wx.DefaultPosition, wx.DefaultSize, 0 )
		deathday_box.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		deathday_box.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		deathday_box.Add( self.m_textCtrl10, 0, wx.ALL, 5 )


		gbSizer1.Add( deathday_box, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )

		eventlist_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"eventlist" ), wx.VERTICAL )

		self.m_button4 = wx.Button( eventlist_box.GetStaticBox(), wx.ID_ANY, u"也以后添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		eventlist_box.Add( self.m_button4, 0, wx.ALL, 5 )


		gbSizer1.Add( eventlist_box, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		parents_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"parents" ), wx.VERTICAL )

		self.father_name = wx.StaticText( parents_box.GetStaticBox(), wx.ID_ANY, u"Father", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.father_name.Wrap( -1 )

		parents_box.Add( self.father_name, 0, wx.ALL, 5 )

		self.father_id = wx.TextCtrl( parents_box.GetStaticBox(), wx.ID_ANY, u"爸爸ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		parents_box.Add( self.father_id, 0, wx.ALL, 5 )

		self.mother_name = wx.StaticText( parents_box.GetStaticBox(), wx.ID_ANY, u"Mother", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mother_name.Wrap( -1 )

		parents_box.Add( self.mother_name, 0, wx.ALL, 5 )

		self.mother_id = wx.TextCtrl( parents_box.GetStaticBox(), wx.ID_ANY, u"妈妈ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		parents_box.Add( self.mother_id, 0, wx.ALL, 5 )


		gbSizer1.Add( parents_box, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		traitlist_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"traitlist" ), wx.VERTICAL )

		self.m_button2 = wx.Button( traitlist_box.GetStaticBox(), wx.ID_ANY, u"以后添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		traitlist_box.Add( self.m_button2, 0, wx.ALL, 5 )


		gbSizer1.Add( traitlist_box, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		skills_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"能力" ), wx.HORIZONTAL )

		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_checkBox1 = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"外交", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"财政", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"密谋", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"学识", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"勇武", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox6, 0, wx.ALL, 5 )


		skills_box.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_spinCtrl1 = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 1 )
		gSizer1.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 2 )
		gSizer1.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer1.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )

		self.m_spinCtrl4 = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer1.Add( self.m_spinCtrl4, 0, wx.ALL, 5 )

		self.m_spinCtrl5 = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer1.Add( self.m_spinCtrl5, 0, wx.ALL, 5 )

		self.m_spinCtrl6 = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer1.Add( self.m_spinCtrl6, 0, wx.ALL, 5 )


		skills_box.Add( gSizer1, 1, wx.EXPAND, 5 )


		gbSizer1.Add( skills_box, wx.GBPosition( 0, 2 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )

		DNA_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"DNA" ), wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( DNA_box.GetStaticBox(), wx.ID_ANY, u"TODO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		DNA_box.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( DNA_box.GetStaticBox(), wx.ID_ANY, u"Toggle me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		DNA_box.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )


		gbSizer1.Add( DNA_box, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		nickname_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Nickname" ), wx.VERTICAL )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( nickname_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		nickname_box.Add( self.m_choice3, 0, wx.ALL, 5 )


		gbSizer1.Add( nickname_box, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		result_box = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"结果" ), wx.VERTICAL )

		self.result_text = wx.StaticText( result_box.GetStaticBox(), wx.ID_ANY, u"无事发生", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.result_text.Wrap( -1 )

		result_box.Add( self.result_text, 0, wx.ALL, 5 )


		gbSizer1.Add( result_box, wx.GBPosition( 2, 2 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )


		sbSizer12.Add( gbSizer1, 1, wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"label" ), wx.HORIZONTAL )

		self.Output_ret = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, u"1414076 = { #character to link 大延琳\n\tdynasty = 1000049543 #Balhae Dae\n\tname = \"Geom\"\n\tculture = bohai\n\treligion = buddhist\n\tfather = 1414068 #unknown but possible\n\ttrait = mahayana_buddhist\n\t#Birth and death dates unknown\n\t938.1.1={\n\t\tbirth=yes\n\t}\n\t925.12.28 = { effect = { imprison = 194325 } }\n\t926.9.6 = { employer = 194326 }\n\t975.1.1={\n\t\tdeath=yes\n\t}\n}", wx.DefaultPosition, wx.Size( 500,200 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer13.Add( self.Output_ret, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( sbSizer13.GetStaticBox(), wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer13.Add( self.m_button1, 0, wx.ALL, 5 )


		sbSizer12.Add( sbSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.culture_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.getCulture )
		self.m_button1.Bind( wx.EVT_BUTTON, self.createCode )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def getCulture( self, event ):
		item = event.GetItem()
		self.newChar.culture=str(self.culture_tree.GetItemText(item))
		event.Skip()
	def createCode( self, event ):
		self.newChar.id=int(self.ID_textCtrl1.GetValue())
		dynasty_choice1Choices_number = [ u"1000001", u"1000002" ]
		self.newChar.dynasty=int(dynasty_choice1Choices_number[self.dynasty_choice1.GetSelection()])
		self.Output_ret.SetValue(str(self.newChar))
		self.result_text.SetLabelText("生成")
		# if self.m_textCtrl5.GetValidator().Validate(self.m_textCtrl5):
		print (self.m_textCtrl5.GetValue())
		print (int(self.m_textCtrl5.GetValue())>1444)
		if int(self.m_textCtrl5.GetValue())>1444 :
			self.result_text.SetLabelText("BAD")
		else:
			self.result_text.SetLabelText("GOOD")
		if self.religion_listBox1.IsShown():
			self.religion_listBox1.Hide()
		elif not self.religion_listBox1.IsShown():
			self.religion_listBox1.Show()
		self.religion_listBox1.GetParent().Layout()
		# self.Layout()
		event.Skip()


if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()

    main_win = MyFrame1(None)
    main_win.Show()

    app.MainLoop()