def arithmetic_arranger(problems, show_answers=False):
    # Step 1: Input validation
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_rows = []
    bottom_rows = []
    lines = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Incorrect problem format."
        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate result if show_answers is True
        if operator == '+':
            result = str(int(num1) + int(num2))
        elif operator == '-':
            result = str(int(num1) - int(num2))
        
        # Compute width for formatting
        width = max(len(num1), len(num2)) + 2
        
        # Format each line
        top_row = num1.rjust(width)
        bottom_row = operator + ' ' + num2.rjust(width - 2)
        line = '-' * width

        top_rows.append(top_row)
        bottom_rows.append(bottom_row)
        lines.append(line)
        if show_answers:
            answers.append(result.rjust(width))

    # Join all parts
    arranged_problems = '    '.join(top_rows) + '\n' + '    '.join(bottom_rows) + '\n' + '    '.join(lines)
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems
