#!/bin/bash
sudo tcpdump -i lo 'icmp6[0] == 128' -w captured_traffic.pcap > /dev/null 2>&1 &
pid=$!
sleep 1
python3 Covert.py -f Data.txt
sleep 1
sudo kill $pid
python3 Capture.py
