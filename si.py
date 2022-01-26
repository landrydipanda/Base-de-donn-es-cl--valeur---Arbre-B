import csv
from node_class import Node

#A l'initialisation on doit pourvoir choisir la version idoine
class gestion_personne :
    def __init__(self):
        self.nom_prenom=[]
        self.notes=[] 

        #note comme key and nom_prenoms comme valeurs
        self.notes_sd=[]
        self.noms_notes=[]

        #noms_prenoms comme clé et notes comme valeurs 
        self.noms_sd=[]
        self.notes_noms=[]

    def charger_fichier(self,chemin):
        with open(chemin, newline='') as csvfile:
            fichier = csv.reader(csvfile, delimiter=';')
            for row in fichier:
                self.nom_prenom.append(row[0])
                self.notes.append(float(row[1]))
 #méthode qui permet de savoir si un element est présent dans une liste
    def elmnt_list(self,liste,elnt):
        var=0
        indi=0
        i=0
        while(i<len(liste) and indi==0):
            if elnt==liste[i]:
                #pour dire qu'il est dans la liste 
                var=1
                #je passe à 1 pour quitter la boucle
                indi=1
            i=i+1
        return var

#v2 les  clés sont les noms_prenoms et les valeurs sont les differents notes qui lui sont associés
    def cmpare_chaine(self,ch1,ch2):
        v=1
        indi=0
        if len(ch1)==len(ch2):
            i=0
            while(i<len(ch1) and indi==0):
                if ch1[i]!=ch2[i]:
                    v=0
                    indi=1
                i=i+1
        else:
            v=0
        return v # v=1 egalité entre les deux chaines

    def element_in_list(self,liste,elmnt):
        pres=0
        i=0
        indi=0
        while(i<len(liste) and indi==0):
            if self.cmpare_chaine(elmnt,liste[i])==1:
                pres=1
                indi=1
            i=i+1
        return pres

    def charger_personne_v2(self):
        """
        self.noms_sd=[]
        self.notes_noms=[]
        """
        #Enregistrer tous les noms_prenoms sans doublons
        for nm in self.nom_prenom:
            #si l'element n'est pas dans la liste on le rajoute 
            if self.element_in_list(self.noms_sd,nm)==0:
                #print("ok")
                self.noms_sd.append(nm)
        print(self.noms_sd)
        """
        for i in range(len(self.noms_sd)):
            ls=[]
            for j in range(len(self.nom_prenom)):
                if cmpare_chaine(self.noms_sd[i],self.nom_prenom[j])==1:
                    #on incremmente les notes correspondant au nom_prenom
                    ls.append(self.notes[j])
            #on ajoutes les notes correspondant aux nom_prenom : 
            self.notes_noms.append(ls)
        """

#v3 les clés clés sont les notes et les valeurs sont les differents noms_prenoms qui lui sont associés
    def charger_personne_v3(self): 
        #Enregistrer tous les notes sans doublons
        for nt in self.notes:
            #si l'element n'est pas dans la liste on le rajoute 
            if self.elmnt_list(self.notes_sd,nt)==0:
                self.notes_sd.append(nt)
        #print(self.notes_sd)
        for i in range(len(self.notes_sd)):
            ls=[]
            for j in range(len(self.notes)):
                if self.notes_sd[i]==self.notes[j]:
                    #on ajoute le noms_prenoms correspondant aux notes
                    ls.append(self.nom_prenom[j])
            #on ajoutes les noms_prenoms correspondant à la note : 
            self.noms_notes.append(ls)
        #print(self.noms_notes)

    def ajoute_personne(self,nm_prnm,note):
        self.nom.append(nm_prnm)
        self.notes.append(note)
    #on retire les notes a l'aide de l'indice
    def note_moyenne_ma(self):
        i=-1
        nt=[]
        for elmnt in self.nom_prenom:
            i=i+1
            if elmnt=="Margaret Smith":
                indi_prn=i
                nt.append(self.notes[indi_prn])
        moy=sum(nt)/len(nt)
        return moy
    def recuperer_notes_sup_19(self):
        personne=[]
        i=-1
        for elmnt in self.nom_prenom:
            i=i+1
            if self.notes[i]>19:
                personne.append(elmnt)
        return personne
    def personne_notes_0(self):
        personne=[]
        i=-1
        for elmnt in self.nom_prenom:
            i=i+1
            if self.notes[i]==0:
                personne.append(elmnt)
        return personne
   
    #liste qui renvoie le nombre de personne ayant plusieurs notes
    def nb_personne_plusieurs_notes(self):
        liste=[]
        occ=0
        for nt in self.notes:
            #on verifie que l'element n'est pas dans la liste avant de l'ajouter, pour evitez d'avoir les doublons
            if self.elmnt_list(liste,nt)==0:
                liste.append(nt)
        #actuellement dans liste on a pas de doublons de notes, on va regarder le nombre d'occurence dans la vraie liste
        #de notes
        for i in liste:
            #on cherche le nombre d'occurennce de i
            nb=0
            for j in self.notes:
                if i==j:
                    nb=nb+1
            if nb>1:
                #incrementer le nombre
                occ=occ+1
        return occ
    def suprime_personne(nm_prnm):
        i=-1
        for elmnt in self.nom_prenom:
            i=i+1
            if elmnt==nm_prnm:
                indi_prn=i
                self.nom_prenom.remove(indi_prn)
                self.notes.remove(indi_prn)        
    def recherche_personne(self,nm_prnm):
        var_=0
        i=-1
        for elmnt in self.nom_prenom:
            i=i+1
            if elmnt==nm_prnm:
                var=1
                indi_prn=i
                print("la personne est dans la base de donnee !\n")
                print("noms et prenoms : "+str(self.nom_prenom[indi_prn])+"\n")
                print("notes : "+str(self.notes))
            else:
                print("Aucune personne ne contient de noms et prenoms renseigner")
  
                
        
        
                
    