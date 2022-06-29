#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtUiTools import *
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import maya.cmds as cmds
import sys,os
path = r'D:\Zhmig\ScriptProj'

sys.path.append(path)
sys.path.append(path + "\XYYScript\Lib")

import XYYScript
import ldap3

#Specify the path directly
LOGGINUIFILEPATH = r'D:\Zhmig\ScriptProj\XYYScript\UI\Signin2.ui'
if os.path.isfile('%s/ActiveDirectory.ini'%path):
    print("the file exist")

##Class that creates MainWindow
class MainWindow(MayaQWidgetBaseMixin, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #Specify the UI path
        self.UI = QUiLoader().load(LOGGINUIFILEPATH)
        #Get window title from UI
        self.setWindowTitle(self.UI.windowTitle())
        #Center widget
        self.setCentralWidget(self.UI)
		# 禁止窗口最大最小化
        self.setWindowFlags(Qt.WindowCloseButtonHint)
 
		# 禁止拉伸窗口
        self.setFixedSize(self.UI.width(), self.UI.height())		


        #Connect button
        self.UI.cancel_btn.clicked.connect(self.cancelPushButton)
        self.UI.signin_btn.clicked.connect(self.signinPushButton)

    def cancelPushButton(self):
        self.close()

    def signinPushButton(self):
        if os.path.exists('%s/XYYScript/ActiveDirectory.ini'%path):
            with open(('%s/XYYScript/ActiveDirectory.ini'%path),'r') as file:
                content=file.read()

        content = content.split('\r\n')
        LDAP_SERVER_IP = content[0].split('= ')[1]
        LDAP_SERVER_NAME = content[1].split('= ')[1]
        LDAP_USER = self.UI.username_lineEdit.text()
        LDAP_PSW = self.UI.pw_lineEdit.text()
        from XYYScript import link_ad
        try:
            ad_link_inf = link_ad.verification_ad(LDAP_SERVER_IP,LDAP_SERVER_NAME,LDAP_USER,LDAP_PSW)
            print (ad_link_inf)
            if ad_link_inf == "lian jie cheng gong":
                self.close()
                self._write_user(LDAP_USER,LDAP_PSW)
        except:pass
        
        # return LDAP_SERVER_IP,LDAP_SERVER_NAME
        

    def _write_user(self,LDAP_USER,LDAP_PSW): 
        getScriptDir = cmds.internalVar(userScriptDir=True)
        getMayaModDir = getScriptDir.rsplit('/',3)[0]+'/'
        if os.path.exists('%sscripts/user_config.ini' % getMayaModDir):
            os.remove('%sscripts/user_config.ini' % getMayaModDir)
        user_file = ('%sscripts/user_config.ini' % getMayaModDir)
        if not os.path.exists(user_file):
            with open(user_file,'w') as file:
                file.write('%s\r\n'%LDAP_USER)
                file.write('%s\r\n'%LDAP_PSW)
                        
    # def ad_link(self,LDAP_USER,LDAP_PSW):
    #     server = ldap3.Server(LDAP_SERVER_IP,port=389,get_info=ldap3.ALL)
    #     try:
    #         conn = ldap3.Connection(server,user="{}\\{}".format(LDAP_SERVER_NAME,LDAP_USER), password=LDAP_PSW,auto_bind=True,authentication='NTLM')
    #         print(u"lian jie cheng gong\n")
    #         self.close()
    #         from XYYScript import maya_menu
    #     except Exception as e:
    #         print(u'wu fa lian jie\n')
    #     return LDAP_USER,LDAP_PSW

##Start MainWindow
# def main():
#    window = MainWindow()
#    window.show()

# if __name__ == '__main__':
#     try:
#         window.close()
#         window.deleteLater()
#     except:
#         pass
        
# window = MainWindow()
# window.show()