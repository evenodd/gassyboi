DIALECT_DISCONNECT = "disconnect"
DIALECT_CONNECT = "connect"
DIALECT_CO2_UP = "co2_up"
DIALECT_CO2_DOWN = "co2_down"
DIALECT_VOC_UP = "voc_up"
DIALECT_VOC_DOWN = "voc_down"

dialects = {
   "lame" : {
        DIALECT_DISCONNECT : "The sensor has been disconnected :slightly_frowning_face:",
        DIALECT_CONNECT : "The sensor has re-established a connection :smile:",
        DIALECT_CO2_UP :"Alert!! CO2 is at a %s level! :skull_and_crossbones: This occurs when CO2 reaches %d ppm. Last recorded value was %d ppm",
        DIALECT_CO2_DOWN : "CO2 level is no longer %s! :confetti_ball: The CO2 level is now at %s %d ppm ",
        DIALECT_VOC_UP : "Oh no!! Organic components in the air is at a %s level. :skull_and_crossbones: This occurs when VOCs reaches %d ppb\nLast recorded value was %d ppb",
        DIALECT_VOC_DOWN : "Organic components in the air is no longer at a %s level. :confetti_ball: The current VOC level is now merely at the %s %d ppb"
   },
   "cool" : {
        DIALECT_DISCONNECT : "Oh no plz help :slightly_frowning_face:, I cant connect to my sensors",
        DIALECT_CONNECT : "My sensors were disconnected but are now back up and running :smile:",
        DIALECT_CO2_UP :"Oh no!! CO2 is at a %s level! :skull_and_crossbones: This occurs when CO2 reaches %d ppm. Last recorded value was %d ppm",
        DIALECT_CO2_DOWN : "Hey guys, the CO2 levels are no longer %s! :confetti_ball: We are now only at the %s levels of %d ppm ",
        DIALECT_VOC_UP : "Oh no!! Organic components in the air are at a %s level. :skull_and_crossbones: This occurs when VOCs reaches %d ppb Last recorded value was %d ppb",
        DIALECT_VOC_DOWN : "Yo, organic components in the air are no longer at a %s level. :confetti_ball: The current level is now merely at the %s %d ppb"
   }
}

class Dialect :
    def __init__(self, dialect : str):
        self.dialect = dialects.get(dialect)

    def get_disconnect(self):
        return self.dialect.get(DIALECT_DISCONNECT)

    def get_connect(self):
        return self.dialect.get(DIALECT_CONNECT)

    def get_co2_up(self, level:str, lower_bound:int, value:int):
        return self.dialect.get(DIALECT_CO2_UP) % (level, lower_bound, value)

    def get_co2_down(self, prev_level:str, new_level:str, value:int):
        return self.dialect.get(DIALECT_CO2_DOWN) % (prev_level, new_level, value)    

    def get_voc_up(self, level:str, lower_bound:int, value:int):
        return self.dialect.get(DIALECT_VOC_UP) % (level, lower_bound, value)

    def get_voc_down(self, prev_level:str, new_level:str, value:int):
        return self.dialect.get(DIALECT_VOC_DOWN) % (prev_level, new_level, value)

