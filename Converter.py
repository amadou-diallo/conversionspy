#Converter classs for Eng-Metric conversions by..

class ConvFunc:

    @staticmethod
    def MitoKi(mi):
        if not isinstance(mi,(int,float)):
            mi = float(mi)
        if mi < 0:
            raise ValueError("Negative values not legal for miles.")
        ki = mi * 1.60934
        return ki

    @staticmethod
    def OztoGr(oz):
        if not isinstance(oz,(int,float)):
            oz = float(oz)
        if oz < 0:
            raise ValueError("Negative values not legal for Ounces.")
        gr = oz * 28.3495
        return gr
    
    @staticmethod
    def ShowdegreeK(c):
        if not isinstance(c,(int,float)):
            c = float(c)
        k = c + 273.15
        if k < 0:
            raise ValueError("temp not possible as it is below absolute zero.")
        return k

    @staticmethod
    def FtoC(f):
        if not isinstance(f,(int,float)):
            f = float(f)
        c = (5.0/9.0) *(f - 32.0)
        ConvFunc.ShowdegreeK(c)
        return c
    
    @staticmethod
    def CtoF(c):
        if not isinstance(c,(int,float)):
            c = float(c)
        f = (9.0/5.0) *( c + 32.0)
        ConvFunc.ShowdegreeK(c)
        return f

    @staticmethod
    def MttoFt(mt):
        if not isinstance(mt,(int,float)):
            mt = float(mt)
        if mt < 0:
            raise ValueError("Negative values not legal ")
        ft = mt * 3.2808
        return ft
    @staticmethod
    def LitoGl(li):
        if not isinstance(li,(int,float)):
            li = float(li)
        if li < 0:
            raise ValueError("Negative values not legal")
        gl = li * 0.26417 
        return gl
    
                
                
                


    

    
