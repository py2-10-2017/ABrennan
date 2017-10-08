"""
You're going to build a hospital with patients in it!

- Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.

- Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
"""

if __name__ != "__main__": #changing so that class is only available if module is imported
    class Patient(object):
        PAT_ID = 1

        def __init__ (self, name, allergies):
            self.name = name
            self.allergies = allergies
            self.bed_num = 'none'
            self.id = Patient.PAT_ID

            Patient.PAT_ID += 1

        def bedNum(self, num):
            self.bed_num = num

        def displayPat(self):
            for attr, val in sorted(self.__dict__.iteritems(), reverse=True):
                if attr == 'allergies':
                    out = 'allergies: '
                    i = 0
                    for allergy in self.allergies:
                        if i == len(self.allergies) - 1:
                            out += '{}'.format(allergy)
                        else:
                            out += '{}, '.format(allergy)
                            i += 1
                    print out
                elif attr == 'bed_num':
                    print "bed number: {}".format(val)
                else:
                    print "{}: {}".format(attr, val)
            print '\n'

        def __repr__(self):
            return "A chart has been added for patient {}".format(self.name)

    class Hospital(object):
        def __init__(self, name, capacity):
            self.name = name
            self.capacity = capacity
            self.totalCap = capacity
            self.patients = []
            self.beds = self.init_beds()

        def init_beds(self):
            beds = []
            for i in range(0, self.totalCap):
                beds.append({
                    'bed_id': i,
                    'open': True
                })
            return beds

        def admit(self, patient):
            if self.capacity > 0:
                self.patients.append(patient)
                for i in range(0, len(self.beds)):
                    if self.beds[i]["open"]:
                        num = self.beds[i]['bed_id'] + 1
                        self.beds[i]['open'] = False
                        patient.bedNum(num)
                        break
                self.capacity -= 1
                print '{} was admitted at {}'.format(patient.name, self.name)
            else:
                print '{} was not admitted to {} - there are no open beds'.format(patient.name, self.name)

        def discharge(self, patient):
            p = patient.name
            i = 0
            for patient in self.patients:
                if patient.name == p:
                    for bed in self.beds:
                        if bed["bed_id"] == patient.bed_num:
                            bed["Available"] = True
                            patient.bedNum('none')
                            break
                    self.patients.pop(i)
                    self.capacity += 1
                    print '{} was discharged from {}'.format(patient.name, self.name)
                else:
                    print '{} cannot be discharged from {} - they are not a current patient'.format(p, self.name)
                i += 1

        def displayHos(self):
            print '\n\n', ('#' * 20), self.name, ('#' * 20)
            print 'total capacity:', self.totalCap
            for attr, val in sorted(self.__dict__.iteritems()):
                if attr == 'patients':
                    if self.patients:
                        i = 0
                        print '\n', ('_' * 20), 'Patients', ('_' * 20)
                        for patient in self.patients:
                            patient.displayPat()
                    else:
                        print 'patients: no patients'
                elif attr == 'capacity':
                    attr = 'open beds'
                    print '{}: {}'.format(attr, val)

        def __repr__(self):
            return "{} has {} beds at their hospital".format(self.name, self.capacity)

"""
#creating instances of the patient
patient1 = Patient("John McDonald",['none'])
patient2 = Patient("Deirdre Lewis",['nuts'])
patient3 = Patient("Lisa Short",['none'])
patient4 = Patient("Alan Clarkson",['latex'])
patient5 = Patient("Owen Hart",['wheat', 'corn', 'oats'])

#creating instances of hospitals
hospital1 = Hospital("Regional Center", 2)
hospital2 = Hospital("Medical Center", 6)

hospital1.admit(patient1)
hospital1.admit(patient4)
hospital1.admit(patient3)
hospital2.admit(patient2)
hospital2.admit(patient5)
hospital2.discharge(patient2)
hospital2.discharge(patient2)

hospital2.displayHos()
hospital1.displayHos()
"""
