class Underscore(object):
    def map(self, val, context):
        out = map(context, val)
        return out

    def reduce(self, val, context):
        out = reduce(context, val)
        return out

    def find(self, val, context):
        if isinstance(val, list):
            out = filter(lambda x: x % 2 == 0, val)
            out = out[0]
        else:
            out = val.find(context)
        return out

    def filter(self, val, context):
        out = filter(context, val)
        return out

    def reject(self, val, context):
        out = filter(context, val)
        return out



_ = Underscore()

# map
mapThree = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
mapSquare = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 2)

# reduce
reduceMultiply = _.reduce([1, 2, 3, 4], lambda x, y: x * y)
reduceSum = _.reduce([1, 2, 3, 4], lambda x, y: x + y)

# find
findEven = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
findExam = _.find('The chicken laid a brown egg', 'egg')

# filter
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
threes = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0)

# reject
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: not x % 2 == 0)
notThrees = _.reject([1, 2, 3, 4, 5, 6], lambda x: not x % 3 == 0)

print '\nMap'
print 'List multiplied by 3:', mapThree
print 'List squared:', mapSquare
print '\nReduce:'
print 'List multiplied together:', reduceMultiply
print 'List added together:', reduceSum
print '\nFind:'
print 'Find first instance of even in list:', findEven
print 'Find first instance of string in string:', findExam
print '\nFilter:'
print 'Filter list to only include evens:', evens
print 'Filter list to only include multiples of three:', threes
print '\nReject:'
print 'Filter list to only exclude evens:', odds
print 'Filter list to only exclude multiples of three:', notThrees
