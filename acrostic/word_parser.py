from types import SimpleNamespace

def move_in_dir(across, n, pos):
	return tuple(a + b for a, b in zip(pos, (n, 0) if across else (0, n)))

def letters_in_dir(grid, across, forward, pos):
	grid_pos = pos
	
	letters = ""
	while grid.is_in_bounds(grid_pos) and grid.grid[grid_pos]:
		c = grid.grid[grid_pos]
		letters = letters + c if forward else c + letters
		
		grid_pos = move_in_dir(across, 1 if forward else -1, grid_pos)
	
	return letters

def word_starting_at(grid, across, pos):
	forward = letters_in_dir(grid, across, True, pos)
	backward = letters_in_dir(grid, across, False, pos)
	
	if len(backward) == 1 and len(forward) != 1:
		return SimpleNamespace(**{
			"start_pos": pos,
			"end_pos": move_in_dir(across, len(forward)-1, pos),
			"text": forward})
	elif len(backward) != 1 and len(forward) == 1:
		return SimpleNamespace(**{
			"start_pos": move_in_dir(across, -(len(backward)-1), pos),
			"end_pos": pos,
			"text": backward})
	else:
		return None

def word_at(grid, across, pos):
	back_count = len(letters_in_dir(grid, across, False, pos))
	
	if back_count <= 0:
		return None
	else:
		return word_starting_at(grid, across, move_in_dir(across, -(back_count-1), pos))

def find_all_words(grid):
	positions = []
	
	for dir in [True, False]:
		for x in range(grid.w):
			for y in range(grid.h):
				word = word_starting_at(grid, dir, (x, y))
				if word is not None and word not in positions:
					positions.append(word)
	
	return positions

def find_word(grid, wordlist):
	return [word for word in find_all_words(grid) if word.text in wordlist]

def position_in_word(word, pos):
	return pos[0] - word.start_pos[0] + pos[1] - word.start_pos[1]

def direction_of(word):
	x0, _ = word.start_pos
	x1, _ = word.end_pos
	return x0 != x1