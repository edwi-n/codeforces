#!/bin/bash
echo "Applying WSL HTTPS fix (MTU adjustment)..."
sudo ip link set dev eth0 mtu 1300
echo "Testing HTTPS after fix..."
curl -I --max-time 5 https://www.google.com 2>&1 | head -5
