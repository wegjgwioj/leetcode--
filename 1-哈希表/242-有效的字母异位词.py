
def isAn(s:str,t:str) -> bool:
    s_sort =''.join(sorted(s))
    t_sort =''.join(sorted(t))
    if s_sort == t_sort:
        return True
    
    return False



if __name__ == "__main__":
    print(isAn("anagram","nagaram"))
    print(isAn("rat","car"))