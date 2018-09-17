#!python
#

kr = [50000,10000,5000,1000,500,100,50,10] #All kind of won
price = 46300 # example
kr_nums =[] # needed number of won

#divide from max to min
for won in kr:
    if(price > won):
        kr_nums = int(price / won)
        price = price - (kr_nums*won)
        print(won)
        print(kr_nums)
        print()
    else:
        kr_nums = 0
        print(won)
        print(kr_nums)
        print()

        
