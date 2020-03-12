class Solution(object):
    def gcdOfStrings(self, str1, str2):
        gcd_=self.gcd(len(str1),len(str2))
        str_gcd=str1[0:gcd_]
        if str_gcd*(len(str1)//gcd_)==str1 and str_gcd*(len(str2)//gcd_)==str2:
            return str_gcd
        return ''

    def gcd(self,a0,b0):
        a=max(a0,b0)
        b=min(a0,b0)
        while a%b!=0:
            temp=a%b
            a=b
            b=temp
        return b

        """
        :type str1: str
        :type str2: str
        :rtype: str
        """