# ESOTERIC LANGUAGE LEARNING

## TODAY
- [Bespoke](https://esolangs.org/wiki/Bespoke)

## NEXT UP
- [硕鼠](https://esolangs.org/wiki/%E7%A1%95%E9%BC%A0)
- [/gɹəʊguː/](https://esolangs.org/wiki//g%C9%B9%C9%99%CA%8Agu%CB%90/)
- [0 bytes XD](https://esolangs.org/wiki/0_bytes_XD) if im lazy and want to just write a bunch of interpreters in different languages
- [2DFuck](https://esolangs.org/wiki/2DFuck) also [here](https://gitlab.com/TheWastl/2DFuck) if i want to get fucked in 2 dimensions also like i was just wondering about this too the other day lol
- [Chef](https://esolangs.org/wiki/Chef)
- [acrostic](https://esolangs.org/wiki/Acrostic) looks [very interesting](https://github.com/Mercerenies/acrostic-lang)

## Do
- [List](https://esolangs.org/wiki/Esoteric_programming_language)
- [Truth machine list](https://esolangs.org/wiki/Truth-machine#-C++)  
- [Pygyat](https://github.com/shamith09/pygyat)  
- asdf and 123 (if i really really have no ideas or time)
- Malbolge brute forcer  

# Language a day
- 17/09/25 Whitespace
- 18/09/25 Brainf*ck
- 19/09/25 EXCON
- 20/09/25 Malbolge (I tried then gave up)
- 21/09/25 Godot (gdscript i guess??)
- 22/09/25 Befunge
- 23/09/25 Bespoke

- 24/09/25 硕鼠
- 25/09/25 0 bytes XD
- 26/09/25 acrostic
- 27/09/25 2DFuck
- 28/09/25 Chef

## General resources
[ASCII table](https://www.ascii-code.com/)
    
## Whitespace 
It's hard (to read)   
Learnt using [tutorial](https://hackage.haskell.org/package/whitespace-0.4/src/docs/tutorial.html) and [compiler](https://naokikp.github.io/wsi/whitespace.html).  
Ran in terminal using [pip install whitespace](https://pypi.org/project/whitespace/)  
```bash
pip install whitespace
```

## BrainF*ck 
Easy to understand using [this excellent tutorial](https://saketupadhyay.medium.com/how-to-code-in-brainf-ck-without-losing-your-mind-6a8fd67b36b4).  
Ran in terminal using [bf-cli](https://github.com/aapzu/bf-cli).  
More learning using [Basics of BF](https://gist.github.com/roachhd/dce54bec8ba55fb17d3a)  
Very comprehensive 13 lessons by [DPAmar](https://tech.io/users/1962352/DPAmar) on tech.io, lesson 1 [here](https://tech.io/playgrounds/50426/getting-started-with-brainfuck/welcome)  
[Very good gist](https://gist.github.com/roachhd/dce54bec8ba55fb17d3a)
I'm trying to:  
- code something where you input two numbers and a function (+/-/*///) and it will do that e.g. (3\*2) returning 6
- solve leetcode problems such as palindrome checking an input string, and prime number checking, and fibonacci and decimal inputs
- base conversion
- calculate pi and output infinite digits and e 
- a game like good game idk with random etc (for this i need to decimal input aka 001-225 and y and n and takex inputs and random number 1 to x decided by input)
- interpreter/compiler in bf
- fibonnaci, pascal triangle numbers
- quine, reverse quine, mutual quine, whatever [this](https://codegolf.stackexchange.com/questions/63669/three-mutual-quines?rq=1) is 
- ~~brainfk interpreter in python pls because inputs are bugged with bf-cli~~ done
- ~~add a ? random command for 0-255 random number generator~~ done

[macos](https://formulae.brew.sh/formula/brainfuck)
```bash
$ brew install brainfuck
$ brainfuck lol-optimised.bf
```

[windows](https://github.com/aapzu/bf-cli)
```bash
npx bf-cli lol-optimised.bf

npm i -g bf-cli
bf-cli lol-optimised.bf
```

## EXCON
It was hard to set up the interpreter because I've never done that before. Anyways my .bat setup only works on windows and it's kind of scuffed but you just go to the excon folder path and use .\excon [script] and since it can be any file extension, I used some funny extensions.  
It literally can only print ASCII characters and that's it. It can't even take inputs. Like idk what to do with it other than print everything.  

I used the ruby interpreter from the [esolang article](https://esolangs.org/wiki/EXCON#Interpreter) and used that article to learn.
I then wrote a simple python script which takes an input and converts it to EXCON and then used questionable programming practices to condense it to one line.  
Then I messed around with it and became a ruby programmer(for real).

If you want to run this yourself uh don't. It's not very satisfying anyways.

# Malbolge
I don't want to talk about it.

# Godot
Followed for ten episodes, coded for 6 hours in that day(though I did do a lot of BF).
[Download](https://godotengine.org/download/)

## Befunge
complicated and cool. problem is its confusing
Found on [esolangs.org](https://esolangs.org/wiki/Befunge)

Using befintp.js:
```bash
npm install befunge
node befintp.js hello.bf
```

## Bespoke
wow made in 2025
very cool I will probably do this more tomorrow and future
basically everything is based on word length and theres A LOT OF COMMANDS
i forgot if its turing complete [check yourself](https://github.com/WinslowJosiah/bespokelang)

```bash
pip install --upgrade bespokelang
bespoke truth.bspk
```