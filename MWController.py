#
#  MWController.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright (c) 2008 Will Larson. All rights reserved.
#

import objc, metaweb
from Foundation import *

class MWController(NSObject):
    tableView = objc.IBOutlet()
    textField = objc.IBOutlet()
    _results = []
    
    @objc.IBAction
    def search_(self,sender):
        search_value = self.textField.stringValue()
        _results = metaweb.search(search_value)
        NSLog(u"Search: %s" % _results)