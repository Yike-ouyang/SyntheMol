from calc_props import smiles_to_ob, average_properties
import math

def scoring(properties):
    rb = math.exp(-properties["rb"])
    glob = math.exp(-properties["glob"])
    return (rb + glob + int(properties["primary_amine"]))/3

def calculate(smiles):
    mol = smiles_to_ob(smiles)
    properties = average_properties(mol)
    print(smiles)
    #print(properties)
    score=scoring(properties)
    print(score)
    return score

calculate("O=C(O)[C@@H]2N3C(=O)[C@@H](NC(=O)[C@@H](c1ccccc1)N)[C@H]3SC2(C)C")

