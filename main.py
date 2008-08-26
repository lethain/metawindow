#
#  main.py
#  MetaWindow
#
#  Created by Will Larson on 8/22/08.
#  Copyright Will Larson 2008. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import metaweb
import MetaWindowAppDelegate
import MWController
import MWDragWindow
import MWDragArrayController

# pass control to AppKit
AppHelper.runEventLoop()
