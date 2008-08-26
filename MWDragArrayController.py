#
#  MWDragArrayController.py
#  MetaWindow
#
#  Created by Will Larson on 8/26/08.
#  Copyright (c) 2008 Will Larson. All rights reserved.
#

from AppKit import NSStringPboardType
from Foundation import *


class MWDragArrayController(NSArrayController):
    def tableView_writeRows_toPasteboard_(self,tv,rows,pb):
        arranged = self.arrangedObjects()
        data = ",".join([ arranged[x]['name'] for x in rows ])
        pb.declareTypes_owner_([NSStringPboardType],self)
        pb.setString_forType_(data,NSStringPboardType)
        return True
        
