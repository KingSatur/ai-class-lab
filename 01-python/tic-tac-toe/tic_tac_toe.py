import re
import random


_PLAYER = "player"
_MACHINE = "machine"
_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    filas = []
    for i,cell in enumerate(self.board):
      filas.append(self.board[i])

    columnas = []
    columnas.append(self.board[0])
    columnas.append(self.board[3])
    columnas.append(self.board[6])
    columnas.append(self.board[1])
    columnas.append(self.board[4])
    columnas.append(self.board[7])
    columnas.append(self.board[2])
    columnas.append(self.board[5])
    columnas.append(self.board[8])

    diagonales = []
    diagonales.append(self.board[0])
    diagonales.append(self.board[4])
    diagonales.append(self.board[8])
    diagonales.append(self.board[2])
    diagonales.append(self.board[4])
    diagonales.append(self.board[6])

  
    if self.turn == _PLAYER:
      trickyJugador = self.verficarTricky(filas,columnas, diagonales, _PLAYER_SYMBOL)
      if trickyJugador:
        print("Ganaste")
        self.winner = _PLAYER
        self.is_game_over = True
        return self.is_game_over
      elif not trickyJugador:
        trickyMachine = self.verficarTricky(filas, columnas,diagonales, _MACHINE_SYMBOL)
        if trickyMachine:
          self.winner = _MACHINE
          print("Gano la maquina")
          self.is_game_over = True
          return self.is_game_over
      elif self.winner and self.board.count(None) == 9:
        print("Empate")
    elif self.turn == _MACHINE:
      trickyMachine = self.verficarTricky(filas,columnas,diagonales, _MACHINE_SYMBOL)
      if trickyMachine:
        print("Gano la maquina")
        self.winner = _MACHINE
        self.is_game_over = True
        return self.is_game_over
      elif not trickyMachine:
        trickyJugador = self.verficarTricky(filas, columnas,diagonales, _PLAYER_SYMBOL)
        if trickyJugador:
          self.winner = _PLAYER
          self.is_game_over = True
          print("Ganaste")
          return self.is_game_over
      elif self.winner and self.board.count(None) == 9:
        print("Empate")
        return self.is_game_over

  def verficarTricky(self, filas, columnas, diagonales, simbolo):
      verticalTricky = False
      horizontalTricky = False
      diagonalTricky = False
      iterableV = 0
      while iterableV <= 6:
        test = columnas[iterableV:iterableV+3]
        verticalTricky = test.count(simbolo) == 3
        # print(test, "Columnas")
        if verticalTricky:
          break
        iterableV += 3

      if(not verticalTricky):
        # print("LLegue aqui")
        iterableH = 0
        while iterableH <= 6:
          test = filas[iterableH:iterableH+3]
          horizontalTricky = test.count(simbolo) == 3
          # print(test, "Filas")
          if horizontalTricky:
            break
          iterableH += 3
        if horizontalTricky:
          return horizontalTricky
        else:
          iterableD = 0
          while iterableD <= 3:
            test = diagonales[iterableD:iterableD+3]
            diagonalTricky = test.count(simbolo) == 3
            # print(test, "Filas")
            if diagonalTricky:
              break
            iterableD += 3
          if diagonalTricky:
            return diagonalTricky
                  
      return verticalTricky

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
      self.is_over()
    else:
      self.machine_turn()
      self.turn = _PLAYER
      self.is_over()

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()
    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    randomCell = random.randint(0,8)
    while(self.board[randomCell]):
       randomCell = random.randint(0,8)
    self.board[randomCell] = _MACHINE_SYMBOL


    # for i, cell in enumerate(self.board):
    #   if cell is None:
    #     self.board[i] = _MACHINE_SYMBOL
    #     break

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    emptyWord = 'Empty Cell'
    board = ''
    for i,cell in enumerate(self.board):
      board += f'[{str(self.board[i] + (len(emptyWord) - len(self.board[i])) * " " if self.board[i] else emptyWord)}]     '  
      if (i + 1) % 3 == 0:
        board += '\n\n'
    return board

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner

    pass

