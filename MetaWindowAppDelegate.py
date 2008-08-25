#
#  MetaWindowAppDelegate.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright Will Larson 2008. All rights reserved.
#

import os,pickle,datetime
from Foundation import *
from AppKit import *

class MetaWindowAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        try:
            path = self.pathForFile('cache.serialized')
            file = open(path,'r')
            self.cache = pickle.load(file)
            file.close()
        except IOError:
            self.cache = {}
    
    def applicationWillTerminate_(self,sender):
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        for key in self.cache:
            filename,createdTime = self.cache[key]
            if createdTime < yesterday:
                filepath = self.pathForFile(filename)
                os.remove(filepath)
                del self.cache[key]
    
        path = self.pathForFile('cache.serialized')
        file = open(path,'w')
        pickle.dump(self.cache,file)
        file.close()
                
    def applicationSupportFolder(self):
        paths = NSSearchPathForDirectoriesInDomains(NSApplicationSupportDirectory,NSUserDomainMask,True)
        basePath = (len(paths) > 0 and paths[0]) or NSTemporaryDirectory()
        fullPath = basePath.stringByAppendingPathComponent_("MetaWindow")
        if not os.path.exists(fullPath):
            os.mkdir(fullPath)
        return fullPath
        
    def pathForFile(self,filename):
        return self.applicationSupportFolder().stringByAppendingPathComponent_(filename)
