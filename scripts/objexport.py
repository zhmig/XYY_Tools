#coding:utf-8
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import os,sys

def tools():
    if(cmds.window('exp_win',q=True,ex=True)):cmds.deleteUI('exp_win')
    cmds.window('exp_win',t=u'导出工具',s=False,wh=(420, 525))
    cmds.formLayout('main_formlay')
    cmds.textFieldButtonGrp('filepath_txbtn',cw=[[1, 60]],cal=[[1, u'left']],adj=2,l=u'存放路径：',bl=u' <<< ',bc='get_fbx_file("g_path")')
    cmds.button('getcurr_path_txbtn',l=u'M',c='get_fbx_file("g_currentfile")')
    cmds.iconTextButton('refresh_tool_btn',i=u'MASH_SwitchGeometryType.png',mw=5,mh=5,c='refresh_tools()')
    cmds.radioButtonGrp('curr_exp_typ_radio',cw=[[1, 80]],cal=[[1, u'left']],nrb=3,sl=1,l=u'导出类型',l1=u'FBX',l2=u'ABC',l3=u'OBJ')
    cmds.frameLayout('fbx_framelay',cll=True,l=u'Fbx导出',
                                    cc=u'cmds.frameLayout("abc_framelay",e=True,cl=False)',
                                    ec=u'cmds.frameLayout("abc_framelay",e=True,cl=True);\ncmds.frameLayout("obj_framelay",e=True,cl=True)')
    cmds.tabLayout('cam_tablay',h=110,cr=True)
    cmds.formLayout('cam_formlay')
    cmds.textScrollList('cam_txscrollList',ams=True)
    cmds.iconTextButton('cam_add_btn',i=u'setEdAddCmd.png',c='add_list_item("cam")')
    cmds.iconTextButton('cam_reduce_btn',i=u'setEdRemoveCmd.png',c='reduce_list_item("cam")')
    cmds.iconTextButton('cam_refresh_btn',i=u'TTF_Refresh_150.png',c='refresh_slist("cam")')
    cmds.tabLayout('cam_tablay',e=True,tli=(1,u'Camera 选项卡'))
    cmds.tabLayout('loc_tablay',p='fbx_framelay',h=110,tv=True,scr=False,cr=True)
    cmds.formLayout('loc_formlay')
    cmds.textScrollList('loc_txscrollList',ams=True)
    cmds.iconTextButton('loc_add_btn',i=u'setEdAddCmd.png',c='add_list_item("loc")')
    cmds.iconTextButton('loc_reduce_btn',i=u'setEdRemoveCmd.png',c='reduce_list_item("loc")')
    cmds.iconTextButton('loc_refresh_btn',i=u'TTF_Refresh_150.png',c='refresh_slist("loc")')
    cmds.tabLayout('loc_tablay',e=True,tli=(1,u'Locator 选项卡'))
    cmds.tabLayout('pl_tablay',p='fbx_framelay',h=110,cr=True)
    cmds.formLayout('pl_formlay')
    cmds.textScrollList('pl_txscrollList',ams=True)
    cmds.iconTextButton('pl_add_btn',i=u'setEdAddCmd.png',c='add_list_item("pl")')
    cmds.iconTextButton('pl_reduce_btn',i=u'setEdRemoveCmd.png',c='reduce_list_item("pl")')
    cmds.iconTextButton('pl_refresh_btn',i=u'TTF_Refresh_150.png',c='refresh_slist("pl")')
    cmds.tabLayout('pl_tablay',e=True,tli=(1,u'PointLight 选项卡'))
    cmds.button('fbx_export_btn',p='fbx_framelay',h=30,l=u'导出',c='fbx_export()')
    cmds.frameLayout('abc_framelay',p='main_formlay',cl=True,cll=True,l=u'Abc导出',
                                    cc=u'cmds.frameLayout("obj_framelay",e=True,cl=False)',
                                    ec=u'cmds.frameLayout("fbx_framelay",e=True,cl=True);\ncmds.frameLayout("obj_framelay",e=True,cl=True)')
    cmds.formLayout('abc_formlay')
    cmds.textScrollList('abc_txscrollList',h=342,ams=True)
    cmds.iconTextButton('abc_add_btn',style="iconOnly",i=u'out_MASH_CreateUtility_200.png',c='add_list_item("abc")')
    cmds.iconTextButton('abc_reduce_btn',style="iconOnly",i=u'TTF_Clear_200.png',c='reduce_list_item("abc")')
    cmds.iconTextCheckBox('abc_comb_btn',i=u'MASH_InvertOn_200.png',si=u'out_MASH_Enable_Selected_200.png')
    cmds.button('abc_export_btn',h=30,l=u'导出',c='abc_obj_export("abc")')
    cmds.frameLayout('obj_framelay',p='main_formlay',cl=True,cll=True,l=u'Obj导出',
                                    cc=u'cmds.frameLayout("fbx_framelay",e=True,cl=False)',
                                    ec=u'cmds.frameLayout("fbx_framelay",e=True,cl=True);\ncmds.frameLayout("abc_framelay",e=True,cl=True)')
    cmds.formLayout('obj_formlay')
    cmds.textScrollList('obj_txscrollList',h=342,ams=True)
    cmds.iconTextButton('obj_add_btn',style="iconOnly",i=u'out_MASH_CreateUtility_200.png',c='add_list_item("obj")')
    cmds.iconTextButton('obj_reduce_btn',style="iconOnly",i=u'TTF_Clear_200.png',c='reduce_list_item("obj")')
    cmds.button('obj_export_btn',h=30,l=u'导出')
    cmds.formLayout('main_formlay',e=1,af=[['filepath_txbtn', 'top', 7], ['filepath_txbtn', 'left', 5], ['getcurr_path_txbtn', 'top', 8], 
                                    ['refresh_tool_btn', 'top', 2], ['refresh_tool_btn', 'right', 5], ['curr_exp_typ_radio', 'left', 5], 
                                    ['curr_exp_typ_radio', 'right', 5], ['fbx_framelay', 'left', 5], ['fbx_framelay', 'right', 5], 
                                    ['abc_framelay', 'left', 5], ['abc_framelay', 'right', 5], ['obj_framelay', 'left', 5], ['obj_framelay', 'right', 5]],
                                    ac=[['curr_exp_typ_radio', 'top', 5, 'filepath_txbtn'], ['fbx_framelay', 'top', 5, 'curr_exp_typ_radio'], 
                                    ['abc_framelay', 'top', 5, 'fbx_framelay'], ['obj_framelay', 'top', 5, 'abc_framelay']],
                                    ap=[['filepath_txbtn', 'right', 3, 85], ['getcurr_path_txbtn', 'left', 2, 85], ['getcurr_path_txbtn', 'right', 2, 90], 
                                    ['refresh_tool_btn', 'left', 2, 90]])
    cmds.formLayout('cam_formlay',e=1,af=[['cam_txscrollList', 'top', 5], ['cam_txscrollList', 'left', 5], ['cam_add_btn', 'top', 5], ['cam_add_btn', 'right', 5], 
                                    ['cam_reduce_btn', 'top', 30], ['cam_reduce_btn', 'right', 5], ['cam_refresh_btn', 'top', 50], ['cam_refresh_btn', 'right', 5]],
                                    ap=[['cam_txscrollList', 'right', 5, 90], ['cam_add_btn', 'left', 5, 90], ['cam_reduce_btn', 'left', 5, 90], 
                                    ['cam_refresh_btn', 'left', 3, 90]])
    cmds.formLayout('loc_formlay',e=1,af=[['loc_txscrollList', 'top', 5], ['loc_txscrollList', 'left', 5], ['loc_add_btn', 'top', 5], ['loc_add_btn', 'right', 5], 
                                    ['loc_reduce_btn', 'top', 30], ['loc_reduce_btn', 'right', 5], ['loc_refresh_btn', 'top', 50], ['loc_refresh_btn', 'right', 5]],
                                    ap=[['loc_txscrollList', 'right', 5, 90], ['loc_add_btn', 'left', 5, 90], ['loc_reduce_btn', 'left', 5, 90], 
                                    ['loc_refresh_btn', 'left', 3, 90]])
    cmds.formLayout('pl_formlay',e=1,af=[['pl_txscrollList', 'top', 5], ['pl_txscrollList', 'left', 5], ['pl_add_btn', 'top', 5], 
                                    ['pl_add_btn', 'right', 5], ['pl_reduce_btn', 'top', 30], ['pl_reduce_btn', 'right', 5], ['pl_refresh_btn', 'top', 50], 
                                    ['pl_refresh_btn', 'right', 5]],
                                    ap=[['pl_txscrollList', 'right', 5, 90], ['pl_add_btn', 'left', 5, 90], ['pl_reduce_btn', 'left', 5, 90], 
                                    ['pl_refresh_btn', 'left', 3, 90]])
    cmds.formLayout('abc_formlay',e=1,af=[['abc_txscrollList', 'top', 5], ['abc_txscrollList', 'left', 5], ['abc_add_btn', 'top', 50], 
                                    ['abc_add_btn', 'right', 30], ['abc_reduce_btn', 'right', 30], ['abc_comb_btn', 'right', 30], 
                                    ['abc_export_btn', 'left', 5], ['abc_export_btn', 'right', 5], ['abc_export_btn', 'bottom', 0]],
                                    ac=[['abc_add_btn', 'left', 5, 'abc_txscrollList'], ['abc_reduce_btn', 'top', 50, 'abc_add_btn'], 
                                    ['abc_reduce_btn', 'left', 2, 'abc_txscrollList'], ['abc_comb_btn', 'top', 50, 'abc_reduce_btn'], 
                                    ['abc_comb_btn', 'left', 10, 'abc_txscrollList'], ['abc_export_btn', 'top', 5, 'abc_txscrollList']],
                                    ap=[['abc_txscrollList', 'right', 5, 70]])
    cmds.formLayout('obj_formlay',e=1,af=[['obj_txscrollList', 'top', 5], ['obj_txscrollList', 'left', 5], ['obj_add_btn', 'top', 50], 
                                    ['obj_add_btn', 'right', 30], ['obj_reduce_btn', 'right', 30], ['obj_export_btn', 'left', 5], 
                                    ['obj_export_btn', 'right', 5]],
                                    ac=[['obj_add_btn', 'left', 10, 'obj_txscrollList'], ['obj_reduce_btn', 'top', 80, 'obj_add_btn'], 
                                    ['obj_reduce_btn', 'left', 2, 'obj_txscrollList'], ['obj_export_btn', 'top', 5, 'obj_txscrollList']],
                                    ap=[['obj_txscrollList', 'right', 5, 70]])
    cmds.showWindow('exp_win')
    cmds.window('exp_win',e=True,h=525)
    cmds.window('exp_win',e=True,w=420)

