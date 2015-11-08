#!/usr/bin/env python

import telnetlib
import time
import snmp_helper
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6
SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def send_command(remote_conn, cmd):
        cmd = cmd.rstrip()
        remote_conn.write(cmd + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()

def login(remote_conn, username, password):
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output
        
def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")

def main():
            ip_addr = raw_input("IP address: ")
            ip_addr = ip_addr.strip()
            username = 'pyclass'
            password = getpass.getpass()
            community_string = getpass.getpass(prompt="Community string: ")
            pynet_rtr1 = (ip_addr, community_string, 7961)
            pynet_rtr2 = (ip_addr, community_string, 8061)
            remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
            output = login(remote_conn, username, password)
            print output

            for a_device in (pynet_rtr1, pynet_rtr2):

                print "\n"
                for the_oid in (SYS_NAME, SYS_DESCR):
                    snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
                    output = snmp_helper.snmp_extract(snmp_data)

                    print output
                print ""

            print

if __name__ == "__main__":
    main()
