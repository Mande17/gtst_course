kali linux + Gnom desktop environment
kali linux previously known as Backtrack
Phase of hacking 
    1. Information gathering 
    2. Scanning 
    3. Gain access
    4. Maintaing access(post exploitation)
    5. Clearing track
=============TOOLS===============
-Information Gathering
    maltego,recon-ng,nmap
-Vlunerability Analysis
    nikito,nmap
-Web application Analysis
    burbsuit,sqlmap,zap,wpscan
-Database Assesment
    jSQL injection,sqlmap
-Password Attack
    hashcat,john
-Wireless Attack
    aircrack-ng,wifite,reaver
-Reverse Engineering
    apktool,ghidra
-Exploiting Tools
    Metasploit
-Sniffing and Spoofing(listening or hijacking network)
    wireshark
-Post exploitation(Maintaing access)
    backdoor
-Forensic
    hashdeep
-Reporting Tool
    record my desktop
-Social engineering
    Maltego,backdoor
-System service(buttons used to start some services)
    beef(start+stop), dradis(start+stop)
-Usually used applications
=========================================
Folder managers
    1. Dolphin
    2. Thunar
    3. Nautilus

Linux uses shell(Terminal) to communicate with kernel
    terminal have 5 parts
        username, hostname, current_directory, privillage, command_place
    ----------------------------------------------------------
    -(Username@Hostname(Machine_name))-[Current_directory]
   |
    -$
    ------------------------------------------------------------------
    privilage $-(user), #-(root)
command = is small programm that perform one task
=======================================================
LS = List information about the FILE and directory
ls - l list with more information
ls - a list including hidden files
ls - R recursive, list including files in the folder
=======================================================
CD = Chenge directory
~ home dorectory
/ root directory
cd/ = root
cd = home 
cd .. = 1x back
cd ../.. 2x back 
cd foldername
=======================================================
pwd = print working directory
=======================================================
echo = used to display line of text
echo "your text here" > text.txt //it create text.txt file with "your text here"
echo "appent text to the file text.txt" >> text.txt
=======================================================
cat = it used to show content in file
cat/head/tail/less
====================================================
touch = it creates file with empty content
==============================================
mkdir = it create folder 
mkdir Newfolder
===============================================
clear = ctrl+l = clear window
==============================================
rm = remove(delete) file
rm -r = recursive (4folders) *for directory
rm -i = for prompt(ask)
rm -f = force delete
rm -rf 
================================================
CP = copy file
MV = move file
=================================================
GREP = global search for regular expression 
grep [option] pattern [files]
grep -i case insensative 
grep -c count numbers 
grep -l display file name that text exist
grep -R search text in folder
grep -v to display with out this term(exclusive)
grep -n to diplay the term find number 
==================================================
WC = word count = used to find number of lines, word count and byte and characters count in
specified file
    Line(-l) word(-w) byte(-c)
==================================================
Multiple command executions=====using 3 methods
    1. And(&&)--run both commands 
    2. Or(||)--run either first command or second(if first )
    3. Pipeing(|)


