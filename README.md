Deux méthodes peuvent être utilisées: .print_tree() et .print_tree_facultatif(). Toutes deux prennent 
en objet l'arbre crée avec la classe BinaryTree. 

print_tree permet de créer un affichage unilatéral de l'arbre. C'est à dire qu'un neoud "enfant" sera 
placé à la ligne avec une incrémentation définie et fixe du noeud "parent", sans prendre 
en compte sa réelle position par rapport à celui-ci (droite ou gauche). 

print_tree_facultatif() permet de créer un affichage bilatéral de l'arbre. C'est à dire que l'incrémentation 
du noeuf enfant par rapport au noeud parent dépend de sa position (gauche/droite) par rapport à celui-ci. De 
plus les noeufs frères seront sur la même ligne.  
