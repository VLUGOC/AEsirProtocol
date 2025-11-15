#!/bin/bash
while true; do
    nc -l -p 8022 >> /home/victor/AEsirProtocol/phone_bridge/from_phone.txt
done
