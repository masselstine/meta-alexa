# Install the pot-watcher container on an OverC system
# Prior to running this .c3 file you need to link the /dev/bus
# from cube-desktop
#
# c3 cfg -v link localhost:bus cube-desktop:/dev/bus
# c3 cfg gen cube-desktop
#
# then restart cube-desktop
#
c3-ctl add -n pot-watcher docker://<registry>/pot-watcher
c3-cfg -v link localhost:bus pot-watcher:/dev/bus
c3-cfg set -n pot-watcher app:/root/entrypoint.sh
c3-cfg gen pot-watcher
