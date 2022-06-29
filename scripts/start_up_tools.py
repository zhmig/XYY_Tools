import os,sys
import maya.cmds as cmds

path = r'D:\Zhmig\ScriptProj\XYYScript'
sys.path.append(path)
sys.path.append(path + "\Lib\site-packages")
import ldap3

if os.path.exists('%s/ActiveDirectory.ini'%path):
    with open(('%s/ActiveDirectory.ini'%path),'r') as file:
        content=file.read()

content = content.split('\r\n')
LDAP_SERVER_IP = content[0].split('= ')[1]
LDAP_SERVER_NAME = content[1].split('= ')[1]
# configure
getScriptDir = cmds.internalVar(userScriptDir=True)
getMayaModDir = getScriptDir.rsplit('/',3)[0]+'/'

if os.path.exists('%sscripts/user_config.ini' % getMayaModDir):
    with open(('%sscripts/user_config.ini' % getMayaModDir),'r') as f:
        user_info = f.read()
    if user_info:
        user_info = user_info.split('\r\n')
        LDAP_USER = user_info[0]
        LDAP_PSW = user_info[1]

server = ldap3.Server(LDAP_SERVER_IP,port=389,get_info=ldap3.ALL)
try:
    conn = ldap3.Connection(server,user=("%s\\%s"% (LDAP_SERVER_NAME,LDAP_USER)), password=LDAP_PSW,auto_bind=True,authentication='NTLM')
    print(u"lian jie cheng gong\n")
    import maya_menu
except Exception as e:
    print(u'wu fa lian jie\n')
    import logging_ad
    if __name__ == '__main__':
        try:
            logon_tools.close()
            logon_tools.deleteLater()
        except:
            pass
            
    logon_tools = logging_ad.MainWindow()
    logon_tools.show()
