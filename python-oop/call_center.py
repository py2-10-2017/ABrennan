"""
You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
"""
from datetime import datetime, timedelta

if __name__ != "__main__": #changing so that class is only available if module is imported
    class Call(object):
        def __init__(self, id, name, number, reason):
            self.id = id
            self.name = name
            self.number = number
            self.reason = reason
            #gives the current time plus 'id' minutes for testing time
            self.time = (datetime.now() + timedelta(minutes=id)).strftime('%m-%d-%Y %H:%M:%S')

        def display(self):
            return "---- Call #{} Details ----\nCaller: {} from {}\nCall Time: {} \nReason: {}\n".format(self.id,self.name,self.number,self.time,self.reason)

        def __repr__(self):
            return "Call came in from {}".format(self.name)

    class CallCenter(object):
        def __init__(self):
            self.calls = []
            self.size = 0

        def add(self, call):
            self.calls.append(call)
            self.size += 1
            return self

        def remove(self):
            self.calls.pop(0)
            self.size -= 1
            return self

        def removePhone(self, phone):
            c = phone
            i = 0
            for call in self.calls:
                if call.number == c:
                    self.calls.pop(i)
                i += 1
            self.size -= 1
            return self

        def info(self):
            print 'The queue has {} calls\n'.format(self.size)

            if self.calls:
                i = 1
                for call in sorted(self.calls):
                    print call.display()
                    i += 1
            else:
                print 'There are no calls in the queue\n\n'
            return self

        def __repr__(self):
            return 'at the call center'

"""
#creating an instance of the class
call1 = Call(1,"Bambino","720-555-5555","I poured milk all over the floor")
call2 = Call(2,"Tyke","303-555-5555","I lost my fidget spinner")
call3 = Call(3,"Baby","615-555-5555","I broke my toy")
call4 = Call(4,"Toddler","720-555-5555","I want to watch tv")
call5 = Call(5,"Kid","919-555-5555","I don't want to go bed")
call6 = Call(6,"Munchkin","695-555-5555","I can't find my shoes")

#creating instance of call list
callList = CallCenter()

#no calls added to list
callList.info()

#adds 6 calls to the queue and prints list
callList.add(call1).add(call2).add(call3).add(call4).add(call5).add(call6).info()

#removes first call and prints list
callList.remove().info()

#remove call if phone number matches list
callList.removePhone("919-555-5555").info()
"""
