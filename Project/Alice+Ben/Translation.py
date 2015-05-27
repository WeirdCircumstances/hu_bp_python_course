# coding=utf-8
__author__ = 'Alice'
'''
# Sequenz zufällig aus AUCG durch 3 teilbar
# nach erstem AUG suchen
# Codons Aminosäuren zuordnen
# bei * abbrechen
# Output mit Aminosäuren
'''
code = dict([('UCA', 'S'), ('UCG', 'S'), ('UCC', 'S'), ('UCU', 'S'),
                 ('UUU', 'F'), ('UUC', 'F'), ('UUA', 'L'), ('UUG', 'L'),
                 ('UAU', 'Y'), ('UAC', 'Y'), ('UAA', '*'), ('UAG', '*'),
                 ('UGU', 'C'), ('UGC', 'C'), ('UGA', '*'), ('UGG', 'W'),
                 ('CUA', 'L'), ('CUG', 'L'), ('CUC', 'L'), ('CUU', 'L'),
                 ('CCA', 'P'), ('CCG', 'P'), ('CCC', 'P'), ('CCU', 'P'),
                 ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'),
                 ('CGA', 'R'), ('CGG', 'R'), ('CGC', 'R'), ('CGU', 'R'),
                 ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'),
                 ('ACA', 'T'), ('ACG', 'T'), ('ACC', 'T'), ('ACU', 'T'),
                 ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'),
                 ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'),
                 ('GUA', 'V'), ('GUG', 'V'), ('GUC', 'V'), ('GUU', 'V'),
                 ('GCA', 'A'), ('GCG', 'A'), ('GCC', 'A'), ('GCU', 'A'),
                 ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
                 ('GGA', 'G'), ('GGG', 'G'), ('GGC', 'G'), ('GGU', 'G')])

def energy(value):
    atp = len(value)
    gtp = 4*len(value)
    return '{0} ATP und {1} GTP wurden verbraucht.'.format(atp,gtp)

sequence = 'UUUGACAUGAGAGACAGGGGGUGAGGUGGA'

start = False
ende = False

codon = list()

i=0
while (i<len(sequence)/3):
    a=sequence[3*i:(3*i)+3]

    amino_acid = code[a]

    if not start:
        if (amino_acid == 'M'):
            start = i
    if start and not ende:
        if (amino_acid == '*'):
            ende = i
    codon.append(amino_acid)
    i += 1


codon = codon[start:ende] # merkt sich vorher i bei start und ende


print (codon)


print (energy(codon))



b=1





