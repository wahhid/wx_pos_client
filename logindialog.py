from pos_client import *
import pos_client
import posframe

class POS_LoginDialog(pos_client.LoginDialog):
    
    def __init__(self,parent):
        pos_client.LoginDialog.__init__(self,parent)
    
    def btnlogin_click( self, event):
        self.parkingframe = posframe.POS_PosFrame(self)
        self.parkingframe.Show()
        return True
    
    def btnquit_click( self, event ):
        self.Destroy()