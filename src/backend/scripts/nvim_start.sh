#! /bin/zsh

P_PATH=$(poetry env info --path)
source $P_PATH'/bin/activate'
nvim .
