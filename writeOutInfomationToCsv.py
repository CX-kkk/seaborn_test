#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import maya.cmds as cmds


def getObjInfo(obj):
    scales = cmds.xform(obj, q=True, r=True, s=True )
    transform = cmds.xform(obj, q=True, r=True, t=True)
    transform.insert(0, scales[0])
    transform.insert(0, obj)
    return transform
    

def wtrieCsv(objList):
    with open('E:/my_scriptLib/JolieXPackage/python/studio/JolieX/seaborn/test.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile,dialect='excel')
        spamwriter.writerow(['Name', 'Radius', 'TransformX', 'TransformY', 'TransformZ'])
        for obj in objList:
            rowInfo = getObjInfo(obj)
            spamwriter.writerow(rowInfo)
    
    
    
if __name__=='__main__':
    objList = cmds.ls(sl=True)
    wtrieCsv(objList)