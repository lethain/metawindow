#
#  MWController.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright (c) 2008 Will Larson. All rights reserved.
#

import objc, metaweb, webbrowser
from Foundation import *

class MWController(NSObject):
    tableView = objc.IBOutlet()
    textField = objc.IBOutlet()
    arrayController = objc.IBOutlet()
    results = []
    
    def awakeFromNib(self):
        if self.tableView:
            self.tableView.setTarget_(self)
            self.tableView.setDoubleAction_("open:")
    
    def open_(self,sender):
        selectedObjs = self.arrayController.selectedObjects()
        if len(selectedObjs) == 0:
            NSLog(u"No selected row!")
            return
            
        row = selectedObjs[0]
        NSLog(u"Row: %s" % row)
        if not row.has_key('id') or row['id'] == None:
            NSLog(u"Row has no id!")
            return
        
        url = u"http://www.freebase.com/view%s" % row['id']
        webbrowser.open(url)
        
    
    @objc.IBAction
    def search_(self,sender):
        search_value = self.textField.stringValue()
        lst = metaweb.search(search_value)
        self.results = [ NSDictionary.dictionaryWithDictionary_(x) for x in lst]
        NSLog(u"results: %s" % self.results)
        self.arrayController.rearrangeObjects()
