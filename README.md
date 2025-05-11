# Description

This project demonstrates a covert communication channel using ICMPv6 packets and the IPv6 hop limit field to encode and decode binary data.

## File Descriptions

### `Covert.py`
This script encodes the contents of a specified file into binary and sends it covertly using ICMPv6 packets. The hop limit of the packets is used to represent binary data:
- **Hop limit 64** → represents binary `0`
- **Hop limit 128** → represents binary `1`

It takes the input file (specified via the `-f` option) and transmits each bit as an ICMPv6 packet with the appropriate hop limit.

### `Capture.py`
This script listens for ICMPv6 packets and decodes the binary data from the hop limit values. The hop limit of each captured packet is checked, and:
- A hop limit of `64` is decoded as a binary `0`
- A hop limit of `128` is decoded as a binary `1`

It reconstructs the binary message by reading packets from a saved `.pcap` file (`captured_traffic.pcap`).

### `Data.txt`
This file contains the secret message to be covertly transmitted. It is read by `Covert.py`, converted to binary, and sent over the covert channel.

### `Run.sh`
This bash script automates the entire process:
1. Starts packet capture with `tcpdump` to monitor ICMPv6 traffic and save it to `captured_traffic.pcap`.
2. Runs `Covert.py` to send the message stored in `Data.txt` over the network.
3. Stops the packet capture.
4. Runs `Capture.py` to decode the captured packets and print the decoded binary message.
