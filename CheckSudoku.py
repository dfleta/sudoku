# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, checkSudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.


class Sudoku():

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def checkSudoku(self):

        # Precondicion
        assert isinstance(
            self.sudoku, list), "la interfaz exige que sudoku debe ser una lista"

        sudokuSano = self.checkCuadrado(self.sudoku) and \
            self.checkNumerosEnRango(self.sudoku) and \
            self.checkFilas(self.sudoku) and \
            self.checkColumnas(self.sudoku)

        # Postcondicion
        assert isinstance(self.sudokuSano, bool)

        return sudokuSano

    def checkCuadrado(self):

        # Precondicion
        assert isinstance(
            self.sudoku, list), "la interfaz exige que sudoku debe ser una lista"

        sudokuSano = True
        numeroFilas = len(self.sudoku)

        for fila in self.sudoku:

            if len(fila) != numeroFilas:
                sudokuSano = False
                break

        # Postcondicion
        assert isinstance(
            sudokuSano, bool), "la interfaz exige devolver un valor lógico"

        return sudokuSano

    def checkNumerosEnRango():
        # Precondicion
        assert isinstance(
            sudoku, list), "la interfaz exige que sudoku debe ser una lista"

        numerosValidos = range(1, len(sudoku) + 1)
        for fila in sudoku:
          for numero in fila:
            if not isinstance(numero, int) or numero not in numerosValidos:
              return False

        return True

    def checkFilas():
        return True

    def checkColumnas():
        return True


### CASOS TEST ###

if __name__ == '__main__':

    import casosTestSudoku
    '''
     # casos test checkSudoku()

     for attr in sorted(casosTestSudoku.__dict__):
     # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
     # Asi podemos añadir todos los casos que queramos en la unidad cassTestSudoku
     # sin modificar este codigo
       if attr.startswith('__'):
         pass
         # Skip atributo
       else:
         sudoku = Sudoku(casosTestSudoku.__dict__[attr]))
         print(attr, " => ", sudoku.checkSudoku() )
         # mismo codigo que getattr(module, attr)
         # es necesario añadir el espacio de nombres del modulo:
         # casosTestSudoku.irregular
    '''
    ### CASOS TEST checkCuadrado() ###

    objetoSudokuTest = Sudoku([])

    for attr in sorted(objetoSudokuTest.__dict__):
         if attr.startswith('__'):
             pass
             # Skip atributo
         else:
             print("### CASOS TEST ### %s" % ( objetoSudokuTest.__dict__[__name__] ) )
             for casoTest in sorted(casosTestSudoku.__dict__):
                      # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
                      # Asi podemos añadir todos los casos que queramos en la unidad cassTestSudoku
                      # sin modificar este codigo
                      if casoTest.startswith('__'):
                          pass
                          # Skip atributo
                      else:
                          sudoku = Sudoku(casosTestSudoku.__dict__[casoTest])
                          print(attr, " => ", sudoku.checkCuadrado())
                          # mismo codigo que getattr(module, attr)
                          # es necesario añadir el espacio de nombres del modulo:
                          # casosTestSudoku.irregular
