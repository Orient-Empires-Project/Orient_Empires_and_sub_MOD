///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxStaticBoxSizer* sbSizer12;
	sbSizer12 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("label") ), wxVERTICAL );

	wxGridBagSizer* gbSizer1;
	gbSizer1 = new wxGridBagSizer( 0, 0 );
	gbSizer1->SetFlexibleDirection( wxBOTH );
	gbSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );

	wxStaticBoxSizer* ID_box;
	ID_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("ID") ), wxVERTICAL );

	ID_textCtrl1 = new wxTextCtrl( ID_box->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	ID_box->Add( ID_textCtrl1, 0, wxALL, 5 );


	gbSizer1->Add( ID_box, wxGBPosition( 0, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* dynasty_box;
	dynasty_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("dynasty") ), wxVERTICAL );

	wxString dynasty_choice1Choices[] = { wxT("王朝1"), wxT("王朝2") };
	int dynasty_choice1NChoices = sizeof( dynasty_choice1Choices ) / sizeof( wxString );
	dynasty_choice1 = new wxChoice( dynasty_box->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, dynasty_choice1NChoices, dynasty_choice1Choices, 0 );
	dynasty_choice1->SetSelection( 0 );
	dynasty_choice1->SetToolTip( wxT("王朝") );

	dynasty_box->Add( dynasty_choice1, 0, wxALL, 5 );


	gbSizer1->Add( dynasty_box, wxGBPosition( 1, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* Name_box;
	Name_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("Name") ), wxVERTICAL );

	m_comboBox1 = new wxComboBox( Name_box->GetStaticBox(), wxID_ANY, wxT("<-请输入或选择->"), wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	m_comboBox1->Append( wxT("名字1") );
	m_comboBox1->Append( wxT("nametest") );
	Name_box->Add( m_comboBox1, 0, wxALL, 5 );


	gbSizer1->Add( Name_box, wxGBPosition( 2, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* culture_box;
	culture_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("culture") ), wxVERTICAL );

	m_listBox2 = new wxListBox( culture_box->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	culture_box->Add( m_listBox2, 0, wxALL, 5 );


	gbSizer1->Add( culture_box, wxGBPosition( 3, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* religion_box;
	religion_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("religion") ), wxVERTICAL );

	religion_listBox1 = new wxListBox( religion_box->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 );
	religion_listBox1->Append( wxT("道教") );
	religion_listBox1->Append( wxT("佛教") );
	religion_listBox1->Append( wxT("儒教") );
	religion_box->Add( religion_listBox1, 0, wxALL, 5 );


	gbSizer1->Add( religion_box, wxGBPosition( 4, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* birthday_box;
	birthday_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("birthday") ), wxVERTICAL );

	m_datePicker4 = new wxDatePickerCtrl( birthday_box->GetStaticBox(), wxID_ANY, wxDefaultDateTime, wxDefaultPosition, wxDefaultSize, wxDP_DROPDOWN|wxDP_SHOWCENTURY );
	birthday_box->Add( m_datePicker4, 0, wxALL, 5 );


	gbSizer1->Add( birthday_box, wxGBPosition( 5, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* deathday_box;
	deathday_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("deathday") ), wxVERTICAL );

	m_datePicker1 = new wxDatePickerCtrl( deathday_box->GetStaticBox(), wxID_ANY, wxDefaultDateTime, wxDefaultPosition, wxDefaultSize, wxDP_DEFAULT );
	deathday_box->Add( m_datePicker1, 0, wxALL, 5 );


	gbSizer1->Add( deathday_box, wxGBPosition( 6, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* eventlist_box;
	eventlist_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("eventlist") ), wxVERTICAL );


	gbSizer1->Add( eventlist_box, wxGBPosition( 7, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* parents_box;
	parents_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("parents") ), wxVERTICAL );

	father_name = new wxStaticText( parents_box->GetStaticBox(), wxID_ANY, wxT("Father"), wxDefaultPosition, wxDefaultSize, 0 );
	father_name->Wrap( -1 );
	parents_box->Add( father_name, 0, wxALL, 5 );

	father_id = new wxTextCtrl( parents_box->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	parents_box->Add( father_id, 0, wxALL, 5 );

	mother_name = new wxStaticText( parents_box->GetStaticBox(), wxID_ANY, wxT("Mother"), wxDefaultPosition, wxDefaultSize, 0 );
	mother_name->Wrap( -1 );
	parents_box->Add( mother_name, 0, wxALL, 5 );

	mother_id = new wxTextCtrl( parents_box->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	parents_box->Add( mother_id, 0, wxALL, 5 );


	gbSizer1->Add( parents_box, wxGBPosition( 1, 1 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* traitlist_box;
	traitlist_box = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("traitlist") ), wxVERTICAL );


	gbSizer1->Add( traitlist_box, wxGBPosition( 2, 1 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer15;
	sbSizer15 = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("label") ), wxVERTICAL );

	m_spinCtrl1 = new wxSpinCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 0, 10, 0 );
	sbSizer15->Add( m_spinCtrl1, 0, wxALL, 5 );

	m_spinCtrl2 = new wxSpinCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 0, 10, 0 );
	sbSizer15->Add( m_spinCtrl2, 0, wxALL, 5 );

	m_spinCtrl3 = new wxSpinCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 0, 10, 0 );
	sbSizer15->Add( m_spinCtrl3, 0, wxALL, 5 );

	m_spinCtrl4 = new wxSpinCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 0, 10, 0 );
	sbSizer15->Add( m_spinCtrl4, 0, wxALL, 5 );

	m_spinCtrl5 = new wxSpinCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 0, 10, 0 );
	sbSizer15->Add( m_spinCtrl5, 0, wxALL, 5 );

	m_spinCtrl6 = new wxSpinCtrl( sbSizer15->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 0, 10, 0 );
	sbSizer15->Add( m_spinCtrl6, 0, wxALL, 5 );


	gbSizer1->Add( sbSizer15, wxGBPosition( 0, 2 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );


	sbSizer12->Add( gbSizer1, 1, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer13;
	sbSizer13 = new wxStaticBoxSizer( new wxStaticBox( sbSizer12->GetStaticBox(), wxID_ANY, wxT("label") ), wxVERTICAL );

	Output_ret = new wxTextCtrl( sbSizer13->GetStaticBox(), wxID_ANY, wxT("1414076 = { #character to link 大延琳\n\tdynasty = 1000049543 #Balhae Dae\n\tname = \"Geom\"\n\tculture = bohai\n\treligion = buddhist\n\tfather = 1414068 #unknown but possible\n\ttrait = mahayana_buddhist\n\t#Birth and death dates unknown\n\t938.1.1={\n\t\tbirth=yes\n\t}\n\t925.12.28 = { effect = { imprison = 194325 } }\n\t926.9.6 = { employer = 194326 }\n\t975.1.1={\n\t\tdeath=yes\n\t}\n}"), wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxTE_MULTILINE|wxTE_READONLY );
	sbSizer13->Add( Output_ret, 0, wxALL, 5 );


	sbSizer12->Add( sbSizer13, 1, wxEXPAND, 5 );


	this->SetSizer( sbSizer12 );
	this->Layout();

	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
}
