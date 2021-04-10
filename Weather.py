import pygame

import random

import Plant
import Grass
import Cloud


SUMMER = 0
FALL = 1
WINTER = 2
SPRING = 3
NIGHT = 4
NB_ITERATION = 300
IT = 15


# class Time:

#     def __init__(self):

#         self.hour = 0

#         self.time = 0


#     def update_hour(self):

#         self.time += 1

#         if self.time > IT:

#             self.time = 0

#             self.hour += 1
            
#         if self.hour > 23:
            
#             self.hour = 0
                
            
#     def get_hour(self):

#         return self.hour


class Weather:

    def __init__(self):

        self.season = random.randint(0,3)

        #self.heure = Time()

        self.temperature = 0

        self.delay = 0


    def reset_season(self):

        self.season = 0
        

    def reset_time(self):
        
        self.delay = 0


    def update_season(self):

        self.delay += 1

        if self.delay >= NB_ITERATION:

           self.reset_time()
           
           self.season += 1

        if self.season > SPRING:

            self.reset_season()


    def update_temperature(self):

        # winter
        
        if self.season == WINTER:
            
            self.temperature = random.uniform(float(-10), float(-6))

            Plant.P_FIRE = 0

            Plant.P_REPOUSSE = (self.season+1) / 10**3

            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)

            Cloud.SPEED_FACTOR = random.randint(1,4)
            
            return

        # spring

        if self.season == SPRING:
            
            self.temperature = random.uniform(float(15), float(20))

            Plant.P_FIRE = self.temperature / 10**4

            Plant.P_REPOUSSE = (self.season+1) / 10**3

            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)

            Cloud.SPEED_FACTOR = random.randint(1,4)

            return

        # summer

        if self.season == SUMMER:
            
            self.temperature = random.uniform(float(30), float(35))

            Plant.P_FIRE = self.temperature / 10**4

            Plant.P_REPOUSSE= (self.season+1) / 10**3

            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)

            Cloud.SPEED_FACTOR = random.randint(1,4)
            
            return 

        # fall

        if self.season == FALL:
            
            self.temperature = random.uniform(float(13), float(16))

            Plant.P_FIRE = self.temperature / 10**4

            Plant.P_REPOUSSE = (self.season+1) / 10**3

            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)

            Cloud.SPEED_FACTOR = random.randint(1,4)



    def get_temperature(self):

        return self.temperature


    def get_season(self):

        # if self.heure.get_hour() < 6 or self.heure.get_hour() > 20:

        #     return NIGHT

        return self.season
        

    def update_weather(self):

        #self.heure.update_hour()
        if not self.delay:
            self.update_temperature()
        #if self.heure.get_hour() > 6 or self.heure.get_hour() < 20:
        self.update_season()
        





