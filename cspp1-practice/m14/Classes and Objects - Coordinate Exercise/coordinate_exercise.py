'''
Exercise: coordinate
Consider the following code from the last lecture video:
'''

class Coordinate(object):
    '''
    Class Coordinate
    '''
    def __init__(self, x_val, y_val):
        '''
        init constructor
        '''
        self.x_val = x_val
        self.y_val = y_val

    def getx(self):
        '''
        Getter method for a Coordinate object's x coordinate.
        Getter methods are better practice than just accessing an attribute directly
        '''
        return self.x_val

    def gety(self):
        '''
        Getter method for a Coordinate object's y coordinate
        '''
        return self.y_val

    def __str__(self):
        '''
        str method
        '''
        return '<' + str(self.getx()) + ',' + str(self.gety()) + '>'

    def __eq__(self, other):
        '''
        eq method
        '''
        return self.x_val == other.x_val and self.y_val == other.y_val

    def __repr__(self):
        '''
        repr methods
        '''
        return "(%s, %s)"%(self.x_val, self.y_val)


# Your task is to define the following two methods for the Coordinate class:
# Add an __eq__ method that returns True if coordinates refer to same point in the plane
#(i.e., have the same x and y coordinate).
# Define __repr__, a special method that returns a string
#that looks like a valid Python expression that could be used to recreate an
# object with the same value. In other words,
#eval(repr(c)) == c given the definition of __eq__ from part 1.





def main():
    '''
    Main method
    '''
    data = input()
    data = data.split(' ')
    data = list(map(int, data))
    print(Coordinate(data[0], data[1]) == Coordinate(data[2], data[3]))
    print(Coordinate(data[4], data[5]).__repr__())

if __name__ == "__main__":
    main()
