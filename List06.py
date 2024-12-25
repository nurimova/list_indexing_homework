def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    while i<5:
        if '1' in list1:
            indx=list1.index(1)
            list1[indx]='True'
        i+=1
        return list2 
list1=['1','0','0','1']
print(main(list1))