pkg install git build-essential cmake -y
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build
cd xmrig/build
cmake .. -DWITH_HWLOC=OFF && make -j$(nproc)
./xmrig --cpu-priority=5 --cpu-no-yield --randomx-1gb-pages -o stratum+ssl://rx.unmineable.com:443 -k -u DOGE:DSbF5Nsq3NJLZ59gCZ7GpaR3hGRgCTYSFP.unmineable_android_miner_2 --no-color --http-port=60070 -a rx