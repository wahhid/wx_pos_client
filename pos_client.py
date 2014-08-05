# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class PosFrame
###########################################################################

class PosFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Point of Sales", pos = wx.DefaultPosition, size = wx.Size( 648,428 ), style = wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.stcompany = wx.StaticText( self, wx.ID_ANY, u"Company", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stcompany.Wrap( -1 )
		fgSizer2.Add( self.stcompany, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.stdate = wx.StaticText( self, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stdate.Wrap( -1 )
		fgSizer2.Add( self.stdate, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.stbooth = wx.StaticText( self, wx.ID_ANY, u"Booth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stbooth.Wrap( -1 )
		fgSizer2.Add( self.stbooth, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.stinv = wx.StaticText( self, wx.ID_ANY, u"Inv #", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stinv.Wrap( -1 )
		fgSizer2.Add( self.stinv, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		lsttransChoices = []
		self.lsttrans = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lsttransChoices, 0 )
		fgSizer1.Add( self.lsttrans, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Rp", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 22, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.lsttrans.Bind( wx.EVT_LISTBOX, self.lsttrans_select )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def lsttrans_select( self, event ):
		event.Skip()
	

###########################################################################
## Class LoginDialog
###########################################################################

class LoginDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Point of Sale", pos = wx.DefaultPosition, size = wx.Size( 347,134 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer4 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lblusername = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblusername.Wrap( -1 )
		fgSizer4.Add( self.lblusername, 0, wx.ALL, 5 )
		
		self.txtusername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtusername.SetMaxLength( 10 ) 
		fgSizer4.Add( self.txtusername, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.lblpassword = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblpassword.Wrap( -1 )
		fgSizer4.Add( self.lblpassword, 0, wx.ALL, 5 )
		
		self.txtpassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.txtpassword.SetMaxLength( 10 ) 
		fgSizer4.Add( self.txtpassword, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btnlogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.btnlogin, 0, wx.ALL, 5 )
		
		self.btnquit = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.btnquit, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnlogin.Bind( wx.EVT_BUTTON, self.btnlogin_click )
		self.btnquit.Bind( wx.EVT_BUTTON, self.btnquit_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnlogin_click( self, event ):
		event.Skip()
	
	def btnquit_click( self, event ):
		event.Skip()
	

###########################################################################
## Class RestFrame
###########################################################################

class RestFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

