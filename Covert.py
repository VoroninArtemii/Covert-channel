import argparse
import socket
import struct
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description='Covert channel emulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--filename', help='Data to transfer via covert channel', required=True, dest='filename', type=str, default='test')
    return parser.parse_args()

def encode_data(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return ''.join(format(byte, '08b') for byte in data)

def send_packet(data_bit):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW, socket.IPPROTO_ICMPV6)
    dest_ip = '::1'
    src_ip = '::1'
    hop_limit = 64 if data_bit == '0' else 128
    packet = struct.pack('!BBHHH', 128, 0, 0, 0, 0)
    try:
        sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_UNICAST_HOPS, hop_limit)
        sock.sendto(packet, (dest_ip, 0))
    except Exception as e:
        print(f"Error sending packet: {e}")

def main():
    args = parse_arguments()
    filename = args.filename
    data_bits = encode_data(filename)
    for bit in data_bits:
        send_packet(bit)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
