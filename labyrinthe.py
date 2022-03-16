from ast import Index
from ctypes import sizeof
from dataclasses import dataclass
import operator
import sys


class Maze(object):
    """Représente un labyrinthe à deux dimensions, où chaque cellule peut contenir un seul caractere."""

    def __init__(self):
        self.data = []

    def read_file(self, path):
        """Lire un fichier texte de type labyrinthe et séparer chaque caractère. Retournez
           une liste à 2 dimensions où la première dimension est constituée de lignes et
           la seconde est constituée de colonnes."""
        maze = []
        with open(path) as f:
            for line in f.read().splitlines():
                maze.append(list(line))
        self.data = maze

    def write_file(self, path):
    
        with open(path, 'w') as f:
            for r, line in enumerate(self.data):
                f.write('%s\n' % ''.join(line))

    def find(self, symbol):
        """Trouve la première instance du symbole spécifié dans le
           labyrinthe, et renvoie l'indice de ligne et l'indice de colonne de la cellule correspondante.
           cellule correspondante. 
           Retourne None si aucune cellule n'est trouvée."""
        for r, line in enumerate(self.data):
            try:
                return r, line.index('1')
            except ValueError:
                pass

    def get(self, where):
        """Retourne le symbole stocké dans la célule spécifiée."""
        r, c = where
        return self.data[r][c]

    def set(self, where, symbol):
        """Store le symbole dans la célule spécifiée."""
        r, c = where
        self.data[r][c] = symbol



    def __str__(self):
        return '\n'.join(''.join(r) for r in self.data)


def solve(maze, where=None, direction=None):
    """Trouve un chemin à travers le labyrinthe spécifié en commençant par where (ou une cellule marquée 'S' si where n'est pas fourni).
       une cellule marquée 'S' si where n'est pas fourni), et une cellule marquée
       '2'. À chaque cellule, les quatre directions sont essayées dans l'ordre suivant
       DROITE, BAS, GAUCHE, HAUT. Lorsqu'une cellule est quittée, un symbole de marqueur
       (un des symboles '>', 'v', '<', '^') est écrit pour indiquer la nouvelle direction.
       direction, et si un retour en arrière est nécessaire, un symbole ('.') est également écrit.
       également écrit. La valeur de retour est None si aucune solution n'a été
       solution n'a été trouvée, et un tuple (row_index, column_index) quand une solution
       est trouvée."""
    start_symbol = '1'
    end_symbol = '2'
    vacant_symbol = ' '
    backtrack_symbol = '.'
    directions = (0, 1), (1, 0), (0, -1), (-1, 0)
    direction_marks = '>', 'v', '<', '^'

    where = where or maze.find(start_symbol)
    if not where:
      
        return
    if maze.get(where) == end_symbol:
      
        return where
    if maze.get(where) not in (vacant_symbol, start_symbol):
      
        return

    for direction in directions:
        try:
        
            next_cell = list(map(operator.add, where, direction))
           
            marker = direction_marks[directions.index(direction)]
            if maze.get(where) != start_symbol:
                maze.set(where, marker)
            sub_solve = solve(maze, next_cell, direction)
            if sub_solve:
               
                return sub_solve
           
            maze.set(where, backtrack_symbol)
        except:
            print(" ")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ('Arguments: <input file> <output file>')
        sys.exit(1)
    input_file, output_file = sys.argv[1:3]

    maze = Maze()
    maze.read_file(input_file)

    solution = solve(maze)
    if solution:
        print ('Fin du labyrinthe trouvée aux coordonées suivantes  %s' % solution)
        
    else:
        print ('Pas de solutions (Pas d entree, de sortie ou erreur')
    print (maze)
    maze.write_file(output_file)