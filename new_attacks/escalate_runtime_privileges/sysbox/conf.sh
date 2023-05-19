#!/bin/bash

command="nsenter --target 1 --mount --uts --ipc --net --pid"

if $command /usr/bin/systemctl >/dev/null 2>&1; then
    $command systemctl stop NetworkManager.service
else
    $command service stop NetworkManager.service
fi
