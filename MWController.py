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
        def valid_result(x):
            if x is None:
                return False
            if not x.has_key('name'):
                return False
            if not x.has_key('article'):
                return False
            article = x['article']
            if article is None:
                return False
            if not article.has_key('id'):
                return False
            return True
        search_value = self.textField.stringValue()
        lst = metaweb.search(search_value)
        lst = [x for x in lst if valid_result(x)]
        self.results = [ NSDictionary.dictionaryWithDictionary_(x) for x in lst]
        self.arrayController.rearrangeObjects()
