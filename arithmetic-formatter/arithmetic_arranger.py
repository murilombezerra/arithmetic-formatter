def arithmetic_arranger(problems, show = False):

  # Variables
  first = ""
  op = ""
  dashes = ""
  second = ""
  sumup = ""
  arithmetic_arranger = ""
  sum = ""
  len_problems = len(problems)

  if len_problems > 5:
    return "Error: Too many problems."

  for problem in problems:
    first_num = problem.split(" ")[0]
    op = problem.split(" ")[1]
    second_num = problem.split(" ")[2]

    len_first = len(first_num)
    len_second = len(second_num)
    
    if len_first > 4 or len_second > 4:
      return "Error: Numbers cannot be more than four digits."

    if not first_num.isdigit() or not second_num.isdigit():
      return "Error: Numbers must only contain digits."
    
    if (op == '+' or op == '-'):
      if op == "+": 
        sum = str(int(first_num) + int(second_num))
      if op == "-":
        sum = str(int(first_num) - int(second_num))
    else: 
      return "Error: Operator must be '+' or '-'."

    length = max(len(first_num) , len(second_num)) + 2
    first_line = str(first_num).rjust(length)
    second_line = op + str(second_num.rjust(length - 1))
    sum_line = str(sum.rjust(length))
    
   
    dash_line = ""
    for d in range(length):
      dash_line += "-"

    if problem != problems[-1]: 
      first += first_line + '    '
      second += second_line + '    '
      dashes += dash_line + '    '
      sumup += sum_line + '    '
    else: 
      first += first_line
      second += second_line 
      dashes += dash_line 
      sumup += sum_line  

  if show: 
    arithmetic_arranger = first + "\n" + second + "\n" + dashes + "\n" + sumup
  else:
    arithmetic_arranger = first + "\n" + second + "\n" + dashes    
    
  return arithmetic_arranger