[app]
title = Decentra-Network
package.name = decentra_network
package.domain = org.decentra_network
source.dir = decentra_network/
source.include_exts = py,png,jpg,kv,atlas
version = 0.26.1
orientation = all
fullscreen = 0
android.permissions = INTERNET
icon.filename = decentra_network/gui_lib/images/logo.ico
p4a.local_recipes = recipes/src/python-for-android/recipes/

ios.codesign.allowed = false

[app@api]
title = Decentra-Network-API
package.name = decentra_network_api
source.dir = decentra_network/api/buildozer/
requirements =  decentra_network==0.26.1, Kivy==2.1.0, waitress==2.1.2, werkzeug==2.0.3, flask==2.0.0

[app@gui]
title = Decentra-Network-GUI
package.name = decentra_network_gui
source.dir = decentra_network/gui/
requirements =  decentra_network==0.26.1, Kivy==2.1.0, kivymd==0.104.2, kivymd_extensions.sweetalert==0.1.5, pillow==9.1.1



[buildozer]
log_level = 2
warn_on_root = 1
