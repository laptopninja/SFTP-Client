import tkinter as tk
from tkinter import ttk
import sshaccess

known_host = {'conf1':{'hostname':'172.16.182.128','username':'azurion-vm','password':'azurion'},
            'conf2':{'hostname':'172.16.30.130','username':'students','password':'students'}}

def callbackFunc(event):
    usernameText['text'] = known_host[configDropdown.get()]['username']
    hostnameText['text'] = known_host[configDropdown.get()]['hostname']
    passwordText['text'] = known_host[configDropdown.get()]['password']

def onSubmit():
    if len(localFilepathText.get()) == 0 and len(remoteFilepathText.get()) == 0:
        print("Empty field detected")
    else:
        username = known_host[configDropdown.get()]['username']
        hostname = known_host[configDropdown.get()]['hostname']
        password = known_host[configDropdown.get()]['password']
        remotepath = remoteFilepathText.get()
        localpath = localFilepathText.get()
        sshaccess.sshConnect(username=username,hostname=hostname,password=password,remotepath=remotepath,localpath=localpath)


app = tk.Tk()
app.title('SSH Client')
app.geometry('325x300')

labelTop = tk.Label(app, text = "Config")
labelTop.grid(column=0, row=0)
configDropdown = ttk.Combobox(app, values=["conf1","conf2"],width='5')
configDropdown.grid(column=1, row=0, pady=(10,10),padx=(0,25))
configDropdown.current(0)
configDropdown.bind("<<ComboboxSelected>>", callbackFunc)

usernameLabel = tk.Label(app, text='Username')
usernameLabel.grid(column=0,row=1,padx=(25,25))
usernameText = tk.Label(app, text=known_host[configDropdown.get()]['username'])
usernameText.grid(column=1,row=1,pady=(5,5),padx=(0,30))

hostnameLabel = tk.Label(app, text='Hostname')
hostnameLabel.grid(column=0,row=2,padx=(25,25))
hostnameText = tk.Label(app, text=known_host[configDropdown.get()]['hostname'])
hostnameText.grid(column=1,row=2,pady=(5,5),padx=(0,30))

passwordLabel = tk.Label(app, text='Password')
passwordLabel.grid(column=0,row=3,padx=(25,25))
passwordText = tk.Label(app, text=known_host[configDropdown.get()]['password'])
passwordText.grid(column=1,row=3,pady=(5,5),padx=(0,30))

remoteFilepathLabel = tk.Label(app, text='File path:')
remoteFilepathLabel.grid(column=0,row=4,padx=(25,25))
remoteFilepathText = tk.Entry()
remoteFilepathText.grid(column=1,row=4,pady=(5,5),padx=(0,30))

localFilepathLabel = tk.Label(app, text='Download to:')
localFilepathLabel.grid(column=0,row=5,padx=(25,25))
localFilepathText = tk.Entry()
localFilepathText.grid(column=1,row=5,pady=(5,5),padx=(0,30))

submitBtn = tk.Button(app, text='Submit', command= onSubmit)
submitBtn.grid(column=1,row=6,pady=(10,0))

app.mainloop()
