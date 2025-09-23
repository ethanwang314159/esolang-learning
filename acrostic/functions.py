import operator, sys

from exceptions import *

def terminate(state):
	state.terminated = True

def push_stack(state, n):
	state.stack.append(n)

def pop_stack(state):
	try:
		return state.stack.pop()
	except IndexError:
		raise StackUnderflow from None

def push_storage(state):
	state.storage.append(pop_stack(state))

def pop_storage(state):
	try:
		push_stack(state, state.storage.pop())
	except IndexError:
		raise StackUnderflow from None

def no_operation(state):
	pass

def duplicate(state):
	a = pop_stack(state)
	push_stack(state, a)
	push_stack(state, a)

def user_input(state):
	if state.ascii:
		push_stack(state, ord(sys.stdin.read(1)))
	else:
		push_stack(state, int(sys.stdin.readline()))

def user_output(state):
	a = pop_stack(state)
	sys.stdout.write(chr(a) if state.ascii else str(a))
	sys.stdout.flush()

def ascii_mode(state):
	state.ascii = True

def number_mode(state):
	state.ascii = False

def unary_op(f):
	def unary_func(state):
		a = pop_stack(state)
		push_stack(state, f(a))
	
	return unary_func

def binary_op(f):
	def binary_func(state):
		b = pop_stack(state)
		a = pop_stack(state)
		push_stack(state, f(a, b))
	
	return binary_func

def safe_div(state):
	b = pop_stack(state)
	a = pop_stack(state)
	try:
		push_stack(state, a // b)
		push_stack(state, a % b)
	except ZeroDivisionError:
		raise MathError("division by zero") from None

def swap(state):
	b = pop_stack(state)
	a = pop_stack(state)
	push_stack(state, b)
	push_stack(state, a)