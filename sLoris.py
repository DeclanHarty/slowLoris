import socket
import argparse

def main():

    parser = argparse.ArgumentParser("Slow Loris Test")

    #parser.add_argument('address')
    #parser.add_argument('port')
    #parser.add_argument('num_of_sockets')

    #args = parser.parse_args()

    #address = args.address
    #port = int(args.port)
    #num_of_sockets = int(args.num_of_sockets)
    

    address = 'declanharty.github.io'
    num_of_sockets = 3

    sockets = init_sockets(address, num_of_sockets)

    close_sockets(sockets)




    # socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # socket1.connect( ("declanharty.github.io", 443)) 
    # print("Connection Successful...")
    
    # content = 3

    # socket1.send(content.to_bytes(8, 'big'))
    # print("Sent stuff...")
    # socket1.close()
    # print("Socket has been closed...")

def init_sockets(address, num_of_sockets):
    content = 3
    target = (address, 80)
    sockets = [None] * num_of_sockets
    for num in range(num_of_sockets):
        sockets[num] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sockets[num].connect(target)
            sockets[num].send(content.to_bytes(8, 'big'))
            print("Socket Connected...")
        except:
            print("Socket Connection Failed...")

    return sockets

def close_sockets(sockets):
    for socket in sockets:
        socket.close()

    print("All Sockets Closed...")




main()