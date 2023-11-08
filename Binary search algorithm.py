'''
Binary serach
'''

def binarysearch(a_list,an_item):
    first=0
    last=len(a_list)-1

    while first<=last:
        mid_point=(first+last)//2
        if a_list[mid_point]==an_item:
            return True
        else:
            if an_item<a_list[mid_point]:
                last=mid_point-1
            else:
                first=mid_point+1
    return False
'''
Recursion
'''


if __name__== '__main__':
    a_list=[19,26,3,24,5,6,7,7,22,9,9,0]

    print('Binary search:',binarysearch(a_list,0))
