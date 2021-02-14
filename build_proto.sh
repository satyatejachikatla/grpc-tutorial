#!/bin/bash

. ./envrc.sh
if [ ! $? == 0 ]; then
	exit
fi

python3 -m grpc_tools.protoc \
-I$TOPDIR/src/ \
--python_out=$TOPDIR/src/ \
--grpc_python_out=$TOPDIR/src/ \
$TOPDIR/src/CalculatorService.proto
