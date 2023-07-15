class Settings:
    FONT_SIZE=None
    FONT_COLOR=None
    FONT_TYPE= None
    FONT_WEIGHT=None
    REGISTERED=None
    SETTINGS=[
    {
        "font_size":{"large":24,"medium":18,"small":11}
        ,"font_color":"black"
        ,"font_type":"Arial"
        ,"font_weight":300
        ,"registered":0

    }
     
]

    def __init__(cls):
        cls.set_font_size()
        cls.set_font_color()
        cls.set_font_type()
        cls.set_font_weight()
        cls.set_registered()
        



    def set_font_size(cls):
        settings= cls.SETTINGS[0]
        cls.FONT_SIZE= settings["font_size"]

    def set_font_color(cls):
        settings= cls.SETTINGS[0]
        cls.FONT_COLOR= settings["font_color"]
    def set_font_type(cls):
        settings= cls.SETTINGS[0]
        cls.FONT_TYPE= settings["font_type"]
    def set_font_weight(cls):
        settings= cls.SETTINGS[0]
        cls.FONT_WEIGHT= settings["font_weight"]
    def set_registered(cls):
        settings= cls.SETTINGS[0]
        if  settings["registered"]==0:
            cls.REGISTERED= False
        else:
            cls.REGISTERED=True
        

    

def test():
    sett= Settings()
    print(sett.FONT_SIZE)
    print(sett.FONT_TYPE)
    print(sett.FONT_COLOR)
if __name__=="__main__":
    
    test()


# Impano Manzi Enock