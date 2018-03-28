# replace <registry> with the name of the registry you
# intend to pull from. Obfuscated here since for the demo
# we are using a known RSA private key which is included
# in the image which we don't want to readily share.
#
c3-ctl add -n seer-hub docker://<registry>/overc-seer-hub
c3-cfg -n seer-hub set app:/root/entrypoint.sh
c3-cfg -n seer-hub set cube.env:SEER_ENDPOINT_PORT=9003
c3-cfg -n seer-hub set autostart:dom0
c3-cfg gen seer-hub
