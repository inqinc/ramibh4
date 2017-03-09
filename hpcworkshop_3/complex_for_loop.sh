#!/bin/bash
LIST=(`ls /home/$USER`)
for NAME in ${LIST[@]}; do echo $NAME ; done
for NAME in ${LIST[@]}; do echo $NAME | tr '[a-z]' '[A-Z]'; done

