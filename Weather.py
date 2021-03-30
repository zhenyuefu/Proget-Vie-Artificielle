import pygame

import random


SUMMER = 0
FALL = 1
WINTER = 2
SPRING = 3
NIGHT = 4


class Time:

    def __init__(self):

        self.hour = 0

        self.time = 0


    def update_hour(self):

        self.time += 1

        if self.time > 50:

            self.time = 0

            self.hour += 1
            
        if self.hour > 23:
            
            self.hour = 0
                
            
    def get_hour(self):

        return self.hour


class Weather:

    def __init__(self):

        self.season = random.randint(0,3)

        self.heure = Time()

        self.temperature = 0

        self.delay = 0


    def reset_season(self):

        self.season = 0
        

    def reset_time(self):
        
        self.delay = 0


    def update_season(self):

        self.delay += 1

        if self.delay>= 2000:

           self.reset_time()
           
           self.season += 1

        if self.season > 3:

            self.reset_season()


    def update_temperature(self):

        # summer

        if self.season == SUMMER:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 22:
                
                self.temperature = random.uniform(float(27), float(30))

                return 

            self.temperature = random.uniform(float(24), float(27))

            return

        # fall

        if self.season == FALL:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 20:
                
                self.temperature = random.uniform(float(13), float(16))

                return

            self.temperature = random.uniform(float(8), float(11))

            return
        
        # winter
        
        if self.season == WINTER:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 20:
                
                self.temperature = random.uniform(float(-10), float(-6))

                return

            self.temperature = random.uniform(float(-15), float(-10))

            return

        # spring

        if self.season == SPRING:

            if self.heure.get_hour() > 6 and self.heure.get_hour() < 21:
                
                self.temperature = random.uniform(float(15), float(20))

                return

            self.temperature = random.uniform(float(10), float(13))

            return


    def get_temperature(self):

        return self.temperature


    def get_season(self):

        if self.heure.get_hour() < 6 or self.heure.get_hour() > 20:

            return NIGHT

        return self.season
        

    def update_weather(self):

        self.heure.update_hour()
        if self.heure.get_hour() > 6 or self.heure.get_hour() < 20:
            self.update_season()
        self.update_temperature()
        





