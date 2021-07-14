import random,time
def rain(f):
    r='/'
    starts=[]
    
    while True:
        place=[' ']*3200
        for i in range(f):
            starts.append(str(random.randint(18,80)))
        for idx,i in enumerate(starts):
            if int(i)>=3200:
                starts.pop(idx)
            else:  
                place[int(i)]=r
                starts[idx]=str(int(i)+79)
        print('_'*80)            
        print(''.join(place))

        #time.sleep(0.01)
rain(3)
