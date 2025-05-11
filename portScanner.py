import socket
# from socket import Server
import termcolor

#scans multiple ip addresses
def scan_ports(target, ports):
    print(termcolor.colored(("\n Scanning Targets"),'green'))

    for port in range(1, ports):
        scan(target, port)
#scans single ip address
def scan(ipaddr, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddr, port))
        print("[+] Port opened "+str(port))
        sock.close()
    except:
        pass

#main()
targets = input("[*] Enter Targets to Scan IP (Split by ,): ")
ports = int(input("[*] Enter How Many Ports to Scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"),'green'))
    for ipaddr in targets.split(','):
        scan_ports(ipaddr.strip(), ports)
else:
    scan_ports(targets, ports)