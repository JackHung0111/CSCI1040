# 1155108381
# Quiz Q2

def validate(number):
    if len(number) < 13 or len(number) > 16:
        return False
    else:
        nList = []
        single = []
        double = []
        double_temp = []
        for i in range(len(number)):
            nList.append(int(number[i]))
        temp = nList.copy()
        temp.reverse()
        for i in range(len(number)):
            if(i%2 == 0):
                single.append(temp[i])
            else:
                double.append(temp[i])
        for i in range(len(double)):
            k = int(double[i]) * 2
            if (k >= 10):
                k -= 9
            double_temp.append(k)
        total = sum(double_temp) + sum(single)
        if (total % 10 > 0):
            return False
        else:
            return True
