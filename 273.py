class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'

        below_ten = ["", "One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        below_twenty = ["Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        below_hundred = ["", "Ten", "Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

        # Hundred -> Thousand -> Million -> Billion


        def helper(num):
            if num < 10:
                res = below_ten[num]
            elif num < 20:
                res = below_twenty[num - 10]
            elif num < 100:
                res = below_hundred[num // 10] + ' ' + helper(num % 10)
            elif num < 1000:
                res = helper(num // 100) + ' Hundred ' + helper(num % 100)
            elif num < 1000000:
                res = helper(num // 1000) + ' Thousand ' + helper(num % 1000)
            elif num < 1000000000:
                res = helper(num // 1000000) + ' Million ' + helper(num % 1000000)
            else:
                res = helper(num // 1000000000) + ' Billion ' + helper(num % 1000000000)

            return res.strip()


        return helper(num)



