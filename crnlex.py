import ply.lex as lex
import ply.yacc as yacc
import crn

reserved = {
    'VOLUME' : 'VOLUME',
    'TIME' : 'TIME',
    'DETERMINISTIC' : 'DETERMINISTIC',
    }

tokens = ['SPECIES', 'REAL', 'INTEGER', 'PLUS', 'HYPHEN', 'ARROWTO',
          'ARROWFROM', 'EQUALS'] + list(reserved.values())

def t_SPECIES(t):
    r'[A-Za-z][^=\+-<># \t\n]*'
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
t_HYPHEN = r'-'
t_ARROWTO = r'>'
t_ARROWFROM = r'<'
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
deterministic = False
concentrations = {}
reactions = []
error = False

def p_stmt_concentration(p):
    'stmt : SPECIES EQUALS number'
    if p[1] in concentrations:
        print('Warning: concentration for %s redefined' %p[1])
    concentrations[p[1]] = p[3]

def p_stmt_volume(p):
    'stmt : VOLUME EQUALS INTEGER'
    global volume
    if volume != 0:
        print('Warning: volume redefined')
    volume = int(p[3])

def p_stmt_time(p):
    'stmt : TIME EQUALS INTEGER'
    global time
    if time != 0:
        print('Warning: time redefined')
    time = int(p[3])

def p_stmt_deterministic(p):
    'stmt : DETERMINISTIC'
    global deterministic
    deterministic = True

def p_number(p):
    '''number : REAL
            | INTEGER'''
    p[0] = p[1]

def p_stmt_empty(p):
    'stmt : '
    pass

def p_stmt_reaction(p):
    '''stmt : molecules HYPHEN number ARROWTO molecules
            | molecules ARROWFROM number HYPHEN molecules
            | molecules HYPHEN ARROWTO molecules
            | molecules ARROWFROM HYPHEN molecules'''
    prod = p[len(p)-1]
    rate = p[3] if len(p) == 6 else 1
    if p[1] == [] and prod == []:
        print('Warning: empty -> empty rule defined')
    if p[2] == '-':
        reactions.append((p[1], prod, rate))
    else:
        reactions.append((prod, p[1], rate))

def p_molecules_rule(p):
    '''molecules : molecule PLUS molecules
                 | molecule
                 | '''
    if len(p) == 4:
        p[0] = dict(p[3])
        if p[1][1] in p[3]:
            p[0][p[1][1]] += p[1][0]
        else:
            p[0][p[1][1]] = p[1][0]
    elif len(p) == 2:
        p[0] = {p[1][1] : p[1][0]}
    else:
        p[0] = {}

def p_molecule_rule(p):
    '''molecule : INTEGER SPECIES
                | SPECIES'''
    if len(p) == 3:
        p[0] = (p[1],p[2])
    else:
        p[0] = (1,p[1])

def p_error(p):
    global error
    if p:
        print("Syntax error at '%s'" %p.value)
    else:
        print("Syntax error at EOF")
    error = True

yacc.yacc()

''' Returns True if successfully parsed, False otherwise '''
def crnlex(filename):
    global concentrations, reactions, volume, time, error
    concentrations = {}
    reactions = []
    volume = 0
    time = 0
    error = False
    with open(filename) as z:
        for line in z.readlines():
            yacc.parse(line)
            if error: return False
    if time == 0:
        # fixme: default value probably better
        print('Time not defined; please set the value TIME to an integer')
        return False
    if volume == 0:
        # fixme: default value probably better
        print('Volume not defined; please set the value VOLUME to an integer')
        return False
    crn.crn(reactions, concentrations, volume, time, deterministic)
    return True
