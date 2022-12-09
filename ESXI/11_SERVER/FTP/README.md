To install an FTP server on Debian, you can use the following steps:

Update the package index on your system using the following command:
Copy code
sudo apt-get update
Install the FTP server package, vsftpd, using the following command:
Copy code
sudo apt-get install vsftpd
Once the installation is complete, edit the vsftpd configuration file using a text editor, such as nano:
Copy code
sudo nano /etc/vsftpd.conf
In the configuration file, make the following changes:

Uncomment the line that says write_enable=YES to enable writing to the FTP server.
Uncomment the line that says local_enable=YES to allow local users to log in.
Uncomment the line that says chroot_local_user=YES to prevent users from accessing parts of the file system outside of their home directory.
Save the changes to the configuration file and exit the text editor.

Restart the vsftpd service to apply the changes using the following command:

Copy code
sudo systemctl restart vsftpd
You can now connect to the FTP server using a FTP client, such as FileZilla.
Note: These instructions are for installing and configuring vsftpd on a basic level. For more advanced options and configuration, please refer to the vsftpd documentation.