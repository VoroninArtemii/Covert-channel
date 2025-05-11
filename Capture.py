import subprocess

def decode_packet(packet):
    if 'hlim 64' in packet:
        return '0'
    elif 'hlim 128' in packet:
        return '1'
    return None

def main():
    process = subprocess.Popen(['sudo', 'tcpdump', '-r', 'captured_traffic.pcap', '-vvv'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data_bits = []
    for line in process.stdout:
        line = line.decode('utf-8')
        bit = decode_packet(line)
        if bit is not None:
            data_bits.append(bit)
    decoded_data = ''.join(data_bits)
    print("Decoded data (bits):", decoded_data)

if __name__ == "__main__":
    main()
