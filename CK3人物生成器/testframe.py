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
from 人物生成器test1 import *
import testDialog
dynasty_Choices_number = [ u"dynasty01", u"dynasty02" ]
houseList = [
	["无分家", u"宗族1家族1", u"宗族1家族2"],# 宗族1
	["无分家",u"宗族2家族1", u"宗族2家族2"] # 宗族2
]
houseList_number =[
	[None,u"宗族1家族1", u"宗族1家族2"],# 宗族1
	[None,u"宗族2家族1", u"宗族2家族2"] # 宗族2
]

cultureGroupList = [ u"中原", u"胡人" ]

cultureList = [
	["无文化分支","东邪", "西毒",'南帝','北丐' ],# 中原
	["无文化分支","匈奴","鲜卑","羯","羌","氐"] # 胡人
]
cultureList_number = [
	[None,"东邪", "西毒",'南帝','北丐'],# 中原
	[None,"匈奴","鲜卑","羯","羌","氐"] # 胡人
]
religionGroupList = [ u"道教", u"佛教", u"儒家" ]

religionList = [# TODO 从文件读取 _adj
	["无信仰分支","正一派", "上清派",'全真派' ],# taoism_religion:0 "道教"
	["无信仰分支","阿利僧派","上座部佛教","大乘佛教","金刚乘佛教","藏传佛教"], # 佛教
	["无信仰分支","理学", "新学",'心学','经学','攘夷派' ]# 儒家
]
religionList_number = [
	[None,"zhengyi", "shangqing",'quanzhen'],# taoism_religion:0 "道教"
	[None,"ari","theravada","mahayana","vajrayana","lamaism"], # 佛教
	[None,"lixue", "jingshi",'xinxue','jingxue','rangyi']# 儒家
]
nicknameList_number = ["nickname1","nickname2"]
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CK3人物生成器", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		self.newChar = Person()

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		ID_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"ID" ), wx.VERTICAL )

		self.ID_textCtrl = wx.TextCtrl( ID_box.GetStaticBox(), wx.ID_ANY, u"000001", wx.DefaultPosition, wx.DefaultSize, 0 )
		ID_box.Add( self.ID_textCtrl, 0, wx.ALL, 5 )


		gbSizer1.Add( ID_box, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		dynasty_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"dynasty" ), wx.VERTICAL )

		dynasty_choiceChoices = [ u"宗族1", u"宗族2" ]
		self.dynasty_choice = wx.Choice( dynasty_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dynasty_choiceChoices, 0 )
		self.dynasty_choice.SetSelection( 0 )
		self.dynasty_choice.SetToolTip( u"王朝" )

		dynasty_box.Add( self.dynasty_choice, 0, wx.ALL, 5 )

		house_choiceChoices = houseList[0]
		self.house_choice = wx.Choice( dynasty_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, house_choiceChoices, 0 )
		self.house_choice.SetSelection( 0 )
		self.house_choice.SetToolTip( u"家族" )

		dynasty_box.Add( self.house_choice, 0, wx.ALL, 5 )

		self.edit_dynasty_and_house_button4 = wx.Button( dynasty_box.GetStaticBox(), wx.ID_ANY, u"编辑宗族家族", wx.DefaultPosition, wx.DefaultSize, 0 )
		dynasty_box.Add( self.edit_dynasty_and_house_button4, 0, wx.ALL, 5 )


		gbSizer1.Add( dynasty_box, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		Name_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Name" ), wx.VERTICAL )

		name_comboBoxChoices = [ u"名字1", u"nametest" ]
		self.name_comboBox = wx.ComboBox( Name_box.GetStaticBox(), wx.ID_ANY, u"<-请输入或选择->", wx.DefaultPosition, wx.DefaultSize, name_comboBoxChoices, 0 )
		Name_box.Add( self.name_comboBox, 0, wx.ALL, 5 )


		gbSizer1.Add( Name_box, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		culture_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"culture" ), wx.VERTICAL )

		cultureGroup_listBoxChoices = cultureGroupList
		self.cultureGroup_listBox = wx.ListBox( culture_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cultureGroup_listBoxChoices, 0 )
		self.cultureGroup_listBox.SetSelection(0)
		culture_box.Add( self.cultureGroup_listBox, 0, wx.ALL, 5 )

		culture_listBoxChoices = cultureList[0]
		self.culture_listBox = wx.ListBox( culture_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, culture_listBoxChoices, 0 )
		self.culture_listBox.SetSelection(0)
		culture_box.Add( self.culture_listBox, 0, wx.ALL, 5 )


		gbSizer1.Add( culture_box, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		religion_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"religion" ), wx.VERTICAL )

		religionGroup_listBoxChoices = religionGroupList
		self.religionGroup_listBox = wx.ListBox( religion_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, religionGroup_listBoxChoices, 0 )
		self.religionGroup_listBox.SetSelection(0)
		religion_box.Add( self.religionGroup_listBox, 0, wx.ALL, 5 )

		religion_listBoxChoices = religionList[0]
		self.religion_listBox = wx.ListBox( religion_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, religion_listBoxChoices, 0 )
		self.religion_listBox.SetSelection(0)
		religion_box.Add( self.religion_listBox, 0, wx.ALL, 5 )
		# TODO 加入图标
		# self.m_bcomboBox1 = wx.adv.BitmapComboBox( religion_box.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 )
		# religion_box.Add( self.m_bcomboBox1, 0, wx.ALL, 5 )

		gbSizer1.Add( religion_box, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		birthday_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"birthday" ), wx.HORIZONTAL )

		self.birthday_year_textCtrl = wx.TextCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, u"867", wx.DefaultPosition, wx.DefaultSize, 0 )
		birthday_box.Add( self.birthday_year_textCtrl, 0, wx.ALL, 5 )

		self.birthday_month_textCtrl = wx.TextCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		birthday_box.Add( self.birthday_month_textCtrl, 0, wx.ALL, 5 )

		self.birthday_day_textCtrl = wx.TextCtrl( birthday_box.GetStaticBox(), wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		birthday_box.Add( self.birthday_day_textCtrl, 0, wx.ALL, 5 )


		gbSizer1.Add( birthday_box, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )

		deathday_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"deathday" ), wx.HORIZONTAL )

		self.deathday_year_textCtrl = wx.TextCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, u"1444", wx.DefaultPosition, wx.DefaultSize, 0 )
		deathday_box.Add( self.deathday_year_textCtrl, 0, wx.ALL, 5 )

		self.deathday_month_textCtrl = wx.TextCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		deathday_box.Add( self.deathday_month_textCtrl, 0, wx.ALL, 5 )

		self.deathday_day_textCtrl = wx.TextCtrl( deathday_box.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		deathday_box.Add( self.deathday_day_textCtrl, 0, wx.ALL, 5 )


		gbSizer1.Add( deathday_box, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )

		eventlist_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"eventlist" ), wx.VERTICAL )

		self.eventlist_button = wx.Button( eventlist_box.GetStaticBox(), wx.ID_ANY, u"也以后添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		eventlist_box.Add( self.eventlist_button, 0, wx.ALL, 5 )


		gbSizer1.Add( eventlist_box, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		parents_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"parents" ), wx.VERTICAL )

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

		traitlist_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"traitlist" ), wx.VERTICAL )

		self.traitlist_button = wx.Button( traitlist_box.GetStaticBox(), wx.ID_ANY, u"以后添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		traitlist_box.Add( self.traitlist_button, 0, wx.ALL, 5 )


		gbSizer1.Add( traitlist_box, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		skills_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"能力" ), wx.HORIZONTAL )

		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )

		self.diplomacy_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"外交", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.diplomacy_checkBox, 0, wx.ALL, 5 )

		self.martial_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"军事", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.martial_checkBox, 0, wx.ALL, 5 )

		self.stewardship_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"财政", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.stewardship_checkBox, 0, wx.ALL, 5 )

		self.intrigue_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"密谋", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.intrigue_checkBox, 0, wx.ALL, 5 )

		self.learning_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"学识", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.learning_checkBox, 0, wx.ALL, 5 )

		self.prowess_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"勇武", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.prowess_checkBox, 0, wx.ALL, 5 )

		self.fertility_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"生育率", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizer2.Add( self.fertility_checkBox, 0, wx.ALL, 5 )

		self.health_checkBox = wx.CheckBox( skills_box.GetStaticBox(), wx.ID_ANY, u"健康", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.health_checkBox, 0, wx.ALL, 5 )


		skills_box.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

		self.diplomacy_spinCtrl = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 2 )
		self.diplomacy_spinCtrl.Enable( False )

		gSizer1.Add( self.diplomacy_spinCtrl, 0, wx.ALL, 5 )

		self.martial_spinCtrl = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 2 )
		self.martial_spinCtrl.Enable( False )

		gSizer1.Add( self.martial_spinCtrl, 0, wx.ALL, 5 )

		self.stewardship_spinCtrl = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.stewardship_spinCtrl.Enable( False )

		gSizer1.Add( self.stewardship_spinCtrl, 0, wx.ALL, 5 )

		self.intrigue_spinCtrl = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.intrigue_spinCtrl.Enable( False )

		gSizer1.Add( self.intrigue_spinCtrl, 0, wx.ALL, 5 )

		self.learning_spinCtrl = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.learning_spinCtrl.Enable( False )

		gSizer1.Add( self.learning_spinCtrl, 0, wx.ALL, 5 )

		self.prowess_spinCtrl = wx.SpinCtrl( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.prowess_spinCtrl.Enable( False )

		gSizer1.Add( self.prowess_spinCtrl, 0, wx.ALL, 5 )

		self.fertility_spinCtrlDouble = wx.SpinCtrlDouble( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.fertility_spinCtrlDouble.SetDigits( 0 )
		self.fertility_spinCtrlDouble.Enable( False )

		gSizer1.Add( self.fertility_spinCtrlDouble, 0, wx.ALL, 5 )

		self.health_spinCtrlDouble = wx.SpinCtrlDouble( skills_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.health_spinCtrlDouble.SetDigits( 0 )
		self.health_spinCtrlDouble.Enable( False )

		gSizer1.Add( self.health_spinCtrlDouble, 0, wx.ALL, 5 )


		skills_box.Add( gSizer1, 1, wx.EXPAND, 5 )


		gbSizer1.Add( skills_box, wx.GBPosition( 0, 2 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )

		DNA_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"DNA" ), wx.VERTICAL )

		self.DNA_Text = wx.StaticText( DNA_box.GetStaticBox(), wx.ID_ANY, u"TODO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DNA_Text.Wrap( -1 )

		DNA_box.Add( self.DNA_Text, 0, wx.ALL, 5 )

		self.DNA_toggleBtn = wx.ToggleButton( DNA_box.GetStaticBox(), wx.ID_ANY, u"以后制作", wx.DefaultPosition, wx.DefaultSize, 0 )
		DNA_box.Add( self.DNA_toggleBtn, 0, wx.ALL, 5 )


		gbSizer1.Add( DNA_box, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		nickname_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nickname" ), wx.VERTICAL )

		nickname_choiceChoices = [ u"昵称1", u"昵称2", u"昵称3" ]
		self.nickname_choice = wx.Choice( nickname_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, nickname_choiceChoices, 0 )
		self.nickname_choice.SetSelection( 0 )
		nickname_box.Add( self.nickname_choice, 0, wx.ALL, 5 )

		sexuality_choiceChoices = [ u"asexual", u"heterosexual", u"homosexual", u"bisexual" ]
		self.sexuality_choice = wx.Choice( nickname_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sexuality_choiceChoices, 0 )
		self.sexuality_choice.SetSelection( 1 )
		nickname_box.Add( self.sexuality_choice, 0, wx.ALL, 5 )


		gbSizer1.Add( nickname_box, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		result_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"参数验证结果" ), wx.VERTICAL )

		self.result_text = wx.StaticText( result_box.GetStaticBox(), wx.ID_ANY, u"无事发生", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.result_text.Wrap( -1 )

		result_box.Add( self.result_text, 0, wx.ALL, 5 )


		gbSizer1.Add( result_box, wx.GBPosition( 2, 2 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )

		misc_box1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"杂项" ), wx.VERTICAL )

		self.isFemale_checkBox1 = wx.CheckBox( misc_box1.GetStaticBox(), wx.ID_ANY, u"是女性", wx.DefaultPosition, wx.DefaultSize, 0 )
		misc_box1.Add( self.isFemale_checkBox1, 0, wx.ALL, 5 )

		self.disallow_random_traits_checkBox = wx.CheckBox( misc_box1.GetStaticBox(), wx.ID_ANY, u"禁止随机特质", wx.DefaultPosition, wx.DefaultSize, 0 )
		misc_box1.Add( self.disallow_random_traits_checkBox, 0, wx.ALL, 5 )


		gbSizer1.Add( misc_box1, wx.GBPosition( 0, 3 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.HORIZONTAL )

		self.Output_ret = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, u"1414076 = { #character to link 大延琳\n\tdynasty = 1000049543 #Balhae Dae\n\tname = \"Geom\"\n\tculture = bohai\n\treligion = buddhist\n\tfather = 1414068 #unknown but possible\n\ttrait = mahayana_buddhist\n\t#Birth and death dates unknown\n\t938.1.1={\n\t\tbirth=yes\n\t}\n\t925.12.28 = { effect = { imprison = 194325 } }\n\t926.9.6 = { employer = 194326 }\n\t975.1.1={\n\t\tdeath=yes\n\t}\n}", wx.DefaultPosition, wx.Size( 500,200 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer13.Add( self.Output_ret, 0, wx.ALL, 5 )

		self.output_button = wx.Button( sbSizer13.GetStaticBox(), wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer13.Add( self.output_button, 0, wx.ALL, 5 )


		gbSizer1.Add( sbSizer13, wx.GBPosition( 4, 2 ), wx.GBSpan( 3, 1 ), wx.EXPAND, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()
		gbSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.dynasty_choice.Bind( wx.EVT_CHOICE, self.Change_house )
		self.edit_dynasty_and_house_button4.Bind( wx.EVT_BUTTON, self.EditDynastyAndHouse )
		self.cultureGroup_listBox.Bind( wx.EVT_LISTBOX, self.Change_culturelist )
		self.religionGroup_listBox.Bind( wx.EVT_LISTBOX, self.Change_religionlist )
		self.traitlist_button.Bind( wx.EVT_BUTTON, self.OpenTraitDial )
		self.diplomacy_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_diplomacy )
		self.martial_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_martial )
		self.stewardship_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_stewardship )
		self.intrigue_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_intrigue )
		self.learning_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_learning )
		self.prowess_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_prowess )
		self.fertility_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_fertility )
		self.health_checkBox.Bind( wx.EVT_CHECKBOX, self.Check_health )
		self.DNA_toggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.Check_DNA )
		self.output_button.Bind( wx.EVT_BUTTON, self.createCode )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Change_house( self, event ):
		self.house_choice.SetItems(houseList[self.dynasty_choice.GetSelection()])
		self.house_choice.SetSelection(0)
		# self.Layout()
		event.Skip()
		
	def EditDynastyAndHouse( self, event ):
		event.Skip()

	def Change_culturelist( self, event ):
		self.culture_listBox.SetItems(cultureList[self.cultureGroup_listBox.GetSelection()])
		self.culture_listBox.SetSelection(0)
		event.Skip()

	def Change_religionlist( self, event ):
		self.religion_listBox.SetItems(religionList[self.religionGroup_listBox.GetSelection()])
		self.religion_listBox.SetSelection(0)
		event.Skip()

	def OpenTraitDial( self, event ):
		dial = testDialog.trait_dialog(self, self.newChar)
		# dial.m_staticText5.SetLabelText('试一试')
		dial.Show()
		event.Skip()

	def Check_diplomacy( self, event ):
		if self.diplomacy_checkBox.GetValue():
			self.diplomacy_spinCtrl.Enable()
		else:
			self.diplomacy_spinCtrl.Disable()
		event.Skip()

	def Check_martial( self, event ):
		if self.martial_checkBox.GetValue():
			self.martial_spinCtrl.Enable()
		else:
			self.martial_spinCtrl.Disable()
		event.Skip()

	def Check_stewardship( self, event ):
		if self.stewardship_checkBox.GetValue():
			self.stewardship_spinCtrl.Enable()
		else:
			self.stewardship_spinCtrl.Disable()
		event.Skip()
		
	def Check_intrigue( self, event ):
		if self.intrigue_checkBox.GetValue():
			self.intrigue_spinCtrl.Enable()
		else:
			self.intrigue_spinCtrl.Disable()
		event.Skip()

	def Check_learning( self, event ):
		if self.learning_checkBox.GetValue():
			self.learning_spinCtrl.Enable()
		else:
			self.learning_spinCtrl.Disable()
		event.Skip()

	def Check_prowess( self, event ):
		if self.prowess_checkBox.GetValue():
			self.prowess_spinCtrl.Enable()
		else:
			self.prowess_spinCtrl.Disable()
		event.Skip()

	def Check_fertility( self, event ):
		if self.fertility_checkBox.GetValue():
			self.fertility_spinCtrlDouble.Enable()
		else:
			self.fertility_spinCtrlDouble.Disable()
		event.Skip()

	def Check_health( self, event ):
		if self.health_checkBox.GetValue():
			self.health_spinCtrlDouble.Enable()
		else:
			self.health_spinCtrlDouble.Disable()
		event.Skip()

	def Check_DNA( self, event ):
		event.Skip()

	def createCode( self, event ):
		self.newChar.id=self.ID_textCtrl.GetValue().lstrip('0')
		self.newChar.name = self.name_comboBox.GetValue()
		self.newChar.dynasty=dynasty_Choices_number[self.dynasty_choice.GetSelection()]
		self.newChar.house=houseList_number[self.dynasty_choice.GetSelection()][self.house_choice.GetSelection()]
		self.newChar.culture=cultureList_number[self.cultureGroup_listBox.GetSelection()][self.culture_listBox.GetSelection()]
		self.newChar.religion=religionList_number[self.religionGroup_listBox.GetSelection()][self.religion_listBox.GetSelection()]

		self.newChar.diplomacy=self.diplomacy_spinCtrl.GetValue() if self.diplomacy_checkBox.GetValue() else None
		self.newChar.martial=self.martial_spinCtrl.GetValue() if self.martial_checkBox.GetValue() else None
		self.newChar.stewardship=self.stewardship_spinCtrl.GetValue() if self.stewardship_checkBox.GetValue() else None
		self.newChar.intrigue=self.intrigue_spinCtrl.GetValue() if self.intrigue_checkBox.GetValue() else None
		self.newChar.learning=self.learning_spinCtrl.GetValue() if self.learning_checkBox.GetValue() else None
		self.newChar.prowess=self.prowess_spinCtrl.GetValue() if self.prowess_checkBox.GetValue() else None

		self.newChar.fertility =self.fertility_spinCtrlDouble.GetValue() if self.fertility_checkBox.GetValue() else None
		self.newChar.health=self.health_spinCtrlDouble.GetValue() if self.health_checkBox.GetValue() else None

		self.newChar.father=self.father_id.GetValue() if (self.father_id.GetValue()!='爸爸ID' and self.father_id.GetValue()!='') else None
		self.newChar.mother=self.mother_id.GetValue() if (self.mother_id.GetValue()!='妈妈ID' and self.mother_id.GetValue()!='') else None

		self.Output_ret.SetValue(str(self.newChar))
		self.result_text.SetLabelText("生成")
		# if self.m_textCtrl5.GetValidator().Validate(self.m_textCtrl5):
		birthday = CK3_Date(str(self.birthday_year_textCtrl.GetValue()+"."+self.birthday_month_textCtrl.GetValue()+"."+self.birthday_day_textCtrl.GetValue()))
		deathday = CK3_Date(str(self.deathday_year_textCtrl.GetValue()+"."+self.deathday_month_textCtrl.GetValue()+"."+self.deathday_day_textCtrl.GetValue()))
		check_str = ''''''
		if birthday.check_period():
			check_str += ""
		else:
			check_str += "时间不在CK3范围内\n"
		if birthday>deathday:
			check_str += "生日晚于忌日\n"
		self.result_text.SetLabelText(check_str)
		self.newChar.eventhistory.clear()
		self.newChar.set_event_detail(birthday,Eventdetail("birth","yes"))
		self.newChar.set_event_detail(deathday,Eventdetail("death","yes"))
		# if self.religion_listBox1.IsShown():
		# 	self.religion_listBox1.Hide()
		# elif not self.religion_listBox1.IsShown():
		# 	self.religion_listBox1.Show()
		self.Output_ret.SetValue(str(self.newChar))
		event.Skip()


if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()

    main_win = MyFrame1(None)
    main_win.Show()

    app.MainLoop()