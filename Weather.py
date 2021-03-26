

import random


class Weather:

    def __init__(self):

        self.season = 0

        self.temperature = 0

        self.time = 0


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

            self.temperature = random.uniform(float(25), float(30))

            return

        # fall

        if self.season == 1:

            self.temperature = random.uniform(float(10), float(15))

            return
        
        # winter
        
        if self.season == 2:

            self.temperature = random.uniform(float(-10), float(-5))

            return

        # spring

        if self.season == 3:

            self.temperature = random.uniform(float(15), float(20))

            return
