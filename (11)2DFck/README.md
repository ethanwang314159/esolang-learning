2dfuck.py, remove_comments.py, and strto2dfuck.py are all stolen from https://gitlab.com/TheWastl/2DFuck
brainfuckto2dfuck.py, strtobrainfuckto2dfuck.py, and .2f files are all original

also taken from https://gitlab.com/TheWastl/2DFuck : 
brainfuck -> 2DFuck
BEGIN     -> !x
<         -> ^^r!xr
>         -> vvr!xr
.         -> v>r.>r.>r.>r.>r.>r.>r.>r.^r![<r!]!
,         -> v>rx,x>rx,x>rx,x>rx,x>rx,x>rx,x>rx,x>rx,x^r![<r!]!
+         -> v>>>>>>>>xr![<xr!]^r![<r!]vrx^r
-         -> vx>>>>>>>>xr[<xr]^r![<r!]vrx^r
[         -> vx>>>>>>>>r![<r!]^r![[<r!]!vx^
]         -> vx>>>>>>>>r![<r!]^r!]v!x^
