class Solution:
    def isAdditiveNumber(self, num):
        def checkAdditive(leading1, leading2, num):
            # leading1, leading2 and num are all strings. Leading1 and leading2 are the starting two integers
            # we want to check if num is the additive number generated by the two leading numbers
            generated_num = leading1 + leading2
            n = len(num)
            while len(generated_num) < n:
                temp = str(int(leading1) + int(leading2))
                generated_num = generated_num + temp
                leading1 = leading2
                leading2 = temp
            if len(generated_num) > n:
                return False
            else:
                for i in range(n):
                    if num[i] != generated_num[i]:
                        return False
                return True
        
        n = len(num)
        max_n1 = (n-1)//2
        for n1 in range(1,max_n1+1):
            max_n2 = (n - n1)//2
            for n2 in range(1,max_n2+1):
                temp1 = num[0:n1]
                temp2 = num[n1:(n1+n2)]
                if checkAdditive(temp1, temp2, num):
                    if (temp1[0] == "0" and n1 >= 2) or (temp2[0] == "0" and n2 >= 2):
                        continue
                    else:
                        return True
        return False
