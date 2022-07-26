[app]
title = Decentra-Network
package.name = decentra_network
package.domain = org.decentra_network
source.dir = decentra_network/
source.include_exts = py,png,jpg,kv,atlas
version = 0.25.0
orientation = all
fullscreen = 0
android.permissions = INTERNET
icon.filename = decentra_network/gui_lib/images/logo.ico


[app@api]
title = Decentra-Network-API
package.name = decentra_network_api
source.dir = decentra_network/api/buildozer/
requirements =  decentra_network, decentra_network_api, Kivy==2.0.0


[buildozer]
log_level = 1
warn_on_root = 1