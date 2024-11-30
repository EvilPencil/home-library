### Debian 11 “Bullseye” Server Set Up for Django 4.2 LTS
 
> **Note:** The numeral or hash sign (#) indicates that the command needs to be run as root, whereas the dollar sign ($) shows that the command should be run as a regular user. 


##### 1. ( Update server )
```
# dpkg-reconfigure tzdata
# dpkg-reconfigure locales
# apt update && apt upgrade -y

# apt install sudo vim curl wget net-tools -y
````
##### 2. (Create user, setup SSH)
```
# adduser django
# adduser django sudo

# ssh-copy-id django@ip_server
```
*Append to* `/etc/ssh/sshd_config`

    PermitRootLogin prohibit-password
    AllowUsers django
    PubkeyAuthentication yes
    PasswordAuthentication no


##### 3. ( Install Python 3.10.15, Update pip, Install virtualenv )


    $ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev -y

```
$ mkdir build ;\
  cd build ;\
  wget https://www.python.org/ftp/python/3.10.15/Python-3.10.15.tgz ;\
  tar xvf Python-3.10.15.tgz ;\
  cd Python-3.10.15 ;\
  ./configure --enable-optimizations --prefix=/usr/local ;\
  make ;\
  sudo make altinstall

$ python3.10 -m pip install -U pip
$ python3.10 -m pip install virtualenv
```
> **Note:** To make the default version of Python 3.10.15, run this:

    $ sudo ln -s /usr/local/bin/python3.10 /usr/local/bin/python

##### 4. ( Install MC )

    $ sudo apt install mc

*Append to* `~/.profile`

    # In order to stay in the same directory when exiting the program
    alias mc='source /usr/lib/mc/mc-wrapper.sh

*Ok, now we can pull our project from Git repository (or create own), create and activate Python virtual environment:*

##### 5. ( Install GIT )

    $ sudo apt install git

*Append to* `~/.bashrc`

    # Show a current active git branch in the shell prompt
    export PS1='\t \[\033[01;32m\]\u\[\033[01;34m\] \w\[\033[01;33m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '

    # Shortcat for the pretty git log. Can be extended with the commit count parameter (git g -10, git g -35)
    git config --global alias.g 'log --all --decorate --oneline --graph'
    
```
$ cd ~/build
$ git clone project_git
$ cd project_git
$ python3.10 -m virtualenv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ deactivate

```
