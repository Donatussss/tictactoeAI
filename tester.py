from tictactoe import *

# print(is_initial_state(initial_state()))

# print(player(initial_state()))

# print(actions(initial_state()))

starting = initial_state()
starting[0][0] = None
starting[0][1] = "X"
starting[0][2] = "O"
starting[1][0] = "X"
starting[1][1] = "X"
starting[1][2] = "O"
starting[2][0] = None
starting[2][1] = "O"
starting[2][2] = None
print(starting)
# print(result(starting, (0, 0)))

# print(winner(starting))
# print(terminal(starting))
# print(utility(starting))

# print(actions(starting))
print(player(starting))