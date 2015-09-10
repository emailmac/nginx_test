#!/bin/sh	
# Compile nginx standalone without root access

SRC_DIR=~/src
INSTALL_DIR=~/programs/nginx

mkdir -p $INSTALL_DIR
mkdir -p $SRC_DIR
cd $SRC_DIR

# PCRE dependency - we'll compile against this statically
wget http://downloads.sourceforge.net/project/pcre/pcre/8.37/pcre-8.37.tar.gz
tar -xzvf pcre-8.37.tar.gz

# Grab nginx
wget http://nginx.org/download/nginx-1.8.0.tar.gz
tar -xzvf nginx-1.8.0.tar.gz

wget http://zlib.net/zlib-1.2.8.tar.gz
tar -xzvf zlib-1.2.8.tar.gz

# Compile it
cd nginx-1.8.0
./configure --prefix=$INSTALL_DIR \
--with-pcre=$SRC_DIR/pcre-8.37 \
--with-zlib=$SRC_DIR/zlib-1.2.8 \
--with-http_auth_request_module

make
make install

