def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    i=0
    while i<len(list1):
        if list1[0]>list1[-1]:
            return list1[0]
        else:
            return list1[-1]
        i+=1
list1=[2,0,0,0,3]
print(main(list1))
