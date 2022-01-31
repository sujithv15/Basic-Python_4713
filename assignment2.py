class Assignment2:

        def __init__(self, year):
                self.year = year

        def tellAge(self, currentYear):
                age = currentYear - self.year
                print("Your age is", age)

        def listAnniversaries(self):
                anniversaryYear = self.year + 10
                currentYear = 2022
                anniversaries = []
                while anniversaryYear < currentYear:
                        tempStr = ""
                        tempStr = tempStr + str(anniversaryYear)[2]
                        tempStr = tempStr + str(anniversaryYear)[3]
                        anniversaries.append(tempStr)
                        anniversaryYear += 10
                return anniversaries

        def modifyYear(self, n):
                var1 = ""
                for i in range(n):
                        var1 = var1 + str(self.year)[0]
                        var1 = var1 + str(self.year)[1]

                tempStr = str(self.year * n)
                var2 = ""
                i = 0
                while (i < len(tempStr)):
                        var2 = var2 + tempStr[i]
                        i += 2

                return var1 + var2

        def checkGoodString(string):
                numDigits = 0
                if (len(string) >= 8 and string[0].islower()):
                        for item in string:
                                if item.isdigit():
                                        numDigits+=1
                        if numDigits == 1:
                                return True
                return False