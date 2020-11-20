 #a router needs to receive N data packets (represent them as strings), and needs to transmit one of the N packets,
 #uniformly at random (i.e. each packet should have an equal probably of being transmitted

def send_packet(packet, N):
    #we are not changing the address of all_packets, so we don't need to global all_packets

    all_packets.append(packet)

    if (len(all_packets) == N)
        n = int(N * random.random())
        return all_packets[n]

if __name__ == "__main__":
    all_packets = []
    print(send_packet("abc", 3))
    print(send_packet("cde", 3))
    print(send_packet("aaa", 3))