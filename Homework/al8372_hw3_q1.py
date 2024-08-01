from ArrayStack import ArrayStack

maths = '+-*/'
vars = []
var_vals = []

ui = ''
while ui != 'done()' or ui != 'done ()':
    s = ArrayStack()
    ui = input('-->')
    lst = ui.strip().split()

    if ui == 'done()' or ui == 'done ()':
        break
    
    if '=' in lst:
        variable = lst[0]
        expression = lst[2:]
        
        for each in expression:
            if each.isdigit():
                s.push(int(each))
            elif each in vars:
                s.push(var_vals[vars.index(each)])
            elif each in maths:
                num2 = s.pop()
                num1 = s.pop()
                if each == '+':
                    s.push(num1 + num2)
                elif each == '-':
                    s.push(num1 - num2)
                elif each == '*':
                    s.push(num1 * num2)
                elif each == '/':
                    s.push(num1 / num2)
        
        value = s.pop()
        if variable in vars:
            var_vals[vars.index(variable)] = value
        else:
            vars.append(variable)
            var_vals.append(value)
        print(variable)
    else:
        for each in lst:
            if each.isdigit():
                s.push(int(each))
            elif each in vars:
                s.push(var_vals[vars.index(each)])
            elif each in maths:
                num2 = s.pop()
                num1 = s.pop()
                if each == '+':
                    s.push(num1 + num2)
                elif each == '-':
                    s.push(num1 - num2)
                elif each == '*':
                    s.push(num1 * num2)
                elif each == '/':
                    s.push(num1 / num2)
        
        result = s.pop()
        print(result)
