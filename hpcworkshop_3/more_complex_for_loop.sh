#!/bin/bash
LIST=(`ls /home/$USER/hpcworkshop_3/*sh`)
for NAME in ${LIST[@]}; do echo $NAME | awk '{split($0,a,"\\.sh") ;print a[1]".bash"}' ; done
