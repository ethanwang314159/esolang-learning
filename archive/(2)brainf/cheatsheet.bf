this is so old don't judge

Formatting:

original stack cursor position
post-function stack cursor position

SHIFT VALUE

X 0 1st
0 X 1st
, save an input to 1
[>+<-] shift to 2

COPY VALUE

X 0 0 1st
X X 0 1st
, save an input to 1
[>+>+<<-] 0 X X
>>[<<+>>-] X X 0

ADDITION

X Y 1st
X+Y 0 1st
,>,< save input to 1 and 2
>[<+>-]<

SUBTRACTION

X Y 1st
X-Y 0 1st
,>,< save input to 1 and 2
>[<->-]<

MULTIPLICATION

X   Y 0 0 1st
X*Y 0 0 0 1st
,>,< save input to 1 and 2
[->[->+>+<<]>>[-<<+>>]<<<] HOLY COMPLEXITY jk you just decrease go right copy value then repeat but its really confusing

BETTER MULTIPLICATION

X Y 0 0   1st
0 X 0 X*Y 1st
,>,<
[>[->+>+<<]>[-<+>]<<-] smart things check tests/multiplication.bf for more info credit https://tech(dot)io/playgrounds/50426/getting-started-with-brainfuck/multiplication

OPTIONAL CLEANSING

0   X 0 X*Y 1st
X*Y 0 0 0   1st

>[-]>>[-<<<+>>>]<<< credit https://tech(dot)io/playgrounds/50426/getting-started-with-brainfuck/multiplication


DIVISION

X Y 0 0 0 1st
0 Y 0 0 X/Y 1st 

,>,< save input to 1 and 2
[>[->+>+<<]>>[-<<+>>]<[-<<->>]>>+<<<<] uses a counter
NOTE INFINITE LOOP FOR SOME Y IF X IS NOT DIVISIBLE

CHR()

oh crap

