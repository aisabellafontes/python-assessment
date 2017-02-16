"""
Ranson Note Magazine
@aisabellafontes

Output Format

Print Yes if he can use the magazine to create an untraceable 
replica of his ransom note; otherwise, print No.

Sample Input

6 4
give me one grand today night
give one grand today


Sample Output

Yes
Explanation

All four words needed to write an untraceable replica of the 
ransom note are present in the magazine, so we print Yes as our answer.

"""


def ransom_note(magazine, ransom):
    flag = True
    for word in ransom:
        if word in magazine: #remove 
           magazine.remove(word)
        else:
            flag = False
            break
    return flag
    
def ransom_note_quickly(m, r):
    pass
        
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
