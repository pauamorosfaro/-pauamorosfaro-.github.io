import random	#Importar random, que inclou funcions per generar nombres aleatoris.
import matplotlib.pyplot as plt	#S’importa una altra llibreria, que dona la possibilitat de crear gràfics.

DEMANAR_UNA_CARTA_MÉS = 1	#Es genera una constant amb valor 1 per a utilitzar-la més endavant.
QUEDAR_IGUAL = 0	#Es genera una constant amb valor 0 per a utilitzar-la més endavant.


class BlackJack: 
   cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  #Aquesta classe representa una partida de Blackjack. La classe té un únic atribut, "cartes", que és una llista que conté els valors de les cartes en el joc (és a dir, els números de l'1 al 10, així com quatre 10). Aquesta llista s'utilitzarà més tard en el codi per a simular les targetes de dibuix.

   def __init__(self, jugador_sum, crupier_visible, as_11):
       self.jugador_sum = jugador_sum 	#Suma de les cartes del jugador.
       self.crupier_visible = crupier_visible 		#Valor de la carta del crupier.
       self.as_11 = as_11	#Diu si es té un as que pugui contar també com a 11 o no.

   def treu_Carta(self):
       return random.choice(self.cartes) 	#Se simula el fet de treure una carta de la llista cartes (creada anteriorment).

   def crupier_torn(self): 	#Representa el torn del crupier a una partida de blackjack. 
       crupier_sum = self.crupier_visible  	#primer s’inicialitza la suma actual del crupier amb el valor de la carta visible per al jugador. Si aquesta carta és un as amb valor 1, es compta com 11 (com faria el crupier en una partida real de blackjack), en cas contrari, es compta com el seu valor nominal.
       if crupier_sum == 1:
           crupier_as = True
           crupier_sum = 11
       else:
           crupier_sum = False

       while crupier_sum < 17: 
           nova_carta = self.treu_Carta()
           crupier_sum = crupier_sum + nova_carta
           if crupier_sum > 21 and crupier_sum == True:
               crupier_sum = crupier_sum - 10
               crupier_sum = False
           elif nova_carta == 1 and crupier_sum + 10 < 22:
               crupier_sum = crupier_sum + 10
               crupier_sum = True 	#Llavors, el crupier comença a treure cartes fins que la seva suma sigui almenys 17. Cada carta s'extreu de la baralla utilitzant el mètode “treu_Carta” definit anteriorment. Si la suma del distribuïdor supera els 21, i tenen almenys un as comptat com a 11, un dels asos es canvia a un valor d'1 per evitar passar-se. Això es fa restant 10 de la suma. Si no hi ha asos comptats com a 11, el mètode simplement retorna l'estat actual del joc (incloent la suma del distribuïdor, la suma del jugador, i l'estat de l'as comptat com a 11).

       if crupier_sum > 21:
           return [self.jugador_sum, self.crupier_visible, self.as_11, 1, True]
       if crupier_sum > self.jugador_sum:
           return [self.jugador_sum, self.crupier_visible, self.as_11, -1, True]
       if self.jugador_sum > crupier_sum :
           return [self.jugador_sum, self.crupier_visible, self.as_11, 1, True]
       if self.jugador_sum == crupier_sum :
           return [self.jugador_sum, self.crupier_visible, self.as_11, 0, True]

   def torn(self, acció):
       if acció == QUEDAR_IGUAL:
           return self.crupier_torn()
       else:
           nova_carta = self.treu_Carta()
           self.jugador_sum = self.jugador_sum + nova_carta

           if self.jugador_sum > 21 and self.as_11 == True:
               self.jugador_sum = self.jugador_sum - 10
               self.as_11 = False

           elif nova_carta == 1 and self.jugador_sum + 10 < 22:
               self.jugador_sum = self.jugador_sum + 10
               self.as_11 = True

           if self.jugador_sum > 21:
               return [self.jugador_sum, self.crupier_visible, self.as_11, -1, True]
           else:
               return [self.jugador_sum, self.crupier_visible, self.as_11, 0, False]	#Finalment, el mètode retorna el resultat del torn del distribuïdor en funció de la suma final. Si la suma del repartidor supera els 21, el jugador guanya. Si la suma del distribuïdor és més gran que la del jugador, el jugador perd. Si la suma del jugador és més gran que la del repartidor, el jugador guanya. Si el jugador i el distribuïdor tenen la mateixa suma, és taules. El mètode retorna una llista de valors, incloent-hi l'estat actual del joc i una bandera que indica si el joc s'ha acabat o no.


