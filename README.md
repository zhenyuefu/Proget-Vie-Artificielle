# **Présentation Partie Agent**

## Animation

Les proies et les prédateurs peuvent se déplacer dans 4 directions.

![wolf_animation](Rapport/wolf.gif)![sheep_animation](Rapport/sheep.gif)

L'animation dans chaque direction est composée de 3 images



## Manger

Un prédateur rencontre une proie et la mange. La proie mangera aussi l'herbe mature quand elle la rencontrera.

![](Rapport/mange1.gif)![](Rapport/mange2.gif)



## Rencontrer un obstacle

L'agent se dirige de manière aléatoire lorsqu'il rencontre un obstacle.

![](Rapport/trun.gif)

## La chasse et la fuite 

Les prédateurs vont trouver la proie la plus proche dans un certain rayon d'action. Les proies peuvent également trouver le prédateur le plus proche dans un certain rayon d'action.

![](Rapport/fuite.gif)

## Pause

L'agent s'arrête pour se reposer après une période de mouvement. Lorsqu'il a faim après n'avoir pas mangé pendant un certain temps, il recommence à se dépenser.

![](Rapport/pause.gif)

## Reproduction

L'agent a une chance de se reproduire en se déplaçant.

![](Rapport/reproduction.gif)



# **Présentation Partie Environnement**

## **Descritpif du Monde**

Le monde est composé :
- d'éléments adaptatifs (montagnes, lacs, rochers, troncs d'arbre)
- de la végétation (arbres, herbes)
- d'une météo(saison, vent, températures...)
- d'agents (proies/prédateurs)

### **Elements adaptatifs**

#### **Montagnes et Points d'eau**

Les montagnes et les points d'eau sont placées selon une carte d'altitude (max altitude : 500m) qui déterminera leurs emplacements (exemple : les points ayant une altitude supérieur à 495m signifie qu'il y a un sommet, donc une montagne ; les points ayant une altitude inférieur à 5m sont des creux, donc un lac).

>De plus, leurs apparences dépendent de la saison :

![Winter](PNG/Aperçu/M_winter.png)      ![Spring](PNG/Aperçu/M_spring.png)      ![Summer](PNG/Aperçu/M_summer.png)      ![Fall](PNG/Aperçu/M_fall.png)      

![Winter](PNG/Aperçu/L_winter.png)      ![Spring](PNG/Aperçu/L_spring.png)      ![Summer](PNG/Aperçu/L_summer.png)      ![Fall](PNG/Aperçu/L_fall.png)      

### **Rochers et Troncs d'arbre**

Les rochers et troncs sont répartis aléatoirement sur la map. Leur seul fonction est de jouer le rôle d'obstacle pour les agents.

>Leurs apparences changent aussi :

![Winter](PNG/split/ice_rock.png)      ![Spring](PNG/split/spring_rock.png)     ![Fall/Summer](PNG/split/fall_rock.png)      

![Winter](PNG/split/winter_tronc.png)      ![Spring](PNG/split/spring_tronc.png)        ![Fall/Summer](PNG/split/fall_tronc.png)      

### **Végétation**

#### **Arbres et Herbes**

Les plantes sont répartis aléatoirement sur la map. Ils évoluent en passant par différentes formes et ce jusqu'à atteindre leur maturité :

>Le temps d'évolution d'une plante dépend de la distance de l'eau à laquelle il se trouve ainsi que de la saison:

![](PNG/split/tree1.png) ![](PNG/split/tree2.png) ![](PNG/split/tree3.png) ![](PNG/split/tree4.png) ![](PNG/split/tree5.png)
![](PNG/split/tree6.png) ![](PNG/split/tree7.png) ![](PNG/split/tree8.png) ![](PNG/split/tree9.png) ![](PNG/split/tree10.png)
![](PNG/split/tree11.png) ![](PNG/split/tree12.png) ![](PNG/split/tree13.png) ![](PNG/split/tree14.png) ![](PNG/split/tree15.png)
![](PNG/split/tree16.png) ![](PNG/split/tree17.png)

![](PNG/split/grass1.png) ![](PNG/split/grass2.png) ![](PNG/split/grass3.png)

![](PNG/split/winter_grass1.png) ![](PNG/split/winter_grass2.png) ![](PNG/split/winter_grass3.png)

Ici on peut apercevoir que l'arbe se trouvant à proximité d'un point d'eau pousse beaucoup plus vite:

![Ev](PNG/Aperçu/pousse_arbre.png)

Une plante peut prendre feu à n'importe quel moment, cela dépend de la température et de la saison (pas de feu en Hiver), et le feu se propage selon la direction dans laquelle souffle le vent.

Voici les étapes du feu :

![Fire](PNG/split/fire4.png) ![Fire](PNG/split/fire5.png) ![Fire](PNG/split/fire6.png) ![Fire](PNG/split/fire7.png) ![Fire](PNG/split/fire8.png) ![Fire](PNG/split/cendre0.png) ![Fire](PNG/split/cendre1.png) ![Fire](PNG/split/cendre2.png)

Arbre en feu : 

![Fire](PNG/Aperçu/tree_inFire.png)

Propagation du feu avec un vent qui souffle au Nord-Est:

![Fire](PNG/Aperçu/grass_inFire.png)

## **Météo**

Le système cyclique comporte 4 saisons : Eté, Automne, Hiver et Printemps. A chaque saison est réatribué une température moyenne, le sens du vent (nuages), sa vitesse ainsi que la probabilité de mise à feu et de repousse pour la végétation.

![Winter](PNG/Aperçu/winter.png) ![Spring](PNG/Aperçu/spring.png) ![Spring](PNG/Aperçu/summer.png) ![Spring](PNG/Aperçu/fall.png)

Il y a deux forme de nuage :

![Winter](PNG/split/cloud.png) ![Winter](PNG/split/cloud2.png)