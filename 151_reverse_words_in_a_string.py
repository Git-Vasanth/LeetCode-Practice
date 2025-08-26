# Question : Reverse Words in a String - 151

#### Solution 1 



class Solution_1:
    def reverseWords(self, s: str) -> str:

        s2 = s.split(" ")

        s3 = []

        result = []

        for i in range(0 , len(s2)):

            if len(s2[i]) > 0 :

                s3.append(s2[i])

        counter_at_s3 = len(s3) - 1

        while counter_at_s3 >= 0 :

            result.append(s3[counter_at_s3])

            counter_at_s3 -= 1

        result = " ".join(result)

        return result
    

### Done in 2 ms


#### Solution 2

class Solution_2:
    def reverseWords(self, s: str) -> str:

        return " ".join(s.split()[::-1])
    
### Done in 0 ms