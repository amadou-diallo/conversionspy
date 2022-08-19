#!/user/bin/env python 3
#Conversions control prog by Amadou


from Converter import ConvFunc
def main():
    print("Welcome to the English-Metric Converter\n")

    Usingk = False
    kchoice = input(" Would you like to see degree Kelvin(K) in the results? (Y/N)\n")
    if len(kchoice) > 0 and kchoice[0].upper() == "Y":
        Usingk = True
    
    choice = getChoice()
    while choice != 0:
        try:
            if choice == 1:
                mi = getValue("Enter your Miles: ")
                ki = ConvFunc.MitoKi(mi)
                print(str(mi) + " Miles = " + str(round(ki,3)) + " Kilometers.")

            elif choice == 2:
                oz = getValue("Enter your Ounces: ")
                gr = ConvFunc.OztoGr(oz)
                print(str(oz) + " Ounces = " + str(round(gr,3)) + " Grams.")

            elif choice == 3:
                f = getValue("Enter your Fahreinheit temperature: ")
                c = ConvFunc.FtoC(f)
                print(str(f) + " Fahreineit = " + str(round(c,3)) + " Celsius.")
                if Usingk:
                    k = ConvFunc.ShowdegreeK(c)
                    print(" which is also a temperature of: " + str(round (k,3)) + " Kelvin.")
            elif choice == 4:
                c = getValue("Enter your Celcius temp: ")
                f = ConvFunc.CtoF(c)
                print(str(c) + " Celsius = " + str(round(f,3)) + " Fahreinheit.")
                if Usingk:
                    k = ConvFunc.ShowdegreeK(c)
                    print(" which is also a temperature of: " + str(round (k,3)) + " Kelvin.")
            elif choice == 5:
                mt = getValue("Enter your Meters: ")
                ft = ConvFunc.MttoFt(mt)
                print(str(mt) + " Meters = " + str(round (ft,3)) + " Feet.")
            
            elif choice == 6:
                li = getValue("Enter your liters: ")
                gl = ConvFunc.LitoGl(gl)
                print(str(li) + " Liters = " + str(round(gl,3)) + " Gallons.")

            else:
                print("Unknown conversion.")
            
        except ValueError as e:
            print("Data Problem: " + str(e))
        except Exception as e:
            print("General Error: " + str(e))

        choice = getChoice()
        print()

    print("Thanks for Using the Converter.")

def getChoice():
    c = -1
    while c < 0 or c > 6:
        try:
            c = int(input("Convertion?(1=Mi-to-Km,  2=Oz-to-Gr, 3= F-to-C, 4=C-to-F, 5=M-to-Ft, 6=Li-to-Gal, 0=end): "))
            if c < 0 or c > 6:
                print("Convertions? 1 - 6 Only please. O= Quit")
        except ValueError:
            print("Illegal input! Positive integers only please ")
            c = -1
    return c

def getValue(prompt):
    goodVal = False
    while not goodVal:
        try:
            v = float(input(prompt))
            goodVal = True
        except:
            print(" Illegal Entries. Numbers Only Please! ")
            goodVal = False
    return v



if __name__ == "__main__":
    main()
            
            
                  
                  
        
    
    

            
                
                    
                          
            
                                          








