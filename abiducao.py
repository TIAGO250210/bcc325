# Esse codigo foi produzido em parcerian com meiu colega joao
# tiago gomes da silva, matricula 19.2.4009

kb = {
    'rules':{
        'bronchitis':[['influenza'],['smokes']],
        'coughing':[['bronchitis']],
        'wheezing':[['bronchitis']],
        'fever':[['influenza'],['infection']],
        'sore_throat':[['influenza']],
        'False':[['smokes','nonsmoker']]},
    'assumables':['smokes', 'nonsmoker', 'influenza','infection'],
    }

def ask(askable):
    ans = input(f'Is {askable} true?')
    return True if ans.lower() in ['sim','s','yes','y'] else False

import itertools

def top_down(kb, observations):
    Gs = []
    for observation in observations:    
        G = {observation}
        while False in [each in kb['assumables'] for each in G]:
            head = None
            for a in G:
                if a not in kb['assumables']:
                    head = a
                    break
            for tails in kb['rules'][head]:
                for tail in tails:
                    G.add(tail)
            G.remove(head)
        Gs.append(G)
    return [set(each) for each in itertools.product(*Gs)]

def get_minimal_explanations(explanations):
    not_minimal = []
    for i in range(len(explanations)):
        for j in range(len(explanations)):
            if explanations[i].issubset(explanations[j]) and i != j:
                not_minimal.append(j)

    return [explanations[i] for i in range(len(explanations)) if i not in not_minimal]

Gs = top_down(kb, ['wheezing', 'fever'])
print(Gs)
print(get_minimal_explanations(Gs))

