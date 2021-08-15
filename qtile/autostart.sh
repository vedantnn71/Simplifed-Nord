#!/bin/bash

# Turn Numlock Key ON
numlockx &

# My Compositor
picom &

# Randomly set a background
nitrogen --random --set-zoom-fill

# Session Manager
lxsession &

# Notification Daemon
dunst &

# Hide mouse cursor when not needed
unclutter &

# My Screen Saver
light-locker --lock-after-screensaver=0 --no-lock-on-suspend --no-lock-on-lid --no-idle-hint &

# For Animation on TWMs
flashfocus &

# Mercy on my eyes
redshift-gtk &

# Eww Daemon for some of its widgets
eww daemon &
