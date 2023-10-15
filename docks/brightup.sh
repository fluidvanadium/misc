P=$(cat /sys/class/backlight/acpi_video0/brightness)
P=$((P+1))
echo "$P" > /sys/class/backlight/acpi_video0/brightness