def get_fbx_file(fbx_path_v):
    if fbx_path_v == 'g_path':
        # multiple_maya_Filters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        multiple_maya_Filters = "FBX (*.fbx);;Obj (*.obj);;Alembic (*.abc)"
        get_file_path = cmds.fileDialog2(ff=multiple_maya_Filters, ds=1, fm=0)[0]# cmds.fileDialog2(ff=multiple_maya_Filters, ds=1, fm=1)[0]
    if fbx_path_v == 'g_currentfile':
        obj_typ = ''
        typ_sel = cmds.radioButtonGrp('curr_exp_typ_radio', q=True, sl=True)
        if typ_sel == 1:
            obj_typ = '.fbx'
        if typ_sel == 2:
            obj_typ = '.abc'
        if typ_sel == 3:
            obj_typ = '.obj'
        if not cmds.file(q=True,sn=True):
            cmds.confirmDialog( t=u'警告', m=u'请先保存文件再点击按钮！！！',icn='warning', b=['Yes'], db='Yes', ds='No' )
        else:
            get_file_path = "%s%s" % (os.path.splitext(cmds.file(q=True,sn=True))[0],obj_typ)
    cmds.textFieldButtonGrp('filepath_txbtn',e=True,tx=get_file_path)

def refresh_tools():
    if cmds.objExists('exp_master'):
        cmds.delete('exp_master')
    default_folder()
    cmds.textFieldButtonGrp('filepath_txbtn',e=True,tx='')
    for i in ['cam','loc','pl']:
        if cmds.textScrollList('%s_txscrollList'%(i),q=True,ai=True):
            cmds.delete(cmds.textScrollList('%s_txscrollList'%(i),q=True,ai=True))
        cmds.textScrollList('%s_txscrollList'%(i),e=True,ra=True)

    cmds.textScrollList('abc_txscrollList',e=True,ra=True)
    cmds.textScrollList('obj_txscrollList',e=True,ra=True)

