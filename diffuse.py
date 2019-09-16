from random import choice
npart=600
##side=55  #Should be an odd number
##time=0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
for side in range(21,102,10):
    grid=[[0 for x in range(side)] for y in range(side)]
    time=0
    for ipart in range(npart):
        # Start particle at origin
        x,y = side//2,side//2
        counter=0
        # perform the random walk until particle aggregates
        while 1:
            counter+=1
            grid[x][y]=0   #Remove particle from current spot
            # Randomly move particle
            sx,sy = choice(steps)
            x += sx
            y += sy
            # Enforce periodic boundaries
            if x<0 or y<0 or x==side or y==side:
                time+=counter
                break
            grid[x][y]=1   #Put particle in new location
    avetime=time/npart
    print("side=%d <t>=%5.2f <t>/r2=%5.2f"%(side,avetime,avetime/(side**2)))
