# DCCN Project - File Transfer using an SSH Client

### Batch - A
### Group Members (Name - Roll no)
- Harsh Agarwal - 1
- Aman Agrawal -2
- Bhavya Ahir - 3
- Harshit Barot - 8
- Pranav Chitale - 12


## Concept

A GUI based application to simplify the process of file transfer using SSH. It removes the hassle of writing bash commands. Allows easy and fast transfer of local files. No prior knowledge of bash commands or SSH is required.Uses SFTP (SSH File Transfer Protocol) a secure file transfer protocol. It runs over the SSH protocol. It supports the full security and authentication functionality of SSH. Uses Paramiko a python library to provide client and server functionality. GUI is developed using Tkinter a python library for developing Graphical User Interface.

## Installation and Operation
1. Create a virtual environment.
	>virtualenv venv
	>source venv/bin/activate

2. Install the dependencies.
	>pip install -r requirements.txt
	
3. Run the SSH client script.
	>python3 SSHClient.py


## Dependencies

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

### Paramiko
Paramiko is a Python (2.7, 3.4+) implementation of the SSHv2 protocol, providing both client and server functionality. While it leverages a Python C extension for low level cryptography (Cryptography), Paramiko itself is a pure Python interface around SSH networking concepts.

### Tkinter
The tkinter package is a thin object-oriented layer on top of Tcl/Tk. To use tkinter, you don’t need to write Tcl code. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter outputs the fastest and easiest way to create the GUI applications.
