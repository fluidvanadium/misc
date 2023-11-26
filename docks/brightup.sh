P=$(cat /sys/class/backlight/amdgpu_bl1/brightness)
P=$((P+$@))
echo "$P" > /sys/class/backlight/amdgpu_bl1/brightness
