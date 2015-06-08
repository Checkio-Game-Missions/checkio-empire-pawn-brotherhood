Chess is a two-player strategy game played on a square checkered game board laid out in eight rows called ranks 
which are denoted with numbers 1 to 8, and eight columns called files and denoted with letters a to h.
Each square of the chessboard is identified by a unique coordinate pair
— a letter and a number (ex, "a1", "h8", "d6").
To train the snipers, we only need to concern ourselves with pawns for now.
A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file,
by moving to that square. For white pawns the front squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

```
S - Safe pawn
U - Unsafe pawn

   |---|---|---|---|---|---|---|---|
8  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
7  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
6  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
5  |   |   |   |   |   |   | S |   |
   |---|---|---|---|---|---|---|---|
4  |   | S |   | S |   | S |   |   |
   |---|---|---|---|---|---|---|---|
3  |   |   | S |   | S |   |   |   |
   |---|---|---|---|---|---|---|---|
2  |   |   |   | U |   |   |   |   |
   |---|---|---|---|---|---|---|---|
1  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
     a   b   c   d   e   f   g   h


   |---|---|---|---|---|---|---|---|
8  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
7  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
6  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
5  |   |   |   |   | S |   |   |   |
   |---|---|---|---|---|---|---|---|
4  |   | U | U | U | U | U | U |   |
   |---|---|---|---|---|---|---|---|
3  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
2  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
1  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
     a   b   c   d   e   f   g   h
```
