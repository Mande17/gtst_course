    Linux File Herarchy 
system files stored in 1: Windows -> Local Disk(C:)
                       2: Linux -> Root Directory(/)
        FILE STRUCTURE IN DETAIL
        ======================== 
1) /(ROOT) -> root directory 
2) /bin - binary execuables
3) /boot -> boot loader files
4) /dev -> Essential Device files
5) /etc -> et cetra -> configuration files 
6) /home -> home directory [~]
7) /lib -> Libraries essential for the binaries /bin & /sbin
8) /media -> Mount point for removable media such as CD-ROMs
9) /mnt -> Temporarily mounted files 
10) /opt -> optional application software packages 
11) /sbin -> Essential system binaries 
12) /tmp -> Temporary files 
13) /usr -> User utilities 
        TEXT EDITORS FOR LINUX
        ======================
VIM, NANO, Emacs, NeoVim
        GRAPHIC TEXT EDITORS
        --------------------
Sublime, VSCode, Gedit, Pluma
VIM = it was called VI in UNIX
    it is a powerfull 
    it is hard to learn (specially for window users)
    it has 2 modes ------ 1 command mode (By pressing ESC)
                    | 
                     ---- 2 input mode (By pressing I)
    COMMANDS
    :w+Enter ======================== Save
    :q+Enter ======================== Quit
    :wq!+Enter ====================== save and force quit
    :undo+Enter or :u+Enter ========= undo
    :%!+your_commande =============== to execute your command
NANO = 
    COMMANDS
    --------
    Ctrl+S === Save         Ctrl+Shift+C ====== Copy
    Ctrl+X === Exit         Ctrl+Shift+X ====== Cut
    Alt+U ==== Undo         Ctrl+Shift+V ====== Paste
    Alt+E ==== Redo
==============================================================
        LINUX USER MANAGMENT 
==============================================================
-On computer system ,  aperson who uses the computer is called "User"
-Every users have group
-"whoami" command used to know name in Linux 
- there are two types of users .--- 1) Root - id = 0
                               |
                               '--- 2) Normal user - is (0-999)
    ======================================
    ==== Creating users in Linux =========
    ======================================
    1) Useradd -> simple 
        $ sudo useradd username
    2) Adduser -> detailed 
        $ sudo adduser username
    ======================================
    > The user files are stored in    ====  /etc/passwd
    > The user passwords are stored in ===  /etc/shadow

    