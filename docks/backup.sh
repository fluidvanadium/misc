mount /dev/sda2 drives/chip_disk
rsync --progress -a --copy-links leaves/ drives/chip_disk/leaves/
sudo umount /dev/sda2
