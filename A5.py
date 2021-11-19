
def printCalendar(year): 
    ny=0
    ly=0
    for i in range(1753,year):
        if i%400==0:
            ly+=1
        elif i%100==0:
            ny+=1
        elif i%4==0:
            ly+=1
        else:
            ny+=1
    days = 365*ny + 366*ly
    day1=days%7
    if year%400==0:
        leapyear=True
    elif year %100==0:
        leapyear=False
    elif year%4==0:
        leapyear=True
    else:
        leapyear=False

    weekcount=6
    jan=[]
    c=0
    cdays=0
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        jan.append(storage)
    

    feb=[]
    c=0
    cdays=0
    day1=(day1+31)%7
    if leapyear:
        febdays=29
    else:
        febdays=28

    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+febdays:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        feb.append(storage)
    

    march=[]
    c=0
    cdays=0
    day1=(day1+febdays)%7

    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        march.append(storage)
    

    april=[]
    c=0
    cdays=0
    day1=(day1+31)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+30:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        april.append(storage)
    

    may=[]
    c=0
    cdays=0
    day1=(day1+30)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        may.append(storage)
    

    june=[]
    c=0
    cdays=0
    day1=(day1+31)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+30:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        june.append(storage)
    

    july=[]
    c=0
    cdays=0
    day1=(day1+30)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        july.append(storage)
    

    august=[]
    c=0
    cdays=0
    day1=(day1+31)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        august.append(storage)
    

    sep=[]
    c=0
    cdays=0
    day1=(day1+31)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+30:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        sep.append(storage)
    
    
    oct=[]
    c=0
    cdays=0
    day1=(day1+30)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        oct.append(storage)
    

    nov=[]
    c=0
    cdays=0
    day1=(day1+31)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+30:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        nov.append(storage)
    

    dec=[]
    c=0
    cdays=0
    day1=(day1+30)%7
    for i in range (weekcount):
        storage =""
        for j in range(7):
            if c<day1:
                storage+="   "
            elif cdays<(9):
                storage+="  "+str(cdays+1)
                cdays+=1
            elif c<day1+31:
                storage+=" " +str(cdays+1)
                cdays+=1
            else:
                storage+="   "
            c+=1
        dec.append(storage)

    line1 = "                                    "+str(year)+"                                  "
    m1="      -JANUARY_                  -FEBRUARY-                  -MARCH-       "
    m2="       -APRIL-                     -MAY-                     -JUNE-         "
    m3="        -JULY-                    -AUGUST-                 -SEPTEMBER-      "
    m4="      -OCTOBER-                  -NOVEMBER-                -DECEMBER-      "
    days="  M  T  W  T  F  S  S       M  T  W  T  F  S  S       M  T  W  T  F  S  S "
    f=open("calendar.txt","w+")
    f.write(line1+"\r\n")
    f.write(m1+"\r")
    f.write(days+"\r")
    for i in range(6):
        f.write(jan[i]+"     "+feb[i]+"     "+march[i]+"\r")
    f.write("\r")
    f.write(m2+"\r")
    f.write(days+"\r")
    for i in range(6):
        f.write(april[i]+"     "+may[i]+"     "+june[i]+"\r")
    f.write("\r")
    f.write(m3+"\r")
    f.write(days+"\r")
    for i in range(6):
        f.write(july[i]+"     "+august[i]+"     "+sep[i]+"\r")
    f.write("\r")
    f.write(m4+"\r")
    f.write(days+"\r")
    for i in range(6):
        f.write(oct[i]+"     "+nov[i]+"     "+dec[i]+"\r")
    f.close()

    

printCalendar(2021)


