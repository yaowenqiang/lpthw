#!/usr/bin/env bash

UNAME='uname -a'
printf "Gathering system information with $UNAME command: \n\n"
$UNAME

DISKSPACE='df -h'
printf "Gathering system information with $DISKSPACE command: \n\n"
$DISKSPACE
