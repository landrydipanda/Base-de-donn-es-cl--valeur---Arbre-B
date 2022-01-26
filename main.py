#import numpy as np
#import matplotlib.pyplot

from si import gestion_personne as gestion
from node_class import Node
from B_Tree import B_tree

#on va faire un test :

my_tree_b=B_tree(["landry"],[[14,12,8]])

my_tree_b.left=B_tree(["cauchy"],[[18,20,19]])
my_tree_b.left.left=B_tree(["caucha"],[[15.21,13.2]])
my_tree_b.left.right=B_tree(["cauchi"],[[11.75,11.24]])

my_tree_b.right=B_tree(["tari","tza"],[[8,14,12,17],[8.5,2,7,3]])
my_tree_b.right.left=B_tree(["tara"],[[17.5,16.75]])
my_tree_b.right.middle=B_tree(["tiro"],[[12.4,13.7]])
my_tree_b.right.right=B_tree(["tzi"],[[14.25,10.60]])


print(my_tree_b.search_element(my_tree_b,"tza",7))

print(my_tree_b.search(my_tree_b, "tza"))
