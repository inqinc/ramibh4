#!/bin/bash
T1=$1
T2=$2
if [ "$T1" = "$T2" ]; then
  echo expression evaluated as true
else
  echo expression evaluated as false
fi
