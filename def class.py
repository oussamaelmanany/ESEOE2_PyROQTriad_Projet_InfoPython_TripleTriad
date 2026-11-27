class carte:
    #Les cartes sont définies selon 6 critères: son nom (.nom), ses valeurs (.top,.left,...) et sa couleur (.color)
    def __init__(self,nom:str='unnamed',a=0,b=0,c=0,d=0,color:str='gris'):
        self.nom=nom
        self.top=a
        self.right=b
        self.bottom=c
        self.left=d
        if color=='bleu':
            self.color='bleu'
        elif color=='rouge':
            self.color='rouge'
        else:
            self.color='gris'
    def __str__(self):
        return (f"{self.nom}:{self.top},{self.right},{self.bottom},{self.left}:{self.color}")
    def Vfight(topcard,bottomcard):
        #retourne quelle carte est la plus forte dans un combat vertical, insérer la carte situé en haut en première
        if topcard.bottom>bottomcard.top:
            bottomcard.color=topcard.color
            return topcard
        if topcard.bottom<bottomcard.top:
            topcard.color=bottomcard.color
            return bottomcard
        return None
    def Hfight(leftcard,rightcard):
        #retourne quelle carte est la plus forte dans un combat horizontal, insérer la carte situé en gauche en première
        if leftcard.right>rightcard.left:
            rightcard.color=leftcard.color
            return leftcard
        if leftcard.right<rightcard.left:
            leftcard.color=rightcard.color
            return rightcard
        return None
    
a=carte('a',1,1,1,1,'bleu')
b=carte('b',1,3,1,1,'rouge')
print(a,b)
print(carte.Hfight(b,b))