import paramiko
import os
import getpass

def main():

    hostname = '172.16.182.128'
    username = 'azurion-vm'
    password = 'azurion'
    
    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)

    stdin,stdout,stderr=ssh_client.exec_command('ls')
    print(stdout.readlines())

    ssh_client.close()

def sshConnect(hostname,username,password,remotepath,localpath):

    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)

    stdin,stdout,stderr = ssh_client.exec_command('[ -f '+remotepath+' ] && echo "Found" || echo "Not found"')
    if stdout.readlines()[0] == 'Found\n':

        #/home/students/Desktop/file.txt
        basePath = '/home/'+getpass.getuser()+'/'
        os.chdir(basePath)
        ftp_client = ssh_client.open_sftp()
        ftp_client.get(remotepath,localpath)
        ftp_client.close()

    else:
        print('File does not exist on the server')

    ssh_client.close()


if __name__ == '__main__':
    main()