def refresh_slist(refresh_v):
    # cmds.textScrollList('%s_txscrollList'%(refresh_v),q=True,ai=True)
    cmds.textScrollList('%s_txscrollList'%(refresh_v),e=True,ra=True)
    if cmds.objExists('exp_%s_grp'%refresh_v):
        grp_dn_obj = cmds.listRelatives(('exp_%s_grp' % refresh_v),ad=True,typ='transform')
    if grp_dn_obj is None:
        cmds.confirmDialog( t=u'警告', m=u'当前选项卡无东西，\n检查大纲里的组!!',icn='warning', b=['Yes'], db='Yes', ds='No' )
    else:
        for obj in grp_dn_obj:
            cmds.textScrollList('%s_txscrollList'%(refresh_v),e=True,a=obj)

def add_list_item(add_v):
    selectObj = cmds.ls(sl=True)
    if add_v in ['cam','loc','pl']:
        grp_dn_obj = cmds.listRelatives(('exp_%s_grp' % add_v),ad=True,typ='transform')
        if grp_dn_obj:
            add_name = ('%s_%s'% (add_v, str(len(grp_dn_obj)+1)))
        else:
            add_name = ('%s_1'% (add_v))
        if add_v == 'cam':
            obj_typ = 'camera'
            # cmds.camera(n=add_name)
        if add_v == 'loc':
            obj_typ = 'spaceLocator'
            # cmds.spaceLocator(n=add_name)
        if add_v == 'pl':
            obj_typ = 'pointLight' 
            # cmds.pointLight(n=add_name)

        mel.eval('%s -n \"%s\"'%(obj_typ,add_name))
        if selectObj:
            parentNode = cmds.parentConstraint(selectObj[0],add_name,w=1,mo=False)
            if not cmds.objExists('OtherConstraintSystem'):
                cmds.group(n='OtherConstraintSystem',em=True,p='exp_master')
            cmds.parent(parentNode,'OtherConstraintSystem')
        cmds.parent(add_name,('exp_%s_grp' % add_v))
        cmds.textScrollList('%s_txscrollList'%(add_v),e=True,a=add_name)
    else:
        if selectObj:
            for obj in selectObj:
                cmds.textScrollList('%s_txscrollList'%(add_v),e=True,a=cmds.ls(obj,l=True))
        else:
            cmds.confirmDialog( t=u'警告', m=u'没有选择任何物体或者组！！',icn='warning', b=['Yes'], db='Yes', ds='No' )

