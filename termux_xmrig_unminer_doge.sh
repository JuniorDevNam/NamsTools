pkg install git build-essential cmake -y
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build
cd xmrig/build
cmake .. -DWITH_HWLOC=OFF && make -j$(nproc)
./xmrig -o stratum+ssl://rx.unmineable.com:443 -k -u DOGE:DSbF5Nsq3NJLZ59gCZ7GpaR3hGRgCTYSFP.unmineable_android_miner --no-color --http-port=60070 -a rx