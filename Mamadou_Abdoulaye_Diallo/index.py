import random
class Personne:
    def __init__(self, nom, sante="saine", proba_infection=0.0):
        self.nom=nom
        self.sante=sante
        self.proba_infection=proba_infection
    def infecter(self):
        self.sante="infecter"
    def immuniser(self):
        self.sante="immunisee" 

    def change_sante(self, sante):
         self.sante=sante
    def __str__(self):
       return f"Bonjour monsieur {self.nom} vous êtes {self.sante}"     


     


class Population:
    def __init__(self, taille_population,proba_infection):
        self.taille_population=taille_population
        self.proba_infection=proba_infection
        self.indiv= [Personne(f'Individu_{i}', self.proba_infection) for i in range(self.taille_population)]
    def introduire_infection(self, nombre):
        personne_infectes = random.sample(self.indiv, nombre)
        for personne in personne_infectes:
            personne.infecter()
    def simuler_jour(self):
        for personne in self.indiv:
            if personne.sante == 'saine':
               personne.infecter()
            elif personne.sante == 'infectee':
                personne.sante='Saine'

    def __str__(self):
        nb_infectes = sum(1 for p in self.individus if p.sante=="infecter")
        saine = sum(1 for p in self.individus if p.sante=="saine")
        immunise = sum(1 for p in self.individus if p.sante=="immunise")

        return f'les personnes saines sont au nombre de {saine}, les affectée sont {nb_infectes}, et immunisées sont {immunise}'            
