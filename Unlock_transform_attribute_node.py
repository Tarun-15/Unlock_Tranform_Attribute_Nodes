"""
Author: Tarun Rawlani
Tool Name : Transform Attribute Node
Description : It will get the selected mesh nodes, checks if any nodes are selected, and then unlocks the transform attributes for each node.

"""

import maya.cmds as cmds

def unlockTransform():
    meshNodes = cmds.ls(selection=True)
    if not meshNodes:
        print("Not selected any objects")
    else:
        print("Unlocked")
        for meshNode in meshNodes:
            meshNo = cmds.listRelatives(meshNode, parent=True)
            attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']
            for attr in attrs:
                cmds.setAttr(meshNode + attr, lock=False, keyable=True, channelBox=True)

unlockTransform()
