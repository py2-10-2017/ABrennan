"""
You're going to build a hospital with patients in it!

- Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.

- Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
"""

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
        print '\nPatient ID #', self.PAT_ID - 1
        for attr, val in sorted(self.__dict__.iteritems(), reverse=True):
            if attr == 'name':
                print "{}: {}".format(attr, val)
            elif attr == 'allergies':
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

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.totalCap = capacity
        self.patients = []

    def admit(self, patient):
        if self.capacity > 0:
            num = str(self.totalCap - self.capacity + 1)
            patient.bedNum(num)
            self.patients.append(patient)
            self.capacity -= 1
            print '{} was admitted at {}'.format(patient.name, self.name)
        else:
            print '{} was not admitted to {} - they\'re are no open beds'.format(patient.name, self.name)

    def discharge(self, patient):
        p = patient.name
        i = 0
        for patient in self.patients:
            if patient.name == p:
                patient.bedNum('none')
                self.patients.pop(i)
                self.capacity += 1
                print '{} was discharged from {}'.format(patient.name, self.name)
            else:
                print '{} cannot be discharged from {} - they\'re not a current patient'.format(p, self.name)
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
