[app]

# (str) Title of your application
title = SimpleApp

# (str) Package name
package.name = simple_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas
source.include_exts_exclude = pyc,pyo,pyd,__pycache__,.git,.svn,CVS

# (list) Application requirements
requirements = python3,kivy

# (list) Application requirements (comma separated e.g. requirement1,requirement2)
# comma separated e.g. sqlite3,kivy
# requirements = sqlite3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET
