import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

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
    
def main():
        ip_addr = '50.76.53.27'
        username = 'pyclass'
        password = '88newclass'
    
        remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        output = login(remote_conn, username, password) 
        print output

        time.sleep(1)
        output = remote_conn.read_very_eager()
        
        output = send_command(remote_conn, 'terminal length 0')
        output = send_command(remote_conn, 'show ip int brief')
        print output
    
        remote_conn.close()

if __name__ == "__main__": 
     main()
