import paramiko
import os

hostname = 'localhost'
port = 22
dir_path = "/home/vagrant/"

username = 'vagrant'
password = 'vagrant'

if __name__ == '__main__':
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)

    for f in  files:
        print(f"Retrieving {f}")

    # sftp.get(os.path.join(dir_path, f))
    t.close()
