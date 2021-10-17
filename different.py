class ITMan:

    ITMen_counter = 0
    deleted_people = 0

    def __init__(self, language, salary):
        self.language = language
        self.salary = salary
        ITMan.ITMen_counter +=1

    def salary_increase(self, addon):
        self.salary += addon

    def workers_counter(self):
        print('Current IT people qty is {0}'.format(ITMan.ITMen_counter))

    def __del__(self):
        ITMan.ITMen_counter -= 1
        ITMan.deleted_people +=1


Buba = ITMan('Python', 1500)
Antoha = ITMan('C++', 6000)
Leha = ITMan('C++', 4500)

del Buba

print(Antoha.deleted_people)