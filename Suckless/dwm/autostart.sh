#! /bin/bash 
picom &
nitrogen --restore &
dwmblocks &
xfce4-power-manager &
xfce4-session &
emacs --daemon &
xautolock -time 10 -locker slock &
redshift &
