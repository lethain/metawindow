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
    arrayController = objc.IBOutlet()
    results = []
    
    @objc.IBAction
    def search_(self,sender):
        search_value = self.textField.stringValue()
        lst = metaweb.search(search_value)
        self.results = [ NSDictionary.dictionaryWithDictionary_(x) for x in lst]
        self.arrayController.rearrangeObjects()
