#
#  MetaWindowAppDelegate.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright Amy and my apartment 2008. All rights reserved.
#

from Foundation import *
from AppKit import *

class MetaWindowAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
