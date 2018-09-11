# Enter your code here. Read input from STDIN. Print output to STDOUT

# QUESTION:
# A cool string S is where each distinct character occurs same number of times in S.
# e.g. "aabbcc" and "cba" and "aaa" is cool but "aabbccd" and "ddcba" is not.

# ddcba -> [2, 1, 1, 1] -> [1, 2] 
# abbbccc -> [1, 3, 3] -> [1, 3]
# abbcc -> [1, 2, 2] -> [1,2]
# Write me a function which returns true if a string is cool or can be made cool by removing one character.
# e.g.  Return true for "aab" (remove b or a), or "aabb"  but false for "aabbcd" (have to remove two, either a and b, or c and d)

# aab -> ab
# aab -> aa
from sets import Set
def can_be_made_cool(input_str):
    
    # first let's try to figure out the number of characters and their occurences
    tmp_cnt = {}
    for idx in range(0, len(input_str)):
        char = input_str[idx]
        if tmp_cnt.has_key(char): # this character appears onece before
            cnt = tmp_cnt.get(char)
        else:
            cnt = 0
        tmp_cnt[char] = cnt + 1
        
    uniq_occur = list(Set(tmp_cnt.values()))
    if len(uniq_occur) == 1:
        return True
    elif len(uniq_occur) == 2:
        if abs(uniq_occur[0] - uniq_occur[1] ) == 1:
            # the max number only occurs once tmp_cnt -> return True
            max_val = max(tmp_cnt.values())
            if tmp_cnt.values().count(max_val) == 1:
                return True
           
        # if min is 1, 1 occurs only once -> return True
        min_val = min(tmp_cnt.values())
        if tmp_cnt.values().count(min_val) == 1 and min_val == 1:
            return True
        
        return False
 
    else:
        return False
    
    

# TEST CASES:
assert can_be_made_cool("aaa") is True
assert can_be_made_cool("aabb") is True
assert can_be_made_cool("aabbc") is True
assert can_be_made_cool("aabbccc") is True
assert can_be_made_cool("aabbccddd") is True
assert can_be_made_cool("abbccc") is False
assert can_be_made_cool("aaabbbcc") is False
assert can_be_made_cool("aaabbbcc") is False
assert can_be_made_cool("aabbcccc") is False