def reduce_list_item(reduce_v):
    sels_v = cmds.textScrollList('%s_txscrollList'%(reduce_v),q=True,sii=True)
    sels_n = cmds.textScrollList('%s_txscrollList'%(reduce_v),q=True,si=True)
    if sels_v:
        sels_v.sort()
        sels_v.reverse()
        sels_n.reverse()
        for s in range(len(sels_v)):
            cmds.textScrollList('%s_txscrollList'%(reduce_v),e=True,rii=sels_v[s])
            if reduce_v in ['cam','loc','pl']:
                cmds.delete(sels_n[s])

def default_folder():
    if not cmds.objExists('exp_master'):
        cmds.group(n='exp_master',em=True,w=True)
    if not cmds.objExists('exp_cam_grp'):
        cmds.group(n='exp_cam_grp',em=True,p='exp_master')
    if not cmds.objExists('exp_loc_grp'):
        cmds.group(n='exp_loc_grp',em=True,p='exp_master')
    if not cmds.objExists('exp_pl_grp'):
        cmds.group(n='exp_pl_grp',em=True,p='exp_master')
    if not cmds.objExists('OtherConstraintSystem'):
        cmds.group(n='OtherConstraintSystem',em=True,p='exp_master')

def fbx_export():
    SaveFilePath = cmds.textFieldButtonGrp('filepath_txbtn', q=True, tx=True)
    if not SaveFilePath:
        cmds.confirmDialog( t=u'警告', m=u'填写保存路径！！',icn='warning', b=['Yes'], db='Yes', ds='No' )
    else:
        export_objs = []
        cam_dn_obj = cmds.listRelatives('exp_cam_grp',ad=True,typ='transform')
        loc_dn_obj = cmds.listRelatives('exp_loc_grp',ad=True,typ='transform')
        pl_dn_obj = cmds.listRelatives('exp_pl_grp',ad=True,typ='transform')

        if cam_dn_obj:
            for cam in cam_dn_obj:
                export_objs.append(cam)
        if loc_dn_obj:
            for loc in loc_dn_obj:
                export_objs.append(loc)
        if pl_dn_obj:
            for pl in pl_dn_obj:
                export_objs.append(pl)
        cmds.parent(export_objs,w=True)
        
        startFrame = cmds.playbackOptions(q=True,min=True)
        endFrame = cmds.playbackOptions(q=True,max=True)

        pm.bakeResults(export_objs,sm=True,
                        t=(int(startFrame),
                            int(endFrame)),
                        sb=1,osr=1,dic=True,pok=True,sac=False,ral=False,
                        rba=False,bol=False,mr=True,cp=True,s=True)

        clip_name = os.path.basename(SaveFilePath).split('.', 1)[0]
        pm.mel.FBXResetExport()
        pm.mel.FBXExportSplitAnimationIntoTakes(clear=None)
        pm.mel.FBXExportSplitAnimationIntoTakes(int(startFrame), int(endFrame), v=clip_name)
        pm.mel.FBXExportDeleteOriginalTakeOnSplitAnimation(v=True)
        pm.mel.FBXExportSmoothingGroups(v=True)
        pm.mel.FBXExportSmoothMesh(v=True)
        pm.mel.FBXExportCameras(v=True)
        # pm.mel.FBXExportLights(v=True)
        pm.mel.FBXExportReferencedAssetsContent(v=True)
        pm.mel.FBXExportAnimationOnly(v=False)
        pm.mel.FBXExportBakeComplexAnimation(v=True)
        pm.mel.FBXExportBakeComplexStart(v=int(startFrame))
        pm.mel.FBXExportBakeComplexEnd(v=int(endFrame))
        pm.mel.FBXExportBakeResampleAnimation(v=True)
        pm.mel.FBXExportSkins(v=True)
        pm.mel.FBXExportShapes(v=True)
        pm.mel.FBXExportInputConnections(v=False)
        pm.mel.FBXExportConstraints(v=False)
        pm.mel.FBXExportUpAxis('y')
        pm.mel.FBXExportFileVersion(v='FBX201300')
        pm.mel.FBXExportInAscii(v=True)
        pm.mel.FBXExportEmbeddedTextures(v=False)
        pm.mel.FBXExportShowUI(v=False)

        #导出
        pm.select(cl = True)
        pm.select(export_objs,add=True)
        pm.mel.eval('FBXExport -file "%s" -s' % SaveFilePath)
        pm.mel.FBXExportSplitAnimationIntoTakes(clear=None) 

        cmds.confirmDialog( t=u'警告', m=u'导出完成，请查看！！！',icn='information', b=['Yes'], db='Yes', ds='No' )

