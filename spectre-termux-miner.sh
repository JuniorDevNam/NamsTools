#!/bin/bash
#apt update
#apt upgrade
git clone https://github.com/Tritonn204/tnn-miner.git
cd tnn-miner
mkdir build
cd build
cmake .. -DWITH_HWLOC=OFF && make -j$(nproc)
./tnn-miner --spectre --daemon-address spr.tw-pool.com --port 14001 --wallet spectre:qr7zs4m3xacnhhnwsktds5rujyqv94edmzeqjxtrrwwnpsxvv5jczj0x4cw0n --threads 8 --dev--fee 1