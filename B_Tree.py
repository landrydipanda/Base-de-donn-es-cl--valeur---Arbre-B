
import math
#import numpy as np

#a B-tree
class B_tree:
	#initialisation de l'arbre binaire
    def __init__(self,node_,val_):
        self.left=None
        self.middle=None
        self.right=None
        self.node=node_ # liste de taille au plus égale à 2
        self.val=val_ # liste de talle au plus égale 2, on a une liste de valeur pour chaque clé. chaque sous liste est de taille infinie
          
    def search_element_in_node(self,b_,key_,value_):
        result=False
        i=-1
        ok_i=-1
        for elnt in b_.node: # i vaut soit 0 soit 1 car max key = 2
            i=i+1
            #on verifie si la clé est dans le noeud
            if key_==elnt:
                ok_i=i #ok_i vaut soit -1 : la clé est absente , soit 0 , soit 1 
        # on se rassure que la clé recherchée est dans la liste 
        if ok_i!=-1: 
            for ss in b_.val[ok_i]: #on se place à la bonne liste de valeurs pour le noeud consideré
                if ss==value_: #on verifie que la valeur est dans la clé
                    result=True 
        return result
        
	#méthode pour la recherche d'un élement dans l'arbre, node est le noeud principale, elle renvoie true si l'element est dans l'arbre et false dans le cas contraire
    def search_element(self,b_,e_key,e_val):
        if self.search_element_in_node(b_,e_key,e_val)==True:		
            return True
        else:
            #si la taille du noeud est 1 : cela est similaire à l'arbre binaire
            if len(b_.node)==1:
                if e_key<b_.node[0]:
                    if b_.left!=None:
                        return self.search_element(b_.left,e_key,e_val)
                else:
                    if b_.right!=None:
                        return self.search_element(b_.right,e_key,e_val)
            #si la taille du noeud est 2 : on a la vrai variante de l'arbre B 2-3
            else:
                if e_key<b_.node[0]:
                    #on parcous la branche gauche:
                    if b_.left!=None:
                        return self.search_element(b_.left,e_key,e_val)
                elif e_key>b_.node[0] and e_key<b_.node[1]:
                    #on parcours la branche du milieu :
                    if b_.middle!=None:
                        return self.search_element(b_.middle,e_key,e_val)
                else:
                    #on parcours la branche de droite dans le cas écheant  :
                    if b_.right!=None:
                        return self.search_element(b_.right,e_key,e_val)   
                                           
                        