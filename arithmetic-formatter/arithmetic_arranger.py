def arithmetic_arranger(problems, show = False):
  first = ""
  op = ""
  dashes = ""
  second = ""
  sumup = ""
  answer = ""
  sum = ""


  if(len(problems) > 5):
    return "Error: Too many problems."

  for problem in problems:
    first_num = problem.split(" ")[0]
    op = problem.split(" ")[1]
    second_num = problem.split(" ")[2]

    if (len(first_num) > 4 or len(second_num) > 4):
      return "Error: Numbers cannot be more than four digits."

    if not first_num.isnumeric() or not second_num.isnumeric():
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
    sltn = str(sum.rjust(length))
    
   
    dash_line = ""
    for dash in range(length):
      dash_line += "-"

    if problem != problems[-1]: 
      first += first_line + '    '
      second += second_line + '    '
      dashes += dash_line + '    '
      sumup += sltn + '    '
    else: 
      first += first_line
      second += second_line 
      dashes += dash_line 
      sumup += sltn  

  if show: 
    answer = first + "\n" + second + "\n" + dashes + "\n" + sumup
  else:
    answer = first + "\n" + second + "\n" + dashes    
  return answer