class Estat: 	#Classe explicada amb profunditat al treball.

   def __init__(self, jugador_sum, crupier_visible, as_11): 	#Tres atributs explicats anteriorment. El mètode "init" s'encarrega d'inicialitzar totes les variables, assignant als comptadors una freqüència inicial d'1 i a les recompenses totals el valor de la recompensa passada com a paràmetre.
       self.jugador_sum = jugador_sum 
       self.crupier_visible = crupier_visible
       self.as_11 = as_11
       self.n_DEMANAR_UNA_CARTA_MÉS = 1
       self.n_QUEDAR_IGUAL = 1
       self.Q_DEMANAR_UNA_CARTA_MÉS_total = 0
       self.Q_QUEDAR_IGUAL_total = 0
       self.policy = QUEDAR_IGUAL

   def actualitza(self, recompensa, acció):  	#El mètode "actualitza" pren dos arguments: «recompensa» i «acció». «Recompensa» és un número que representa la recompensa rebuda després de realitzar una acció en un estat. «acció» és una variable que indica l'acció que es va prendre en aquest estat («DEMANAR_UNA_CARTA_MÉS» o «QUEDAR_IGUAL»).

       if acció == QUEDAR_IGUAL: 
           self.n_QUEDAR_IGUAL = self.n_QUEDAR_IGUAL + 1
           self.Q_QUEDAR_IGUAL_total = self.Q_QUEDAR_IGUAL_total + recompensa
       else:
           self.n_DEMANAR_UNA_CARTA_MÉS = self.n_DEMANAR_UNA_CARTA_MÉS + 1
           self.Q_DEMANAR_UNA_CARTA_MÉS_total = self.Q_DEMANAR_UNA_CARTA_MÉS_total + recompensa
#S’actualitzen valors amb els nous valors de la recompensa i el nombre de vegades que s’ha pres una acció determinada.

       if self.Q_DEMANAR_UNA_CARTA_MÉS_total / float(self.n_DEMANAR_UNA_CARTA_MÉS) > self.Q_QUEDAR_IGUAL_total / float(self.n_stick):
           self.policy = DEMANAR_UNA_CARTA_MÉS
       else:
           self.policy = QUEDAR_IGUAL 
#Finalment, s'actualitza el valor de «policy» segons la regla del "epsilon-greedy". Es compara la recompensa mitjana de prendre una carta addicional amb la recompensa mitjana de quedar-se igual. Si la recompensa mitjana de prendre una carta addicional és major, llavors la política s'actualitza a «DEMANAR_UNA_CARTA_MÉS», en cas contrari, la política s'actualitza a «QUEDAR_IGUAL».

def getEstatIdx(jugador_sum, crupier_visible, as_11):
   return ((jugador_sum - 11) * 10 + crupier_visible) * 2 - as_11- 1

#Aquesta funció llavors calcula un índex que representa l'estat del joc utilitzant la fórmula: ((jugador +sum - 11) * 10 + crupier_visible) * 2 - as-11- 1
Això significa el següent: 
(jugador_sum - 11): Aquesta part resta 11 de la suma del jugador per a fer l'interval de valors de 0 a 9 en lloc d'11 a 20.
* 10: Multiplica el resultat anterior per 10 per a obtenir valors de 0 a 90 en lloc de 0 a 9.

+ crupier_visible: afegeix el valor de la targeta visible del distribuïdor al resultat anterior.

* 2: Multiplica el resultat anterior per 2 per a aconseguir valors de 0 a 180 en lloc de 0 a 90.

