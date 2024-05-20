#!/bin/bash
#apt update
#apt upgrade
pkg install git build-essential cmake -y
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build
cd xmrig/build
cmake .. -DWITH_HWLOC=OFF && make -j$(nproc)
#./xmrig -o pool.hashvault.pro:443 -u 43KkmRcqPvN8fYXNxX5CeV1NWZ5wunUTSVocU7ArEjQG9aDoHsM8xf665Z9K5Dwsm34tdsJuTXboji9mgPzSRrmHG8cAf2x -p NamAndroidMining -k --coin monero --tls
./xmrig --donate-level=0 -o stratum+tcp://randomxmonero.auto.nicehash.com:9200 --coin=monero -u 3LHpkPBNRwXhJ7ttGYD5ToWmGgQ1PE7zGe.yhbul7aaguviak4 -k --nicehash
