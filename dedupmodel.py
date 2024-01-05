#!/usr/bin/env python3
import ast
import sys
data = ast.literal_eval(sys.stdin.read())
known_ships = {}
known_models = {}
replace_edges = {'SPLINTER': 'ESCAPE_POD', 'THARGON': 'CANISTER'}
for s in data:
    if s[0] not in ('COBRA_MK_3_P', 'PYTHON_P', 'ROCK_HERMIT'):
        model = s[1:]
        if s[0] in known_ships:
            if known_ships[s[0]] != model:
                print(s[0], file=sys.stderr)
            assert known_ships[s[0]] == model
        else:
            assert len(model[0])
            assert len(model[1]) or s[0] in replace_edges
            assert len(model[2])
            if s[0] in replace_edges:
                model = model[0], known_ships[replace_edges[s[0]]][1], model[2]
            known_ships[s[0]] = model
            if s[1:] in known_models:
                print(s[0], known_models[model], file=sys.stderr)
            assert s[1:] not in known_models
            known_models[model] = s[0]
order = [
'MISSILE', 'CORIOLIS', 'DODO', 'ESCAPE_POD', 
'PLATE', 'CANISTER', 'BOULDER', 'ASTEROID', 
'SPLINTER', 'SHUTTLE', 'TRANSPORTER', 'COBRA_MK_3', 
'PYTHON', 'BOA', 'ANACONDA', 'VIPER', 
'SIDEWINDER', 'MAMBA', 'KRAIT', 'ADDER', 
'GECKO', 'COBRA_MK_1', 'WORM', 'ASP_MK_2', 
'FER_DE_LANCE', 'MORAY', 'THARGOID', 'THARGON', 
'CONSTRICTOR', 'LOGO', 'COUGAR', 
]

print('"use strict";')
print('window.shipdata = [')
for i in order:
    if i in known_ships:
        vs, es, fs = known_ships[i]
        vs = [list(x) for x in zip(*(vs[i::8] for i in range(8)))]
        es = [list(x) for x in zip(*(es[i::5] for i in range(5)))]
        fs = [list(x) for x in zip(*(fs[i::4] for i in range(4)))]
        print(f'{{ shipname: \'{i}\', vertexes: {vs}, edges: {es}, faces: {fs} }},')
print('];')
