#
#  MWDragWindow.py
#  MetaWindow
#
#  Created by Will Larson on 8/26/08.
#  Copyright (c) 2008 Will Larson. All rights reserved.
#

import objc
from Foundation import *
from AppKit import *


class MWDragWindow(NSWindow):
    controller = objc.IBOutlet()
    
    def awakeFromNib(self):
        self.registerForDraggedTypes_([NSStringPboardType])
        
    def draggingEntered_(self,sender):
        pboard = sender.draggingPasteboard()
        types = pboard.types()
        opType = NSDragOperationNone
        if NSStringPboardType in types:
            return NSDragOperationCopy
        return opType
        
    def performDragOperation_(self,sender):
        pboard = sender.draggingPasteboard()
        successful = False
        if NSStringPboardType in pboard.types():
            txt = pboard.stringForType_(NSStringPboardType)
            self.controller.dragSearch(txt)
            successful = True
        return successful