#!/bin/bash

. ./envrc.sh
if [ ! $? == 0 ]; then
	exit
fi


mkdir $TOPDIR/stage
cp -r $TOPDIR/src/* $TOPDIR/stage/