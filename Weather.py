import pygame

import random

class Time:

    def __init__(self):

        self.hour = 0

        self.time = 0

    def update_hour(self):

        self.time += 1

        if self.time > 3:

            self.time = 0

            self.hour += 1
            
            if self.hour > 23:
                
                self.hour = 0
                
            print(self.hour)



    def get_hour(self):

        return self.hour




class Weather:

    def __init__(self):

        self.season = 0

        self.heure = Time()

        self.temperature = 0

        self.delay = 0


    def reset_season(self):

        self.season = 0

    def reset_time(self):
        
        self.time = 0


    def update_season(self):

        self.time += 1

        if self.time >= 50:

           self.reset_time()
           
           self.season += 1

        if self.season > 3:

            self.reset_season()


    def update_temperature(self):

        # summer

        if self.season == 0:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 22:
                
                self.temperature = random.uniform(float(27), float(30))

                return 

            self.temperature = random.uniform(float(24), float(27))

            return

        # fall

        if self.season == 1:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 20:
                
                self.temperature = random.uniform(float(13), float(16))

                return

            self.temperature = random.uniform(float(8), float(11))

            return
        
        # winter
        
        if self.season == 2:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 20:
                
                self.temperature = random.uniform(float(-10), float(-6))

                return

            self.temperature = random.uniform(float(-15), float(-10))

            return

        # spring

        if self.season == 3:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 21:
                
                self.temperature = random.uniform(float(15), float(20))

                return

            self.temperature = random.uniform(float(10), float(13))

            return


    def get_temperature(self):

        return self.temperature


    def get_season(self):

        return self.season
        

    def update_weather(self):

        self.update_season()
        self.update_temperature()
        self.heure.update_hour()





