from random import *
import pygame                   # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

class Agent(object):

    def __init__(self, x, y, predator_or_prey, world):

        self.x, self.y = x, y
        self.world = world
        self.predator_or_prey = predator_or_prey
        self.orient = 0
        self.it_non_mange = 0
        self.predator, self.prey = False, False
        self.alive = True
        self.dir = -1

        if predator_or_prey :

            self.predator = True

            self.p_reproduce = 0.03

            self.delai_famine = 14

        else :

            self.prey = True

            self.p_reproduce = 0.07

            self.delai_famine = 16


    def setDirection(self,d):

        if self.dir == -1 :

            self.dir = d

        if random() < 0.5 :

            self.dir = d


    def reset_mange(self):

        self.it_non_mange = 0
        

    def reproduce(self):

        if random() < self.p_reproduce :

            world.reproduce(Agent(self.x,self.y,self.predator_or_prey,self.world))



    def step(self):

        self.it_non_mange += 1

        if self.it_non_mange > self.delai_famine :

            self.alive = False

        self.reproduce()

        if random() < 0.5 :

            self.orient = (self.orient - 1) % 4

        else:

            self.orient = (self.orient - 1 + 4) % 4

        if dir != -1 :

            self.orient = self.dir

        self.dir = -1


        if self.orient == 0 :

            self.y = (self.y - 1 + world.size_factor_X) % world.size_factor_X

            if self.y < 0 :

                self.y += world.size_factor_Y

            if self.y >= world.size_factor_Y :

                self.y -= world.size_factor_Y

            return
        
        if self.orient == 1 :

            self.x = (self.x + 1 + world.size_factor_X) % world.size_factor_X

            if self.x < 0 :

                self.x += world.size_factor_X

            if self.x >= world.size_factor_X :

                self.x -= world.size_factor_X

            return

        if self.orient == 2 :

            self.y = (self.y + 1 + world.size_factor_Y) % world.size_factor_Y

            if self.y < 0 :

                self.y += world.size_factor_Y

            if self.y >= world.size_factor_Y :

                self.y -= world.size_factor_Y

            return

        if self.orient == 3 :

            self.x = (self.x - 1 + world.size_factor_X) % world.size_factor_X

            if self.x < 0 :

                self.x += world.size_factor_X

            if self.x >= world.size_factor_X :

                self.x -= world.size_factor_X

class World:
    """
    classe principale du jeux
    """

    def __init__(self, size_factor_X=50, size_factor_Y=37, size_tile_X=32, size_tile_Y=32):
        """
        constructeur de la classe
        size_factor_X et size_factor_Y représentent la taille du plateau de jeux en nombre de tuiles 64*64 pixels
        """



        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y

        self.size_tile_X, self.size_tile_Y = size_tile_X, size_tile_Y

        self.Grass=[x[:] for x in [[0] * self.size_factor_X] * self.size_factor_Y]

        self.p_grass = 0.09

        # Initialisation proies - predateurs

        self.Prey=[]

        self.Predator=[]

        for agent in range(20):

            self.Prey.append(Agent(randint(0,self.size_factor_X),randint(0,self.size_factor_Y),False,self))

            self.Predator.append(Agent(randint(0,self.size_factor_X),randint(0,self.size_factor_Y),True,self))

        pygame.init()          
                                                     
        self.screen = pygame.display.set_mode((int(self.size_tile_X*self.size_factor_X), int(self.size_tile_Y*self.size_factor_Y)),DOUBLEBUF)

        pygame.display.set_caption("WORLD TEST")  


    def loadImage(self,filename):
        
        image = pygame.image.load(filename).convert_alpha()
        
        image = pygame.transform.scale(image, (int(self.size_tile_X), int(self.size_tile_Y)))
        
        return image 

    def stepAgent(self):

        for prey in self.Prey :

            prey.step()

        for pred in self.Predator :

            pred.step()


    def stepWorld(self):

        for i in range(len(self.Predator)):

            pred = self.Predator[i]

            if not pred.alive :

                del self.Predator[i]

                continue

            for j in range(len(self.Prey)):

                prey = self.Prey[j]

                if not prey.alive :

                    del self.Prey[j] 

                    continue

                if self.Grass[prey.y][prey.x] == 1:

                    self.Prey[j].reset_mange()

                    self.Grass[prey.y][prey.x] = 0

                if pred.y == prey.y and pred.x == prey.x :

                    del self.Prey[j]
                    
                    self.Predator[i].reset_mange()

                    continue

                if pred.x == prey.x:

                    if pred.y == prey.y + 1:

                        self.Predator[i].setDirection(0)
                        self.Prey[j].setDirection(0)
                        continue

                    if pred.y == prey.y - 1:

                        self.Predator[i].setDirection(2)
                        self.Prey[j].setDirection(2)
                        continue

                if pred.y == prey.y:

                    if pred.x == prey.x + 1:

                        self.Predator[i].setDirection(3)
                        self.Prey[j].setDirection(3)
                        continue

                    if pred.x == prey.x - 1:

                        self.Predator[i].setDirection(1)
                        self.Prey[j].setDirection(1)

        self.repousse_grass()
                       

    def repousse_grass(self):

        for x in range(len(self.Grass[0])):

            for y in range(len(self.Grass)):

                if self.Grass[y][x] == 0 and random() <= self.p_grass:
                    
                    self.Grass[y][x] = 1

    
    def reproduce(self, agent):

        if agent.predator :

            self.Predator.append(agent)

        else :

            self.Prey.append(agent)


    def step(self):
        """
        boucle de lecture infinie événementielles du jeux

        """

        while len(self.Predator) != 0 or len(self.Prey) != 0:

            self.stepWorld()

            self.stepAgent()

            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe           

            # update de l'environnement : 

            for x in range(self.size_factor_Y):

                for y in range(self.size_factor_X):
                    
                    self.screen.blit(self.loadImage('dirt.png'),(x*self.size_tile_X,y*self.size_tile_Y))
            
            for prey in self.Prey :

                self.screen.blit(self.loadImage('PNG/prey.png'),(prey.x*self.size_tile_X,prey.y*self.size_tile_Y))

            for pred in self.Predator :

                self.screen.blit(self.loadImage('PNG/predator.png'),(pred.x*self.size_tile_X,pred.y*self.size_tile_Y))

            pygame.display.update()


    def destroy(self):
        """
        destructeur de la classe
        """
        print('Exit')
        pygame.quit() # ferme la fenêtre principale
        exit()        # termine tous les process en cours

if __name__ == '__main__':
    world=World()
    try:
        world.step()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
        world.destroy()




