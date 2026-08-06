def filterX(task,Elements):
    Result = list()

    for no in Elements:
        Ret = task(no)      #checkEven(no)

        if (Ret == True):
            Result.append(no)

    return Result

def mapX(task,Elements):
    Result = list()

    for no in Elements:
        Ret = task(no)      #Increment(no)
        Result.append(Ret)

    return Result

def reduceX(task,Elements):
    sum = 0

    for no in Elements:
        sum = task(sum,no)

    return sum
