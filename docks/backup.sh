mount /dev/nvme0n1p1 /exp
rsync --progress -a leaves/ /exp/leaves/
rsync --progress -a dotfiles/ /exp/dotfiles/
rsync --progress -a ZINGO/ /exp/ZINGO/
sudo umount /exp
