from utils import *

inp = get_data(year=2021, day=16)


def solve1(d):
    inp = d.strip().lower()
    binary = bin(int(inp, base=16))[2:].zfill(len(inp)*4)
    
    def parse_packet(packet):
        if len(packet) < 3 and packet.count("1") == 0: return 0 
        assert len(packet) > 6, "packet too short"

        V = int(packet[0:3], 2)
        T = int(packet[3:6], 2)
        if T == 4:
            idx = 6
            while packet[idx] != "0": 
                idx += 5
            return V + parse_packet(packet[idx+5:])
        else:
            I = int(packet[6], 2)
            if I == 0:
                return V + parse_packet(packet[22:])
            else:
                return V + parse_packet(packet[18:])
            
    result = parse_packet(binary)
    return result


def solve2(d):
    inp = d.strip().lower()
    binary = bin(int(inp, base=16))[2:].zfill(len(inp)*4)
    
    def parse_packet(packet):
        assert len(packet) > 6, "packet too short"
        
        T = int(packet[3:6], 2)
        
        if T == 4:
            idx = 6
            literal = ""
            while True:
                literal += packet[idx+1:idx+5]
                idx += 5
                if packet[idx-5] == "0": break
            return int(literal, 2), idx
        else:
            I = int(packet[6], 2)
            subpackets = []
            if I == 0:
                idx = 22
                L = int(packet[7:22], 2)
                while idx - 22 != L:
                    subpacket, length = parse_packet(packet[idx:])
                    subpackets.append(subpacket)
                    idx += length
            else:
                idx = 18
                L = int(packet[7:18], 2)
                while len(subpackets) != L:
                    subpacket, length = parse_packet(packet[idx:])
                    subpackets.append(subpacket)
                    idx += length
                    
            match T:
                case 0:
                    return sum(subpackets), idx
                case 1:
                    return math.prod(subpackets), idx
                case 2:
                    return min(subpackets), idx
                case 3:
                    return max(subpackets), idx
                case 5:
                    return int(subpackets[0] > subpackets[1]), idx
                case 6:
                    return int(subpackets[0] < subpackets[1]), idx
                case 7:
                    return int(subpackets[0] == subpackets[1]), idx
        
    result = parse_packet(binary)[0]
    return result


s = """A0016C880162017C3686B18A3D4780
"""
s2 = """9C0141080250320F1802104A08
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s2))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
