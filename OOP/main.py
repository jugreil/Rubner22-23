class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, firma):
        super().__init__(name, gender)
        self.firma = firma


class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, gender, firma):
        super().__init__(name, gender, firma)


class Firma():
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def compare_men_women(self):
        count_women = 0
        count_men = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.gender == "women":
                    count_women += 1
                    continue
                count_men += 1
            for gruppenleiter in abteilung.gruppenleiter:
                if gruppenleiter.gender == "women":
                    count_women += 1
                    continue
                count_men += 1
        # return count men / women in %
        return {"men": count_men / (count_men + count_women), "women": count_women / (count_men + count_women)}

    def count_abteilungen(self):
        return len(self.abteilungen)

    def count_mitarbeiter(self):
        count = 0
        for abteilung in self.abteilungen:
            count += len(abteilung.mitarbeiter)
        return count

    def count_gruppenleiter(self):
        count = 0
        for abteilung in self.abteilungen:
            count+= len(abteilung.gruppenleiter)
        return count

    def get_biggest_abteilung(self):
        biggest_abteilung = self.abteilungen[0]
        for abteilung in self.abteilungen:
            if len(abteilung.mitarbeiter) > len(biggest_abteilung.mitarbeiter):
                biggest_abteilung = abteilung
        return biggest_abteilung

class Abteilung():
    def __init__(self, name, gruppenleiter):
        self.name = name
        self.gruppenleiter = []
        self.gruppenleiter.append(gruppenleiter)
        self.mitarbeiter = []


# main:

firma = Firma("HTL")
abteilung = Abteilung("Wirtschaftingeneurwesen", Gruppenleiter("AV", "men", firma))
firma.abteilungen.append(abteilung)
abteilung2 = Abteilung("Elektronik", Gruppenleiter("AV", "men", firma))
firma.abteilungen.append(abteilung2)

abteilung.mitarbeiter.append(Mitarbeiter("Simon", "men", firma))
abteilung.mitarbeiter.append(Mitarbeiter("Julius", "men", firma))
abteilung.mitarbeiter.append(Mitarbeiter("MariaDB", "women", firma))
abteilung.gruppenleiter.append(Gruppenleiter("AV2", "women", firma))

print(firma.get_biggest_abteilung().name)
print(firma.count_abteilungen())
print(firma.count_mitarbeiter())
print(firma.compare_men_women())
print(firma.count_gruppenleiter())
