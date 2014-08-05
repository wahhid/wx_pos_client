import wx
import pos_client
import logindialog
		
class Pos_ClientMain(wx.App):
	
	def OnInit(self):
		self.logindialog = logindialog.POS_LoginDialog(None)
		self.logindialog.Show()	
		return True

app = Pos_ClientMain(0)		
app.MainLoop()