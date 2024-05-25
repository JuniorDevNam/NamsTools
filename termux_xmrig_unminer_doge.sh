pkg install git tsu build-essential cmake -y
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build
cd xmrig/build
cmake .. -DWITH_HWLOC=OFF && make -j$(nproc)
wget https://raw.githubusercontent.com/xmrig/xmrig/master/scripts/enable_1gb_pages.sh && chmod +x enable_1gb_pages.sh
sudo ./enable_1gb_pages.sh
./xmrig --cpu-priority=5 --cpu-no-yield --randomx-1gb-pages -o stratum+ssl://rx.unmineable.com:443 -k -u DOGE:DSbF5Nsq3NJLZ59gCZ7GpaR3hGRgCTYSFP.unmineable_android_miner --no-color --http-port=60070 -a rx