mount /dev/nvme0n1p1 /exp
rsync --progress -a --copy-links leaves/ /exp/leaves/
sudo umount /exp
