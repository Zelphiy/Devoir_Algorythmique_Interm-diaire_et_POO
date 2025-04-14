class Patient:
    def __init__(self, nom, age, urgence):
        self.nom = nom
        self.age = age
        self.urgence = urgence
        
    def __str__(self):
        return f"{self.nom} (âge: {self.age}, urgence: {self.urgence})"

class Medecin:
    def __init__(self, nom):
        self.nom = nom
        
    def peut_vacciner(self, patient: Patient) -> bool:
        # De base le booléen renvoit True
        return True
    
    def vacciner(self, patient: Patient):
        # Phrase pour dire que le Medecin vaccine le patient
        print(f"{self.nom} vaccine {patient.nom}")
    
class MedecinGeneraliste(Medecin):
    def __init__(self, nom):
        super().__init__(nom)
        
    # Peut vacciner les patients de plus de 12 ans 
    def peut_vacciner(self, patient):
        return patient.age > 12
    
class Pediatre(Medecin):
    def __init__(self, nom):
        super().__init__(nom)
        
    # Peut vacciner les patients de plus de 0 à 12 ans
    def peut_vacciner(self, patient):
        return 0 <= patient.age <= 12
    
class Urgentiste(Medecin):
    def __init__(self, nom):
        super().__init__(nom)
        
    # Peut vacciner les patients dont l'urgence est égale à True
    def peut_vacciner(self, patient):
        return patient.urgence == True
    


class CentreVaccination:
    
    def __init__(self):
        self.file_patient = [] # Liste FIFO
        self.medecin_libre = [] # Liste des medecins libres
    
    def ajouter_patient(self, patient: Patient):
        # Ajoute un patient à la file 
        self.file_patient.append(patient)
        
    def prioriser_patient(self, patient : Patient):
        # Si l'age du patient est supérieur ou égale à 75 alors le patient est mis en tête de file
        if patient.age >= 75:
            self.file_patient.insert(0, patient)
        else:
            self.ajouter_patient(patient)
        
    def taille_file(self):
        # Affiche la taille de la file de patient
        return len(self.file_patient)
        
    def afficher_file(self):
        # Affiche la file complète avec les noms prénoms et age des patients
        print("Patient dans la file :")
        for patient in self.file_patient:
            print(f"- {patient}")
    
    def ajouter_medecin(self, medecin: Medecin):
        # Ajoute un medecin à la liste
        self.medecin_libre.append(medecin)
    
    def traiter(self):
        # Pour chaque patient dans la file, cherche un medecin qui peut le vacciner, sinon envoyer " Aucun medecin disponible pour {patient.nom}"
        while self.file_patient:
            patient = self.file_patient.pop(0)
            trouve = False
            for medecin in self.medecin_libre:
                if medecin.peut_vacciner(patient):
                    medecin.vacciner(patient)
                    trouve = True
                    break
            if not trouve:
                print(f"Aucun médecin disponible pour {patient.nom}")



centre = CentreVaccination()

# # Ajout des médecins
centre.ajouter_medecin(MedecinGeneraliste("Dr Martin"))
centre.ajouter_medecin(Pediatre("Dr Petit"))
centre.ajouter_medecin(Urgentiste("Dr Secours"))

# # Ajout de patients
centre.ajouter_patient(Patient("Alice", 30, False))
centre.ajouter_patient(Patient("Bob", 6, False))
centre.ajouter_patient(Patient("Charlie", 50, True))
centre.ajouter_patient(Patient("Daisy", 10, True))
centre.ajouter_patient(Patient("Eliot", 15, False))

# # Traitement de la file
centre.traiter()