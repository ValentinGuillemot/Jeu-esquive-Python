from tkinter import*
import random

#**********************************

def déplacement(event) :
    c = can.coords(joueur)
    if event.keysym == 'Right' and c[0]+25 < 500 :
        can.move(joueur, 5, 0)
    if event.keysym == 'Left' and c[0]-5 > 0 :
        can.move(joueur, -5, 0)
    if event.keysym == 'Up' and c[1]-5 > 0 :
        can.move(joueur, 0, -5)
    if event.keysym == 'Down' and c[1]+25 < 400 :
        can.move(joueur, 0, 5)

#***********************************

def mouvement() :
    global jeu, joueur, a, b, c, d, boss, score, vxa, vya, vxb, vyb, vxc, vyc, vxd, vyd, vxboss, vyboss, echec, f
    if jeu :
        bouton.config(state = DISABLED, text = 'En jeu', disabledforeground='green')
        j = can.coords(joueur)
        place_a = can.coords(a)
        place_b = can.coords(b)
        place_c = can.coords(c)
        place_d = can.coords(d)
        place_f = can.coords(boss)
        x = 3 - echec
        can.move(a, vxa, vya)
        if score >= 100 :
            can.move(b, vxb, vyb)
            if score >= 200 :
                can.move(c, vxc, vyc)
                if score >= 300 :
                    can.move(d, vxd, vyd)
                    if score >= 500 :
                        can.move(boss, vxboss, vyboss)

    #Déplacement des balles :
        #Déplacement de la première balle
        if place_a[0]+25> 500 : 
                vxa = -5
        if place_a[1]+25> 400 :
                vya = -5
        if place_a[0]-5< 0 :
                vxa = 5
        if place_a[1]-5<0 : 
                vya = 5
        #Déplacement de la seconde balle  
        if place_b[0]+25> 500 : 
                vxb = -5
        if place_b[1]+25> 400 :
                vyb = -5
        if place_b[0]-5< 0 :
                vxb = 5
        if place_b[1]-5<0 : 
                vyb = 5
        #Déplacement de la troisième balle
        if place_c[0]+25> 500 : 
                vxc = -5
        if place_c[1]+25> 400 :
                vyc = -5
        if place_c[0]-5< 0 :
                vxc = 5
        if place_c[1]-5<0 : 
                vyc = 5
        #Déplacement de la dernière balle    
        if place_d[0]+25> 500 : 
                vxd = -5
        if place_d[1]+25> 400 :
                vyd = -5
        if place_d[0]-5< 0 :
                vxd = 5
        if place_d[1]-5<0 : 
                vyd = 5
        #Déplacement de la balle rouge
        if place_f[0]+45> 500 : 
                vxboss = -2
        if place_f[1]+45> 400 :
                vyboss = -2
        if place_f[0]-5< 0 :
                vxboss = 2
        if place_f[1]-5<0 : 
                vyboss = 2
    #Collision
        if j[1] < place_a[1] and place_a[1] < j[3] or j[1] < place_a[3] and place_a[3] < j[3] :
            if j[0] < place_a[0] and place_a[0] < j[2] or j[0] < place_a[2] and place_a[2] < j[2] :
                if f > 1 :
                    v.delete(vie[x])
                    echec += 1
                    f = 0
        if j[1] < place_b[1] and place_b[1] < j[3] or j[1] < place_b[3] and place_b[3] < j[3] :
            if j[0] < place_b[0] and place_b[0] < j[2] or j[0] < place_b[2] and place_b[2] < j[2] :
                if f > 1 :
                    v.delete(vie[x])
                    echec += 1
                    f = 0
        if j[1] < place_c[1] and place_c[1] < j[3] or j[1] < place_c[3] and place_c[3] < j[3] :
            if j[0] < place_c[0] and place_c[0] < j[2] or j[0] < place_c[2] and place_c[2] < j[2] :
                if f > 1 :
                    v.delete(vie[x])
                    echec += 1
                    f = 0
        if j[1] < place_d[1] and place_d[1] < j[3] or j[1] < place_d[3] and place_d[3] < j[3] :
            if j[0] < place_d[0] and place_d[0] < j[2] or j[0] < place_d[2] and place_d[2] < j[2] :
                if f > 1 :
                    v.delete(vie[x])
                    echec += 1
                    f = 0
        if place_f[1] < j[1] and j[1] < place_f[3] or place_f[1] < j[3] and j[3] < place_f[3] :
            if place_f[0] < j[0] and j[0] < place_f[2] or place_f[0] < j[2] and j[2] < place_f[2] :
                if f > 1 :
                    v.delete(vie[x])
                    echec += 1
                    if echec < 4 :
                        v.delete(vie[x-1])
                        echec += 1
                    f = 0
        score += 1
        f += 0.1
        if echec == 4 :
            jeu = False
            bouton.config(state = DISABLED, text = 'Perdu !', disabledforeground='red')
            print ("Votre score est :", score)
            can.delete(joueur)
            joueur = can.create_rectangle(j[0], j[1], j[2], j[3], fill = 'black')
        can.after(10, mouvement)
            

#*******************************************

fenetre = Tk()
fenetre.title("Evitez les balles !")
fenetre.geometry('500x500+250+100')
can = Canvas(fenetre, width = 500, height = 400, bg='black')
v = Canvas(fenetre, width = 200, height = 25, bg='red')
can.pack(side = TOP)
v.pack(side = TOP)
fenetre.bind("<KeyPress>", déplacement)

joueur = can.create_rectangle(240, 190, 260, 210, fill='green')
d = can.create_oval(5, 375, 25, 395, fill='orange')
c = can.create_oval(30, 375, 50, 395, fill='orange')
b = can.create_oval(55, 375, 75, 395, fill='orange')
a = can.create_oval(80, 375, 100, 395, fill='orange')
boss = can.create_oval(0, 510, 40, 550, fill ='red')

jeu = True
score = 0
echec = 0
f = 2
bouton = Button(fenetre, text='Commencer', command = mouvement)
bouton.pack(side = BOTTOM, pady = 10)
vxa = 5
vya = -5
vxb = 5
vyb = -5
vxc = 5
vyc = -5
vxd = 5
vyd = -5
vxboss = 2
vyboss = -2
vie = []
x = 0
while x < 4 :
    y = 50*x
    vie.append (v.create_rectangle(y+2, 0, 52+y, 30, fill='green'))
    x += 1

fenetre.mainloop
