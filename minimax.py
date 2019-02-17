from collections import namedtuple
import random


from numpy import argmax


"""负无穷"""
infinity = float('inf')
"""使用namedtuple存储游戏状态
GameState：名称为“棋盘状态”
to_move：轮到谁下子
utility：用来在算法递归计算时存储每一个棋盘状态的效用值：
board：棋盘黑白子下子位置
moves：还可以走子的空位置
"""
GameState = namedtuple('GameState', 'to_move, utility, board, moves')


# ______________________________________________________________________________
# Minimax Search


def minimax_decision(state, game):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states. [Figure 5.3]"""
    player = game.to_move(state)

    def max_value(state):
        # 如果是最终结果，返回当前效用值
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        # 在MAX当前状态的所有可能的移动
        for a in game.actions(state):
            # 每个移动产生一个结果状态，对应一个MIN值
            # 找出这些MIN值中最小的，作为MAX当前状态的MAX值
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        """求MIN的功效值
        当是最终节点时"""
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        # 在MIN当前状态的所有可能的移动
        for a in game.actions(state):
            # 每个移动产生一个结果状态，对应一个MAX值
            # 找出这些MAX值中最小的，作为MIN当前状态的MIN值
            v = min(v, max_value(game.result(state, a)))
        return v

    # Body of minimax_decision:
    # 比较当前状态所有行为a 的大小
    # 比较方法：通过min_value（state，a）函数的结果比较
    return argmax(game.actions(state),
                  key=lambda a: min_value(game.result(state, a)))


def query_player(game, state):
    """Make a move by querying standard input.
    手动输入"""
    print("current state:")
    game.display(state)
    print("available moves: {}".format(game.actions(state)))
    print("")
    move_string = input('Your move? ')
    try:
        move = eval(move_string)
    except NameError:
        move = move_string
    return move


def random_player(game, state):
    """A player that chooses a legal move at random.
    随机选择一个动作"""
    return random.choice(game.actions(state))


class Game:


    def actions(self, state):

        raise NotImplementedError

    def result(self, state, move):

        raise NotImplementedError

    def utility(self, state, player):

        raise NotImplementedError

    def terminal_test(self, state):

        return not self.actions(state)

    def to_move(self, state):

        return state.to_move

    def display(self, state):

        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):

        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                state = self.result(state, move)
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))




class TicTacToe(Game):


    def __init__(self, h=3, v=3, k=3):
        # 棋盘是h行v列k个子连在一起算赢
        self.h = h
        self.v = v
        self.k = k
        # 所有棋盘都可以走子
        moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        # 设置初始棋盘状态
        self.initial = GameState(to_move='X',
                                 utility=0,
                                 board={},
                                 moves=moves)

    def actions(self, state):
        """Legal moves are any square not yet taken."""
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                             utility=self.compute_utility(state.board, move, state.to_move),
                             board=state.board, moves=state.moves)  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise.
        只有在最终状态时调用：赢则1
        """
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares.
        len对象长度
        当为"""
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("Now board state:")
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        """Return true if there is a line through move on board for player."""
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k


g=Game()
t=TicTacToe(g)
t.play_game()