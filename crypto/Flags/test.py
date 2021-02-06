def gen_flag(randlist):
    ans=randlist
    #length = randlist.length
    ans.insert(4,randlist[2])
    ans.insert(8,randlist[6])
    ans.insert(13,randlist[10])
    ans.insert(16,randlist[12])
    ans.insert(19,randlist[6])
    ans.insert(20,randlist[6])    
    return ans
def list_print(list):
    for i in list:
        print(i, end='')
    print('')

randlist =['P','I','C','O','T','F','{','L','A','G','E','H','I','J','K','}']
list = gen_flag(randlist)
list_print(list)
    