print("".join([":" + "".join(["^<" if b == "1" else "<" for b in bin(ord(l))[2:].zfill(8)[::-1]]) + '!' for l in input()]))
"""
make it make sense
print(
    "".join(
        [":" + "".join(
            ["^<" if b == "1" else 
             "<" for b in 
             bin(ord(l))[2:].zfill(8)[::-1]
             ]
            ) + 
            '!' for l in input()
            ]
        )
    )

"""