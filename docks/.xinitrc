#!/bin/sh
setxkbmap -variant dvorak
sudo dhcpcd &
sudo chmod a+rw /sys/class/backlight/acpi_video0/brightness
exec leftwm
