#!/bin/bash

GYP_GENERATORS=ninja gyp hello.gyp --toplevel-dir=`pwd` --depth=0


ninja -C out/Default/ all
