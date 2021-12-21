#!/usr/bin/env python
##########################################
#           Print song lyrics            #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


b = "Birds in the Trap Sing Mcknight"
a = "ASTROWORLD"
t = "Travis Scott"

class songs:
    def __init__(self, artist, title, album):
        self.titel = title
        self.artist = artist
        self.album = album
    def play(self):
        print("")
        print(self.artist, "-", self.titel) #Hier word eerst de artiest dan een streepje en dan de titel gepriny
        print("(",self.album,")") #Hier word het album geprint tussen haakjes
        print("")

# FUNCTIONS
def main():
    sicko_mode = songs(t, "SICKO MODE", a) #Hier defineer ik het de liedjes
    goosebumps = songs(t, "goosebumps", b)
    butterfly = songs(t, "BUTTERFLY EFFECT", a)
    putp = songs(t, "pick up the phone", b)

    print("1 = SICKO MODE")
    print("2 = goosebumps")
    print("3 = BUTTERFLY EFFECT")
    print("4 = pick up the phone")
    try:
        choice = int(input('Choose a song (1, 2, 3 or 4): '))
    except ValueError:
        print("Please insert a number!")
        main()
    if choice == 1:
        sicko_mode.play()
        f = open("assets/songs/sickomode.txt", "r")
        print(f.read())

    elif choice == 2:
        goosebumps.play()
        f = open("assets/songs/goosebumps.txt", "r")
        print(f.read())

    elif choice == 3:
        butterfly.play()
        f = open("assets/songs/butterfly.txt", "r")
        print(f.read())

    elif choice == 4:
        putp.play()
        f = open("assets/songs/pick up the phone.txt", "r")
        print(f.read())
    else:
        print("Please give a number between 1-4!")
        main()
    f.close()



if __name__ == '__main__':
    main()
