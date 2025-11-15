#!/bin/bash

PORT=8022

GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
BLUE="\e[34m"
RESET="\e[0m"

echo -e "${BLUE}🔍 Checking port ${PORT}...${RESET}"

if sudo lsof -i :$PORT > /dev/null 2>&1; then
    echo -e "${RED}❌ Port ${PORT} is BUSY${RESET}"
    echo -e "${YELLOW}Active process:${RESET}"
    sudo lsof -i :$PORT
else
    echo -e "${GREEN}✔️ Port ${PORT} is FREE${RESET}"
fi
