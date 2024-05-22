# TicTacToe

Kindergarten implementation of tictactoe in Python with 

## State Representation 
state is 9 zeros + 1 zero which tells whose turn it is

because `0` looks like `o` or `O` i'll represent O's as -1 and X's as 1, 0 means empty square

### Moves
should taken move be `a1` in context of board that is `c` characters on 3 characters long?

or 

as an input in range of `0-8`

```
    1   2   3

a  a1, a2, a3

b  b1, b2, b3

c  c1, c2, c3
```

by enumerating this we get:

```
[(0, 'a1'), (1, 'a2'), (2, 'a3'), (3, 'b1'), (4, 'b2'), (5, 'b3'), (6, 'c1'), (7, 'c2'), (8, 'c3')]
```

## Testing

if testing run `python3 -m pytest -v` from home directory, otherwise won't work.

## TODO

* ~~check for wins in rows~~
* ~~check for wins in diagonals~~
* ~~heck for draws~~
* ~~wiret test for both of those things~~
* fix this state:
   turn: -1
  [[-1  1 -1]
   [-1  1  0]
   [ 1  1 -1]]
  (False, 1)

