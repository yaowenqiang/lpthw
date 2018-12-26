import paramiko
import pprint

hostname = 'localhost'
port = '22'

username = 'vagrant'
password = 'vagrant'

if __name__ == '__main__':
    paramiko.util.log_to_file("paramkio.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print((stdout.read().decode('utf-8')))

    stdin, stdout, stderr = s.exec_command('hostname')
    print((stdout.read().decode('utf-8')))

    stdin, stdout, stderr = s.exec_command('who')
    print((stdout.read().decode('utf-8')))

    s.close()
