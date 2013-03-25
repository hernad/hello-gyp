#!/bin/bash

GYP_GENERATORS=ninja gyp hello.gyp --toplevel-dir=`pwd` --depth=0

echo http://n8.io/converting-a-c-library-to-gyp/

ninja -v -C out/Default/ all

echo "---run----"
out/Default/h1
