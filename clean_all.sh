#!/bin/bash

. ./envrc.sh
if [ ! $? == 0 ]; then
	exit
fi


find $TOPDIR | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

rm -f $TOPDIR/src/CalculatorService_pb2*.py
rm -rf $TOPDIR/stage
