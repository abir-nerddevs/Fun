import itertools

inp_string = "123456789"
operator_combinations = itertools.product(["+","-",""], repeat=9)
answers = []

for each_operator_combination in operator_combinations:
  if(each_operator_combination[0] != "+"):
    expression_tuples = zip(each_operator_combination, inp_string)
    expression = "".join("".join(each_tuple) for each_tuple in expression_tuples)
    if(eval(expression) == 100):
      answers.append(expression)

print("Total Results: " + str(len(answers)))

for each_expression in answers:
  print(each_expression)