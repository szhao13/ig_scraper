import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection() 

package = "com.instagram.android"

runComponent = package + "/" + activity