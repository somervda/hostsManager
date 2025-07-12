from hosts_updater import HostsUpdater

hu=HostsUpdater()
piaiIp =(hu.resolve_host("piai"))
print("piai:", piaiIp)
hu.add_or_update_host("proxyai",piaiIp)
print("hosts file updated with proxyai entry.")
