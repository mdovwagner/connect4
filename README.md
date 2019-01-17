# Connect 4 
## Plus AI

### How to Use

Download and in the `connnect4` directory, run `python main.py` 

Type in a column number (1-7) to play your move. You are `X`, the computer is `O`. 

This is an example board
```
	[X, , , , , , ,]
	[X, , , , , , ,]
	[X, , , , , , ,]
	[O, , ,O, , , ,]
	[X, , ,O, , , ,]
	[O,X, ,O, , , ,]
	[X,O, ,O, , , ,]
	 1 2 3 4 5 6 7
```
Type `d` to see the debug output. Like this...
```
      1
      [1, 0, 0, 5, 0, 0, 0]
      1
      [0, 0, -1, 3, 3, -1, 0]
      1
      [3, 3, 2, 6, 4, 4, 3]
      1
      [1, 1, 0, 4, 1, 1, 3]
    [5, 6, 3, 5, 3, 6, 4]
  [2, 2, 9995, 3, 2, 2, 3]
[9995, 9995, 4, 9993, 9993, 4, 9995]

	[ , , , , , , ,]
	[ , , , , , , ,]
	[ , , , , , , ,]
	[ , , , , , , ,]
	[ , , , , , , ,]
	[ , , ,O, , , ,]
	[ , ,O,X,X, , ,]
	 1 2 3 4 5 6 7
```
The bottom row shows the score of possible moves. The AI plays for `Mini` so they will pick the lowest value (in this case `4`), and place an `O` in this column (col `3`). The high values are present because if Mini goes in one of those columns, Maxi can 100% win in the next 2 turns (that's how far lookahead is)
