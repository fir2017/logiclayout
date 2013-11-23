# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import parser
# import serializer
from optimizer2 import Tree

# -----------------------------------------------------------------------------
# Run PLY yacc in the parser module.
# -----------------------------------------------------------------------------

yacc = parser.run_yacc

# -----------------------------------------------------------------------------

def clear_parser():
	""" Empties root of pre-exisiting root tokens. """
	parser.root = []

def compiler(data, debug=0, print_tree=1):
	""" Run compiler on a logic expression. """
	clear_parser()
	yacc.error = 0
	yacc.parse(data)

	if yacc.error:
		return None

	tree = Tree(parser.root[0], data)
	tree.print_tree()
	tree.print_nodes()
	# tree.print_levels()
	# json_data = serializer.to_json(tree)

	# return json_data

# def parse_expression(expr, debug=0):
# 	""" Run parser on one expression and return a tree of that expression. """
# 	clear_parser()
# 	yacc.error = 0
# 	yacc.parse(expr)

# 	if yacc.error:
# 		return None

# 	return Tree(parser.root[0])

# def compiler_multiple(data, debug=0, print_tree=1):
# 	""" Run compiler on a logic expression. """

# 	parser_trees = []

# 	for expr in data:
# 		new_tree = parse_expression(expr)
# 		parser_trees.append(new_tree)

# 		print "*"*80
# 		new_tree.print_tree()
# 		print "*"*80
# 		new_tree.print_levels()	
# 		print "*"*80

# 	return None
