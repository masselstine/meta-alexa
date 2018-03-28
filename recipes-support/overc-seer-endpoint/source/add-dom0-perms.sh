#!/bin/bash
#
# Run in dom0 before starting the seer-hub container
# for the first time. Run with:
#
# /opt/container/seer-hub/rootfs/root/add-dom0-perms.sh
#
echo "Adding to /etc/cube-cmd-server.conf"
cat >> /etc/cube-cmd-server.conf <<- EOF

seer:
  commands:
    - cube-ctl#list
    - cube-ctl#start
    - cube-ctl#stop
    - cube-ctl#delete
    - c3-construct
  capabilities:
    - cap-add
    - cap-del

EOF

# Be sure to match what is in /etc/cube-cmd.auth in the container
echo "Adding to /var/lib/cube-cmd-server/auth.db"
echo 'seer $1$overc$u9xCI24YMaNWS3RhbYJXG0' >> /var/lib/cube-cmd-server/auth.db

echo "Restarting cube-cmd-server to make changes to effect."
systemctl restart cube-cmd-server
