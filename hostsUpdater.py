import os
import socket
import re

class HostsUpdater:
    def __init__(self, hosts_file):
        self.hosts_file = hosts_file

    def update_host(self, hostname, ip_address):
                # Check valid parameters are passed
        if not socket.inet_pton(socket.AF_INET, ip_address):
            raise ValueError("Invalid IPv4 address: {}".format(ip_address))
            
        if not self.is_valid_hostname(hostname):
            raise ValueError("Invalid hostname: {}".format(hostname))

        with open(self.hosts_file, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if hostname in line:
                lines[i] = f'{ip_address} {hostname}\n'
                break
        else:
            lines.append(f'{ip_address} {hostname}\n')

        with open(self.hosts_file, 'w') as f:
            for line in lines:
                f.write(line)

    def is_valid_hostname(self,hostname):
        if hostname[-1] == ".":
            hostname = hostname[:-1] # Strip exactly one dot from the right, if present
        if len(hostname) > 253:
            return False

        labels = hostname.split(".")
        # The TLD (last label) should not be all-numeric
        if re.match(r"^[0-9]+$", labels[-1]):
            return False

        # Each label must conform to the hostname rules:
        # - Cannot start or end with a hyphen
        # - Can contain letters (a-z, A-Z), numbers (0-9), and hyphens
        # - Length between 1 and 63 characters
        allowed = re.compile(r"^(?!-)[a-zA-Z0-9-]{1,63}(?<!-)$")
        
        return all(allowed.match(label) for label in labels)


    def resolve_host(self, hostname):
        ip_address = socket.gethostbyname(hostname)
        return ip_address

hu=HostsUpdater("hosts.")
piaiIp =(hu.resolve_host("piai"))
print("piai:", piaiIp)
hu.update_host("proxyai.local",piaiIp)
print("hosts file updated with proxyai.local entry.")
hu.update_host("proxyai.lan",piaiIp)
print("hosts file updated with proxyai.lan entry.")
