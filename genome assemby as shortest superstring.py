# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 23:33:46 2024

@author: gbulb
"""

dict_strings={'Rosalind_56': 'ATTAGACCTG', 'Rosalind_57' : 'CCTGCCGGAA',  'Rosalind_58': 'AGACCTGCCG', 'Rosalind_59': 'GCCGGAATAC'}

def find_min_len_of_keys(dict_strings):
    list_of_lens=[]
    for key in dict_strings.keys():
        list_of_lens.append(len(dict_strings[key]))
    return max(list_of_lens)
max_len=find_min_len_of_keys(dict_strings)
class substrings_to_superstring:
    def substrings_to_string(dict_strings):
        STRING=''
        for key in dict_strings.keys():
            for i in range(0,max_len,3):
                if dict_strings[key][i:i+3] not in STRING:
                   STRING+=dict_strings[key][i:i+3]
                if key==list(dict_strings.keys())[-1]:
                    if STRING[len(STRING)-1]!=dict_strings[key][-1]:
                       STRING+=dict_strings[key][-1]
        return print(STRING)
               

        
if __name__ == "__main__":
    substrings_to_superstring.substrings_to_string(dict_strings)