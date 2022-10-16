def compSeq(DNA_seq, direction = 'same'):
    comp_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} #dictionary declaration
    comp = '' #declaring output originally as an empty string
    DNA_seq = DNA_seq.upper() #to take care of lowercase letters in input
    
    #everything in the if statement is executed with the direction argument specified as 'reverse'
    if direction == 'reverse':
        for nuc in DNA_seq[::-1]: #iteration in reverse order
            if nuc in comp_dict: #in case there are characters that are not actually DNA nucleotides
                comp += comp_dict[nuc]
    else:
        for nuc in DNA_seq:
            if nuc in comp_dict:
                comp += comp_dict[nuc]
    
    return comp
        