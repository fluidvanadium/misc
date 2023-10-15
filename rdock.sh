#/bin/bash

G=$(git rev-parse --show-toplevel 2> /dev/null)

function dedot_dir {
  DEDOT=$(echo "$1" | sed 's/dotfiles\/docks/./')
  echo $DEDOT
  mkdir -p $DEDOT
  mkdir -p $HOME/tmp/dockedout/$DEDOT
}
function dedot_ln {
  DEDOT=$(echo "$1" | sed 's/dotfiles\/docks/./')
  mv --backup $DEDOT ~/tmp/dockedout/$DEDOT
  echo $DEDOT
  ln -s $1 $DEDOT
}
export -f dedot_dir
export -f dedot_ln

echo "creating dock directories and"
echo "creating backup docks in ~/tmp/dockedout"
find $G/docks -type d -exec bash -c 'dedot_dir $0' {} \;

echo "moving in-the-way docks to ~/tmp/dockedout"
echo "... and softlinking all docks"
mkdir -p ~/tmp/dockedout
find $G/docks -type f -exec bash -c 'dedot_ln $0' {} \;
