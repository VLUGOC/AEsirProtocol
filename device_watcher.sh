#!/bin/bash

PHONE_IP="192.168.20.133"
ADB_PORT=5555

while true; do
    if ping -c 1 $PHONE_IP >/dev/null 2>&1; then
        adb connect $PHONE_IP:$ADB_PORT >/dev/null 2>&1
    fi
    sleep 5
done
