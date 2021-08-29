///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/textctrl.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/sizer.h>
#include <wx/statbox.h>
#include <wx/choice.h>
#include <wx/combobox.h>
#include <wx/listbox.h>
#include <wx/datectrl.h>
#include <wx/dateevt.h>
#include <wx/stattext.h>
#include <wx/spinctrl.h>
#include <wx/gbsizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame1
///////////////////////////////////////////////////////////////////////////////
class MyFrame1 : public wxFrame
{
	private:

	protected:
		wxTextCtrl* ID_textCtrl1;
		wxChoice* dynasty_choice1;
		wxComboBox* m_comboBox1;
		wxListBox* m_listBox2;
		wxListBox* religion_listBox1;
		wxDatePickerCtrl* m_datePicker4;
		wxDatePickerCtrl* m_datePicker1;
		wxStaticText* father_name;
		wxTextCtrl* father_id;
		wxStaticText* mother_name;
		wxTextCtrl* mother_id;
		wxSpinCtrl* m_spinCtrl1;
		wxSpinCtrl* m_spinCtrl2;
		wxSpinCtrl* m_spinCtrl3;
		wxSpinCtrl* m_spinCtrl4;
		wxSpinCtrl* m_spinCtrl5;
		wxSpinCtrl* m_spinCtrl6;
		wxTextCtrl* Output_ret;

	public:

		MyFrame1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("CK3人物生成器"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1210,1071 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~MyFrame1();

};

