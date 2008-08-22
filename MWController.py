#
#  MWController.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright (c) 2008 Will Larson. All rights reserved.
#

import objc
from Foundation import *

class MWController(NSObject):
    tableView = objc.IBOutlet()
    textField = objc.IBOutlet()
    _results = []
    
    @objc.IBAction
    def search_(self,sender):
        search_value = self.textField.stringValue()
        NSLog(u"Search: %s" % search_value)