import operator
from types import SimpleNamespace

import functions

def entry(f, b, f_branch = lambda x: True, b_branch = lambda x: True):
	return SimpleNamespace(**{
		"forward": f,
		"backward": b,
		"forward_branch": f_branch,
		"backward_branch": b_branch})

def literal_number(n, words):
	def push_num(state):
		functions.push_stack(state, n)
	
	def push_num_negative(state):
		functions.push_stack(state, -n)
	
	return entry(
		SimpleNamespace(**{
			"words": words,
			"func": push_num}),
		SimpleNamespace(**{
			"words": [],
			"func": push_num_negative})
	)

def self_opposite(f):
	return entry(f, f)

def branch(f, b):
	return entry(f, b, lambda s: s.stack[-1] != 0, lambda s: s.stack[-1] == 0)

class Words:
	entries = [
		entry(
			SimpleNamespace(**{
				"words": ["START", "STARTED", "STARTING", "STARTS",
					"BEGAN", "BEGIN", "BEGINS", "BEGINNING", "BEGUN",
					"COMMENCE", "COMMENCED", "COMMENCEMENT", "COMMENCEMENTS", "COMMENCES", "COMMENCING",
					"INCEPTION", "INCEPTIONS",
					"INITIATE", "INITIATED", "INITIATES", "INITIATING", "INITIATION", "INITIATIONS",
					"INAUGURATION", "INAUGURATIONS",
					"PROLOGUE", "PROLOGUES"],
				"func": functions.no_operation}),
			SimpleNamespace(**{
				"words": ["END", "ENDED", "ENDING", "ENDS",
					"FINISH", "FINISHED", "FINISHES", "FINISHING",
					"DENOUEMENT", "DENOUEMENTS",
					"RESOLUTION", "RESOLUTIONS",
					"EPILOGUE", "EPILOGUES",
					"FINAL", "FINALE", "FINALIZE", "FINALIZED", "FINALIZES", "FINALIZING"],
				"func": functions.terminate})
		),
		literal_number(0, ["ZERO", "ZEROES", "ZEROS", "ZILCH", "ZIP", "NONE", "AUGHT", "AUGHTS"]),
		literal_number(1, ["ONE", "ONES", "SINGLE", "SINGLES", "SINGLETON", "SINGLETONS", "SINGULAR", "ACE", "ACES", "UNIT", "UNITS", "UNO", "PENNY", "PENNIES", "SOLO"]),
		literal_number(2, ["TWO", "TWOS", "PAIR", "PAIRS", "DOUBLE", "DOUBLES", "DUO", "DUOS", "DUET", "DUETS", "COUPLE", "COUPLES", "DYAD", "DYADS"]),
		literal_number(3, ["THREE", "THREES", "TRIPLE", "TRIPLES", "TRIPLET", "TRIO", "TRIAD", "TRIADS"]),
		literal_number(4, ["FOUR", "FOURS", "QUADRUPLE", "QUADRUPLES", "QUADRUPLET", "QUADRUPLETS", "QUARTET", "QUARTETS"]),
		literal_number(5, ["FIVE", "FIVES", "QUINTUPLE", "QUINTUPLES", "QUINTUPLET", "QUINTUPLETS", "NICKEL", "NICKELS"]),
		literal_number(6, ["SIX", "SIXES", "SEXTET", "SEXTETS"]),
		literal_number(7, ["SEVEN", "SEVENS", "SEPTET", "SEPTETS",]),
		literal_number(8, ["EIGHT", "EIGHTS", "OCTET", "OCTETS"]),
		literal_number(9, ["NINE", "NINES"]),
		literal_number(10, ["TEN", "TENS", "DECADE", "DECADES", "DIME", "DIMES"]),
		literal_number(11, ["ELEVEN", "ELEVENS", "JACK", "JACKS"]),
		literal_number(12, ["TWELVE", "TWELVES", "DOZEN", "DOZENS", "QUEEN", "QUEENS"]),
		literal_number(13, ["THIRTEEN", "THIRTEENS", "KING", "KINGS"]),
		literal_number(14, ["FOURTEEN", "FOURTEENS", "FORTNIGHT", "FORTNIGHTS"]),
		literal_number(15, ["FIFTEEN", "FIFTEENS"]),
		literal_number(16, ["SIXTEEN", "SIXTEENS"]),
		literal_number(17, ["SEVENTEEN", "SEVENTEENS"]),
		literal_number(18, ["EIGHTEEN", "EIGHTEENS"]),
		literal_number(19, ["NINETEEN", "NINETEENS"]),
		literal_number(20, ["TWENTY", "TWENTIES", "SCORE", "SCORES"]),
		literal_number(21, ["BLACKJACK", "BLACKJACKS"]),
		literal_number(25, ["QUARTER", "QUARTERS"]),
		literal_number(30, ["THIRTY", "THIRTIES"]),
		literal_number(40, ["FORTY", "FORTIES"]),
		literal_number(50, ["FIFTY", "FIFTIES"]),
		literal_number(60, ["SIXTY", "SIXTIES"]),
		literal_number(70, ["SEVENTY", "SEVENTIES"]),
		literal_number(80, ["EIGHTY", "EIGHTIES"]),
		literal_number(90, ["NINETY", "NINETIES"]),
		literal_number(100, ["HUNDRED", "HUNDREDS", "CENTURIES", "CENTURY"]),
		literal_number(144, ["GROSS", "GROSSES"]),
		literal_number(1000, ["THOUSAND", "THOUSANDS", "MILLENIA", "MILLENIUM", "MILLENIUMS"]),
		literal_number(1024, ["KILOBYTE", "KILOBYTES"]),
		literal_number(10000, ["MYRIAD"]),
		literal_number(1000000, ["MILLION", "MILLIONS"]),
		literal_number(1048576, ["MEGABYTE", "MEGABYTES"]),
		literal_number(1000000000, ["BILLION", "BILLIONS"]),
		entry(
			SimpleNamespace(**{
				"words": ["ASCII",
					"TEXT", "TEXTS", "TEXTUAL", "TEXTUALLY",
					"STRING", "STRINGS",
					"CHARACTER", "CHARACTERS",
					"SYMBOL", "SYMBOLIC", "SYMBOLS",
					"MONOGRAM", "MONOGRAMMED", "MONOGRAMMING", "MONOGRAMS",
					"HIEROGLYPH", "HIEROGLYPHIC", "HIEROGLYPHICS", "HIEROGLYPHS"],
				"func": functions.ascii_mode}),
			SimpleNamespace(**{
				"words": ["NUMBER", "NUMBERS", "NUMERICAL", "NUMERICALLY",
					"INTEGER", "INTEGERS"],
				"func": functions.number_mode})
		),
		entry(
			SimpleNamespace(**{
				"words": ["PRINT", "PRINTED", "PRINTING", "PRINTS",
					"OUTPUT", "OUTPUTS", "OUTPUTTED", "OUTPUTTING",
					"WRITE", "WRITES", "WRITING", "WROTE",
					"DISPLAY", "DISPLAYED", "DISPLAYING", "DISPLAYS"],
				"func": functions.user_output}),
			SimpleNamespace(**{
				"words": ["SCAN", "SCANNED", "SCANNING", "SCANS",
					"INPUT", "INPUTS", "INPUTTED", "INPUTTING",
					"READ", "READING", "READS",
					"PARSE", "PARSED", "PARSES", "PARSING"],
				"func": functions.user_input})
		),
		entry(
			SimpleNamespace(**{
				"words": ["ADD", "ADDED", "ADDING", "ADDITION", "ADDITIVE", "ADDS",
					"SUM", "SUMMATION", "SUMMATIONS", "SUMMED", "SUMMING", "SUMS",
					"PLUS",
					"COMBINE", "COMBINED", "COMBINES", "COMBINING",
					"TOTAL", "TOTALED", "TOTALING", "TOTALS",
					"TALLIED", "TALLIES", "TALLY", "TALLYING"],
				"func": functions.binary_op(operator.add)}),
			SimpleNamespace(**{
				"words": ["SUBTRACT", "SUBTRACTED", "SUBTRACTING", "SUBTRACTION", "SUBTRACTS",
					"DIFFER", "DIFFERED", "DIFFERENCE", "DIFFERING", "DIFFERS",
					"MINUS",
					"WITHOUT",
					"DEDUCT", "DEDUCTED", "DEDUCTING", "DEDUCTION", "DEDUCTIONS", "DEDUCTS"],
				"func": functions.binary_op(operator.sub)})
		),
		entry(
			SimpleNamespace(**{
				"words": ["MULTIPLIED", "MULTIPLIES", "MULTIPLY", "MULTIPLYING",
					"TIMES",
					"OF",
					"PRODUCT", "PRODUCTS"],
				"func": functions.binary_op(operator.mul)}),
			SimpleNamespace(**{
				"words": ["DIVIDE", "DIVIDED", "DIVIDES", "DIVIDING", "DIVISION", "DIVISIONS",
					"QUOTIENT", "QUOTIENTS",
					"MODULAR", "MODULO",
					"BY",
					"REMAINDER", "REMAINDERS"],
				"func": functions.safe_div})
		),
		self_opposite(
			SimpleNamespace(**{
				"words": ["NOTHING", "NOTHINGNESS",
					"VOID", "VOIDED", "VOIDING", "VOIDS",
					"NIL", "NILS", "NULL", "NULLS",
					"EMPTINESS", "EMPTY",
					"AWAIT", "AWAITED", "AWAITING", "AWAITS", "WAIT", "WAITED", "WAITING", "WAITS",
					"STANDBY",
					"REST", "RESTED", "RESTING", "RESTS",
					"HANG", "HANGING", "HANGS", "HUNG",
					"STALL", "STALLED", "STALLING", "STALLS"],
				"func": functions.no_operation})
		),
		entry(
			SimpleNamespace(**{
				"words": ["DUPLICATE", "DUPLICATED", "DUPLICATES", "DUPLICATING",
					"DUPE", "DUPED", "DUPES", "DUPING",
					"DITTO",
					"AGAIN",
					"CLONE", "CLONED", "CLONES", "CLONING",
					"COPIED", "COPIES", "COPY", "COPYING",
					"MIRROR", "MIRRORED", "MIRRORING", "MIRRORS",
					"REPLICATE", "REPLICATED", "REPLICATES", "REPLICATING",
					"REPRODUCE", "REPRODUCED", "REPRODUCES", "REPRODUCING"],
				"func": functions.duplicate}),
			SimpleNamespace(**{
				"words": ["POP", "POPPED", "POPPING", "POPS",
					"REMOVE", "REMOVED", "REMOVES", "REMOVING",
					"DELETE", "DELETED", "DELETES", "DELETING",
					"DISCARD", "DISCARDED", "DISCARDING", "DISCARDS",
					"DESTROY", "DESTROYED", "DESTROYING", "DISTROYS",
					"ELIMINATE", "ELIMINATED", "ELIMINATES", "ELIMINATING",
					"CUT", "CUTS", "CUTTING",
					"OMIT", "OMITS", "OMITTED", "OMITTING"],
				"func": functions.pop_stack})
		),
		self_opposite(
			SimpleNamespace(**{
				"words": ["SWAP", "SWAPPED", "SWAPPING", "SWAPS",
					"FLIP", "FLIPPED", "FLIPPING", "FLIPS",
					"SWITCH", "SWITCHED", "SWITCHES", "SWITCHING",
					"EXCHANGE", "EXCHANGED", "EXCHANGES", "EXCHANGING",
					"FLOP", "FLOPPED", "FLOPPING", "FLOPS"],
				"func": functions.swap})
		),
		entry(
			SimpleNamespace(**{
				"words": ["STORE", "STORED", "STORES", "STORING",
					"PUT", "PUTS", "PUTTING",
					"HOARD", "HOARDED", "HOARDING", "HOARDS",
					"KEEP", "KEEPING", "KEEPS", "KEPT",
					"STASH", "STASHED", "STASHES", "STASHING",
					"DEPOSIT", "DEPOSITED", "DEPOSITING", "DEPOSITS"],
				"func": functions.push_storage}),
			SimpleNamespace(**{
				"words": ["RETRIEVAL", "RETRIEVALS", "RETRIEVE", "RETRIEVED", "RETRIEVES", "RETRIEVING",
					"GET", "GETS", "GETTING", "GOT",
					"WITHDRAW", "WITHDRAWAL", "WITHDRAWALS", "WITHDRAWING", "WITHDRAWS", "WITHDREW",
					"RECALL", "RECALLED", "RECALLING", "RECALLS",
					"RECLAIM", "RECLAIMED", "RECLAIMING", "RECLAIMS",
					"FETCH", "FETCHED", "FETCHES", "FETCHING"],
				"func": functions.pop_storage})
		),
		branch(
			SimpleNamespace(**{
				"words": ["BRANCH", "BRANCHED", "BRANCHES", "BRANCHING",
					"IF",
					"CONDITION", "CONDITIONAL", "CONDITIONALLY", "CONDITIONALS", "CONDITIONS",
					"CASE", "CASES",
					"WHEN", "WHENEVER",
					"ASSUMING",
					"PROVIDED",
					"NECESSARILY",
					"CONTINGENCIES", "CONTINGENCY", "CONTINGENT"],
				"func": functions.no_operation}),
			SimpleNamespace(**{
				"words": [],
				"func": functions.no_operation})
		),
	]
	
	starting_word = "START"