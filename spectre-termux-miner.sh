#!/bin/bash
#apt update
#apt upgrade
pkg install git build-essential cmake clang libssl-dev libudns-dev libfmt-dev libc++-dev lld -y
git clone https://github.com/Tritonn204/tnn-miner.git
mkdir tnn-miner/build
cd tnn-miner/build
cmake .. -DWITH_HWLOC=OFF && make -j$(nproc)
./tnn-miner --spectre --daemon-address spr.tw-pool.com --port 14001 --wallet spectre:qr7zs4m3xacnhhnwsktds5rujyqv94edmzeqjxtrrwwnpsxvv5jczj0x4cw0n --threads 8 --dev--fee 1