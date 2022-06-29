# -*- coding: utf-8 -*-
import maya.cmds as cmds
import pymel.core as pm

MainMayaWindow = pm.language.melGlobals['gMainWindow']
try: 
    if cmds.menu(u'MayaWindow|原创动力工具',ex=True):
        cmds.deleteUI(u'MayaWindow|原创动力工具')
    customMenu = pm.menu(u'原创动力工具', parent=MainMayaWindow)
    pm.menuItem(label=u"导出工具", parent=customMenu)
except:pass