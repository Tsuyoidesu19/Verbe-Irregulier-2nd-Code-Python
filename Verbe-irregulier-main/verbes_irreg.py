#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import random
import os


def load_list():

    found_file=False

    verbes.clear()

    while found_file != True :

        n = input("""\t Quel liste veut tu apprendre ? 
        \t >>>""")

        found_file = os.path.exists("liste_%s.txt"%(n))

        if found_file == False :
            print("Ce fichier n'éxiste pas !")
        
    liste = open("liste_%s.txt"%(n), 'r')
    for line in liste:
        line = line.strip()
        verb_split = line.split(' ')
        inf = verb_split[0]
        pret = verb_split[1]
        past = verb_split[2]
        trad = verb_split[3]
        verbes[inf] = [pret,past,trad]
    print(verbes)


def score_final(score, counter):
    return("Vous avez %d réponses de juste sur %d") % (score, (counter*3))


def infinitif():
    global counter
    global score
    counter = 0
    score = 0
    tour_de_liste = 0
    list_random=list(verbes.items())

    random.shuffle(list_random)

    while tour_de_liste < numb :

        verb, (pret, past, trad) = list_random[counter]
        lst = []
        lst.append(verb)
        lst.append(pret)
        lst.append(past)
        lst.append(trad)

        print("Le verbe à l'infinitif est le suivant '%s'" % (lst[0]))

        reponsepret = input("Quel est son prétérit? >>> ")
        if reponsepret == lst[1]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[1])

        reponsepp = input("Quel est son participe passé? >>> ")
        if reponsepp == lst[2]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[2])

        reponsetrad = input("Quel est sa traduction Française? >>> \033[0m")
        if reponsetrad == lst[3]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[3])

        counter += 1
        if len(list_random) == counter :
            tour_de_liste += 1
        print(score_final(score, counter))


def traduction():
    global counter
    global score
    counter = 0
    score = 0
    tour_de_liste = 0
    list_random=list(verbes.items())

    random.shuffle(list_random)

    while tour_de_liste < numb :

        verb, (pret, past, trad) = list_random[counter]
        lst = []
        lst.append(verb)
        lst.append(pret)
        lst.append(past)
        lst.append(trad)

        print("La traduction Française est la suivante '%s'" % (lst[3]))

        reponseinf = input("Quel est son infinitif en Anglais? >>> ")
        if reponseinf == lst[0]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[0])

        reponsepret = input("Quel est son prétérit? >>> ")
        if reponsepret == lst[1]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[1])

        reponsepp = input("Quel est son participe passé? >>> ")
        if reponsepp == lst[2]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[2])

        counter += 1
        if len(list_random) == counter :
            tour_de_liste += 1
        print(score_final(score, counter))



verbes = {}

load_list()

while True:


    rand = random.SystemRandom().choice(list(verbes.items()))
    verb, (pret, past, trad) = rand
    # print "Le verbe %s se conjugue au prétérit par %s, au participe passé par %s et se traduit par %s" % (verb, pret, past, trad)
    lst = []
    lst.append(verb)
    lst.append(pret)
    lst.append(past)
    lst.append(trad)

    print("""\n Ce court programme propose d'étuditer les verbes irrégliers de la
    langue Anglaise.
    \nDeux modes de jeu sont proposés :

    \t soit le programme va afficher le verbe irrégulier à l'infinitif et vous
    \tdevrez trouver son prétérit, son participe passé et sa traduction en Français.
    """)

    print("Par exemple : si le verbe '%s' est proposé, il faudra répondre '%s', '%s' et '%s'" %(lst[3], lst[0], lst[1], lst[2]))

    print("""
    \t soit le programme va afficher la traduction du verbe en Français et vous 
    \t devrez dans ce cas la, trouver son infinitif, son prétérite et son participe passé.
    """)

    print("Par exemple : si le verbe '%s' est proposé, il faudra répondre '%s', '%s' et '%s'" %(lst[0], lst[1], lst[2], lst[3]))
    print("\n")


    jeu = input("""\t Si vous souhaitez jouer avec l'infinitif du verbe merci de tapez 1
    \t Si vous souhaitez jouer avec la traduction Française du verbe merci de tapez 2  
    \t Si vous souhaitez changer de liste tapez 3
    \t Si vous souhaitez quitter tapez 4
    \t >>> """)

    if jeu == "1":
        numb = input("\t Combien de fois souhaitez vous faire la liste ? >>>  ")
        numb = int(numb)
        infinitif()
    elif jeu == "2":
        numb = input("\t Combien de fois souhaitez vous faire la liste ? >>>  ")
        numb = int(numb)
        traduction()
    elif jeu == "3":
        load_list()
    elif jeu == "4":
        break