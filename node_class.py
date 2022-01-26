import math
#import numpy as np

#a binary tree
class Node:
	#initialisation de l'arbre binaire
	def __init__(self,key_,val_):
		self.left=None
		self.right=None
		self.key=key_
		self.val=val_ 

	#méthode pour la recherche d'un élement dans l'arbre, node est le noeud principale, elle renvoie true si l'element est dans l'arbre et false dans le cas contraire
	def search_element(self,node,e_key,e_val):
		return_value=False
		if e_key==node.key and e_val==node.val :
			return_value=True
			return return_value
		else:
			if e_key<node.key:
				if node.left!=None:
					return self.search_element(node.left,e_key,e_val)
			else:
				if node.right!=None:
					return self.search_element(node.right,e_key,e_val)

	#Insertion d'un élement dans l'arbre binaire
	def insert_element(self,node,e_key,e_val):
		#si on parcours tout l'arbre et que on est une feuille à un moment donnée on insere l'element au bon endroit
		if node.left==None and node.right==None :
			print('ok')
			if e_key<node.key:
				node.left=Node(e_key,e_val)
			else:
				node.right=Node(e_key,e_val)
		else:
			if e_key<node.key:
				if node.left!=None:
					return self.insert_element(node.left,e_key,e_val)
			else:
				if node.right!=None:
					return self.insert_element(node.right,e_key,e_val)

	#Suppression d'un element 

	#supression d'un élement et reangement