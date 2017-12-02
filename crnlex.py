import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'VOLUME' : 'VOLUME',
    'TIME' : 'TIME'
    }

tokens = ['SPECIES', 'INTEGER', 'REAL', 'PLUS', 'ARROWTO', 'ARROWFROM',
          'EQUALS'] + list(reserved.values())

def t_SPECIES(t):
    r'[A-Za-z][^=\+-<># \t\n]+'
    t.type = reserved.get(t.value, 'SPECIES')
    return t

def t_REAL(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

t_PLUS = r'\+'
t_ARROWTO = r'->'
t_ARROWFROM = r'<-'
t_EQUALS = r'='

def t_COMMENT(t):
    r'\#.*'
    pass

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

volume = 0
time = 0
concentrations = {}
reactions = []

def p_stmt_concentration(p):
    'stmt : SPECIES EQUALS number'
    if p[1] in concentrations:
        print('Warning: concentration for %s redefined' %p[1])
    print('Setting concentration for',p[1],'to',p[3])
    concentrations[p[1]] = p[3]

def p_stmt_volume(p):
    'stmt : VOLUME EQUALS number'
    global volume
    if volume != 0:
        print('Warning: volume redefined')
    print('setting volume')
    volume = float(p[3])

def p_stmt_time(p):
    'stmt : TIME EQUALS number'
    global time
    if time != 0:
        print('Warning: time redefined')
    print('setting time')
    time = float(p[3])

def p_number(p):
    '''number : REAL
            | INTEGER'''
    p[0] = p[1]

def p_stmt_empty(p):
    'stmt : '
    pass

def p_stmt_reaction(p):
    '''stmt : molecules ARROWTO molecules
            | molecules ARROWFROM molecules'''
    if p[1] == [] and p[3] == []:
        print('Warning: empty -> empty rule defined')
    if p[2] == '->':
        reactions.append((p[1], p[3]))
    else:
        reactions.append((p[3], p[1]))
    print(p[1],p[2],p[3])

def p_molecules_rule(p):
    '''molecules : molecule PLUS molecules
                 | molecule
                 | '''
    if len(p) == 4:
        p[0] = p[3] + [p[1]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_molecule_rule(p):
    '''molecule : INTEGER SPECIES
                | SPECIES'''
    if len(p) == 3:
        p[0] = (p[1],p[2])
    else:
        p[0] = (1,p[1])

def p_error(p):
    print("Syntax error at '%s'" %p.value)

yacc.yacc()

with open('min_example.crn') as z:
    y = z.read()

##lexer.input(y)
##x = lexer.token()
##while x != None:
##    print(x)
##    x = lexer.token()

for line in y.split('\n'):
    yacc.parse(line)
