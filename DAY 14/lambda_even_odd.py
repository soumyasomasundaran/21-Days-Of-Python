# lambda_expr ::=  "lambda" [parameter_list] ":" expression
evenodd = lambda x: 'even' if x % 2 == 0 else 'odd'
print(evenodd(10))