def abc_obj_export(abcobj_v):
    SaveFilePath = cmds.textFieldButtonGrp('filepath_txbtn', q=True, tx=True)
    startFrame = cmds.playbackOptions(q=True,min=True)
    endFrame = cmds.playbackOptions(q=True,max=True)
    if not SaveFilePath:
        cmds.confirmDialog( t=u'警告', m=u'填写保存路径！！',icn='warning', b=['Yes'], db='Yes', ds='No' )
    else:
        allitems = cmds.textScrollList('%s_txscrollList'%(abcobj_v),q=True,ai=True)
        if abcobj_v == 'abc':
            obj_command = ''
            if cmds.iconTextCheckBox('abc_comb_btn',q=True,v=True):
                for item in allitems:
                    obj_command += ('-root %s '% item)
                abc_command(startFrame,endFrame,obj_command,SaveFilePath)
            else:
                pass
                for item in allitems:
                    save_name = SaveFilePath
                    item_sort = item.split('|')[-1]
                    filename= os.path.splitext(SaveFilePath)
                    save_name = "%s_%s%s" % (filename[0],item_sort,filename[1])
                    obj_command = ('-root %s' % item)
                    abc_command(startFrame,endFrame,obj_command,save_name)
            

def abc_command(start,end,obj,save_name):
    command = "-frameRange " + str(start) + " " + str(end) +" -attr Translate -uvWrite -writeVisibility -dataFormat ogawa " + obj + " -file " + save_name #-root 
    print (command)
    cmds.AbcExport ( j = command )
tools()
default_folder()
