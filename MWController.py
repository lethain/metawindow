#
#  MWController.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright (c) 2008 Will Larson. All rights reserved.
#

import objc, metaweb, webbrowser, pickle, datetime, md5, threading
from MWRowWindowController import MWRowWindowController
from AppKit import *
from Foundation import *


class MWController(NSObject):
    tableView = objc.IBOutlet()
    textField = objc.IBOutlet()
    arrayController = objc.IBOutlet()
    indicator = objc.IBOutlet()
    results = []
    rowCache = {}
    _cache = None
    
    def getCache(self):
        if self._cache is None:
            self._cache = NSApp.delegate().cache
        return self._cache
    cache = property(getCache,None,None,"Cache of searches.")
    
    def awakeFromNib(self):
        if self.tableView:
            self.tableView.setTarget_(self)
            self.tableView.setDoubleAction_("open:")
            self.tableView.setDraggingSourceOperationMask_forLocal_(NSDragOperationCopy, False)
            
    def dealloc(self):
        for key in self.rowCache:
            value = self.rowCache[key]
            value.release()
        super(MWController,self).dealloc()
    
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
        
        if self.rowCache.has_key(row):
            rwc = self.rowCache[row]
            rwc.showWindow_(self)
        else:
            rwc =MWRowWindowController.alloc().initWithWindowNibName_(u"RowWindow")
            rwc.rowDict = row
            rwc.showWindow_(self)
            rwc.retain()
            self.rowCache[row] = rwc
        
    
    def getCachedSearch(self,searchString):
        if self.cache.has_key(searchString):
            filename,timestamp = self.cache[searchString]
            age = datetime.datetime.now() - timestamp
            if age > datetime.timedelta(days=1):
                return None
            filepath = NSApp.delegate().pathForFile(filename)
            file = open(filepath,'r')
            data = pickle.load(file)
            file.close()
            return data
        return None
        
    def cacheResultsForSearch(self,searchString,results):
        filename = u"%s.cached" % md5.md5(searchString).hexdigest()[12:]
        filepath = NSApp.delegate().pathForFile(filename)
        file = open(filepath,'w')
        pickle.dump(results,file)
        file.close()
        self.cache[searchString] = (filename,datetime.datetime.now())
        
    def dragSearch(self,searchString):
        self.textField.setStringValue_(searchString)
        self.search_(self)
    
    @objc.IBAction
    def search_(self,sender):
        search_value = self.textField.stringValue()
        cached = self.getCachedSearch(search_value)
        if cached is None:
            self.indicator.startAnimation_(self)
            cached = metaweb.search(search_value)
            self.cacheResultsForSearch(search_value,cached)
            self.indicator.stopAnimation_(self)
        self.results = [ NSDictionary.dictionaryWithDictionary_(x) for x in cached]
        self.arrayController.rearrangeObjects()
