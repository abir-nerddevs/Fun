import itertools

inp_string = "123456789"
operator_combinations = itertools.product(["+","-",""], repeat=9) #Generates Cartesian product of nine ["+","-",""] amounting 3^9 nunmber of combinations
answers = []

for each_operator_combination in operator_combinations:
  if(each_operator_combination[0] != "+"):
    expression_tuples = zip(each_operator_combination, inp_string) #Generates expression tuples combining operators and digits
    expression = "".join("".join(each_tuple) for each_tuple in expression_tuples) #converts the tuples to string => [(-,1),(+,2)] => '-1+2'
    if(eval(expression) == 100):
      answers.append(expression)

print("Total Results: " + str(len(answers)))

for each_expression in answers:
  print(each_expression)
