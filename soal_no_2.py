class Main:
    def isPalindrome(self, x):
        # x: int
        str_x = str(x)
        return str_x == str_x[::-1]

main = Main()
x = 121
print(main.isPalindrome(x))