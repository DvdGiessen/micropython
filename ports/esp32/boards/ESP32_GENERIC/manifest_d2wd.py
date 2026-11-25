# D2WD variant manifest: the 2MiB build has no room for the full frozen set
# Compared to boards/manifest.py this removes:
# - aioespnow
# - dht
# - ds18x20
# - onewire
# - umqtt.robust
# - umqtt.simple
# - upysh
# These can instead be installed from micropython-lib via mip when needed.

freeze("$(PORT_DIR)/modules")
include("$(MPY_DIR)/extmod/asyncio")

# Useful networking-related packages.
require("bundle-networking")

# Require some micropython-lib modules.
require("neopixel")