- as_11 - 1: resta el valor de as.11 i 1 del resultat anterior. Aquesta part de la fórmula s'utilitza per diferenciar entre els dos valors possibles d'as (011 (0 o 1).
El resultat final de la fórmula és l'índex que representa l'estat actual del joc. Aquest índex s'emprarà per accedir a l'element corresponent en una matriu que conté informació sobre l'estat.



def monteCarloES(nombre_episodis=7500000): 	#Explicat amb detall al treball. Aquesta funció implementa l'algorisme Monte Carlo Exploring Starts per aprendre la política òptima per jugar blackjack. La funció pren també  un argument nombre_episodis, que especifica el nombre d'episodis (jocs) a simular. El valor per defecte és 7,500,000.

   states = [Estat(i, j, l) for i in range(11, 22) for j in range(1, 11) for l in reversed(range(2))]		#Primer, la funció crea una llista d'estats que contenen tots els estats possibles del joc. Cada estat està representat per un objecte Estat, que emmagatzema la suma del jugador, la carta visible del crupier, i si el jugador té, un as que es pot comptar com 11.

   for i in range(0, nombre_episodis): 	#A continuació, la funció entra en bucle la quantitat de vegades determinada per “nombre_episodis”. Per a cada episodi, se selecciona un estat inicial aleatori “s” de la llista d'estats. Una instància de la classe BlackJack es crea amb l'estat inicial, i la primera acció d'”Acció” s'escull aleatòriament (0 o 1. Determinats anteriorment).

       s = random.choice(states)
       episodi = []
       bj = BlackJack(s.jugador_sum, s.crupier_visible, s.as_11)
       acció= random.randint(0, 1)
       episodi.append([s, acció])
#La funció llavors simula el joc emprant repetidament el mètode “torn()” de la instància BlackJack fins que el joc finalitza. Cada vegada, l'estat actual “s” s'actualitza en funció de la suma del jugador, la cara visible del crupier, i si el jugador té un as que es pot comptar com 11. L'acció òptima per al nou estat es tria basant-se en l'atribut de política de l'objecte Estat. L'estat actual i l'acció escollida s'afegeixen a la llista d'episodis.

       while True:
           jugador_sum, crupier_visible, as_11, recompensa, joc_acaba = bj.torn(acció)
           if joc_acaba == False:
               s = states[getEstatIdx(jugador_sum, crupier_visible, as_11)]
               acció= s.policy
               episodi.append([s, acció])
           else:
               for e in episodi:
                   e[0].actualitza(recompensa, e[1])
               break
   return states
#Una vegada que el joc acaba, la funció es repeteix sobre la llista d'episodis i actualitza els valors Q de cada parell d'acció i estat utilitzant el mètode “actualitza()” de l'objecte “Estat”. Finalment, després que tots els episodis s'hagin simulat, la funció retorna la llista d'estats, que ara conté la política òptima apresa per jugar a blackjack.


def determina_estratègia(states):  #Agafa la llista d’estats com a “input” i crea dos diccionaris.
   nodemanar_amb_as = dict()	#1r diccionari.
   demanar_amb_as = dict()	#2n diccionari.
   for s in states:
       if s.policy == DEMANAR_UNA_CARTA_MÉS and s.as_11 == False:	#El jugador no demana una carta més.
           if s.crupier_visible in nodemanar_amb_as:
               nodemanar_amb_as[s.crupier_visible] = max(nodemanar_amb_as[s.crupier_visible], s.jugador_sum)
           else:
               nodemanar_amb_as[s.crupier_visible] = s.jugador_sum
       elif s.policy == DEMANAR_UNA_CARTA_MÉS and s.as_11 == True: 3	#El jugador demana una carta més.
           if s.crupier_visible in demanar_amb_as:
               demanar_amb_as[s.crupier_visible] = max(demanar_amb_as[s.crupier_visible], s.jugador_sum)
           else:
               demanar_amb_as[s.crupier_visible] = s.jugador_sum

#Els diccionaris s'utilitzen per determinar l'estratègia a seguir en el joc. Si la suma actual del jugador està per sota del valor corresponent en el diccionari per a la carta visible actual, el jugador hauria de demanar una altra carta. En cas contrari, el jugador s'hauria de quedar.

   xrange = range	#Necessari en la versió de Python que s’ha utilitzat.

   lists = sorted(nodemanar_amb_as.items()) 
   x, y = zip(*lists)

#Defineix les llistes de variables com una llista ordenada d'elements del diccionari nodemanar_amb_as. Cada element de la llista és una tupla que conté un parell clau-valor del diccionari. La funció zip s'utilitza per a separar les claus i els valors de cada tupla a la llista de llistes i assignar-los a variables separades x i y. Això crea dues llistes, x i y, on x conté les claus del diccionari nodemanar.amb.as i y conté els valors corresponents. En resum, aquest bloc de codi està preparant les dades del diccionari nodemanar.amb.as per a la visualització o anàlisi posterior. Ordena els elements del diccionari per clau i crea dues llistes, x i y, per mantenir les claus i valors ordenats, respectivament.


   plt.figure(figsize=(12, 6)) 		#Mesura del gràfic
   plt.subplot(1, 2, 1)		#Aquest codi utilitza la biblioteca Matplotlib per a crear una visualització. Crea un subplot amb 1 fila, 2 columnes, i selecciona la primera columna per a dibuixar les dades.
   plt.torn(x, y, where='mid') 	#Les dades es proporcionen com dues llistes de valors x i y, que es comprimeixen junts utilitzant la funció zip. Aquestes llistes representen els punts que es dibuixaran al gràfic. La funció plt.plot() es crida per a dibuixar les dades com una funció de pas, on el paràmetre WHERE s'estableix a «mitjà» per a dibuixar els passos al punt mig entre cada valor x.
   axes = plt.gca()
   axes.set_ylim([10, 22])
   axes.yaxis.set_ticks(xrange(10, 23, 1))
   axes.xaxis.set_ticks(xrange(1, 10, 1))
   plt.xlabel("Carta visible crupier")
   plt.ylabel("Conjunt jugador")
   plt.title("L'as té valor 1", fontsize=14)
   plt.text(0.5, 0.8, "Quedar-se igual", fontsize=10, horizontalalignment="center", transform=axes.transAxes)
   plt.text(0.8, 0.2, "Demanar una carta més", fontsize=10, horizontalalignment="center", transform=axes.transAxes)

#En conclusió, aquest codi està traçant un gràfic que mostra l'estratègia òptima per a un jugador en un joc de blackjack, on el jugador pot optar per quedar-se o colpejar en funció de la seva mà actual i la carta visible del distribuïdor. El gràfic mostra el valor de la mà del jugador en l'eix Y, la targeta visible del distribuïdor en l'eix X, i l'acció òptima a prendre (posar-se o prémer) s'indica per la funció de pas.

   lists = sorted(hit_ace.items()) 	#La funció “sorted” s'utilitza per a ordenar el diccionari de hit.ace, que conté els parells de la targeta visible del distribuïdor i la suma màxima que el jugador hauria d'obtenir si decideix prémer (demana una altra carta) en lloc de posar-se dret.
   x, y = zip(*lists) 	#Aquest codi crea un gràfic utilitzant Matplotlib per mostrar l'estratègia recomanada per a un jugador de Blackjack quan té un as a la mà amb un valor d'11.
   plt.subplot(1, 2, 2)
   plt.torn(x, y, where='mid')
   axes = plt.gca()
   axes.set_ylim([10, 22])
   axes.yaxis.set_ticks(xrange(10, 23, 1))
   axes.xaxis.set_ticks(xrange(1, 10, 1))
   plt.xlabel("Carta visible crupier") 	#Títol eix x.
   plt.ylabel("Conjunt jugador")	#Títol eix y.

   plt.title("L'as té valor 11", fontsize=14) 		#Títol general i tamany que tindrà.
   plt.text(0.5, 0.8, "Quedar-se igual", fontsize=10, horizontalalignment="center", 	transform=axes.transAxes)		#Configuració de l’aspecte.
   plt.text(0.5, 0.2, "Demanar una carta més", fontsize=10, horizontalalignment="center", transform=axes.transAxes)
   plt.show()		#Es representa el gràfic.


if __name__ == "__main__":
   states = monteCarloES()
   determina_estratègia(states)

#Aquesta part del codi s'utilitza per executar l'algorisme de Monte Carlo per simular el joc de Blackjack i determinar l'estratègia òptima per al jugador. La funció monteCarloES() executa l'algorisme de Monte Carlo per generar un conjunt d'estats del joc i els seus corresponents retorns esperats. La funció “determina_estratègia(estats)” pren aquest conjunt d'estats de joc i els seus retorns esperats com a entrada i determina l'estratègia òptima per al jugador en cada estat de joc possible. El bloc if .name = == "_main_": és un llenguatge Python comú que permet que el codi que conté només s'executi quan el fitxer s'executa com un programa independent, en lloc de quan s'importa com un mòdul en un altre programa.
