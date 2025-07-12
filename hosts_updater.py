import os
import socket

class HostsUpdater:
    def __init__(self):
        self.hosts_file = 'hosts'
    
    def add_or_update_host(self, name, ip_address):
        # Check valid parameters are passed
        if not socket.inet_pton(socket.AF_INET, ip_address):
            raise ValueError("Invalid IPv4 address: {}".format(ip_address))
            
        if not name.isalnum():
            raise ValueError("Invalid hostname: {}".format(name))

        with open(self.hosts_file, 'a+') as file:
            lines = file.readlines()
            found = False
            for line in lines:
                if line.startswith(ip_address):
                    line = f"{ip_address} {name}\n"
                    found = True
            if not found:
                lines.append(f"{ip_address} {name}\n")
            file.seek(0)
            file.truncate()
            file.write(''.join(lines))


    def resolve_host(self, hostname):
        ip_address = socket.gethostbyname(hostname)
        return ip_address