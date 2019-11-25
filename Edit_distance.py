# Author: Carlos Meza
# CWID: 7306
# CPSC 485

# Program Complile/Run
# This program is written in Python 3.6 on Visual Studio 2017 in a Windows enviroment
# You should be able to run program by simply double clicking the file
# Or by providing filepath to the command prompt
# 
# Program Input:
# Excepts two words to calcualte its edit distance
# 
# Program Output:
# An Edit Matrix
# A Trace Matrjx
# Edit Distance
# Relagnment of input

class edit_distance():
    def __init__(self):
        self.input1 = ''
        self.input2 = ''
        self.realign1 = ''
        self.realign2 = ''
        self.distance = 0

    # this needs to be called first
    def get_input(self):
        self.input1 = input("Enter first word: ").lower()
        self.input2 = input("Enter second word: ").lower()
    
    def create_matrix(self):

        if(self.input1 == ''):
            self.get_input()

        # creates 2d array using lists this implementation
        # allows us to access individual cells
        self.matrix = [[0]*(len(self.input2) +1) for i in range(len(self.input1) + 1 )]
        self.trace_matrix = [[0]*(len(self.input2) +1) for i in range(len(self.input1) + 1 )]
        
        for x in range(len(self.input1) + 1):
            self.matrix[x][0] = x
            if(x == 0):
                self.trace_matrix[x][0] = 's'
            else:
                self.trace_matrix[x][0] = 'u'

        for y in range(len(self.input2) + 1):
            self.matrix[0][y] = y

            if(y == 0):
                self.trace_matrix[0][y] = 's'
            else:
                self.trace_matrix[0][y] = 'l'
                 
    def calculate_distance(self):
        for x in range(1, len(self.matrix)):
            for y in range(1, len(self.matrix[x])):
                horz = self.get_horizontal(x, y)
                vert = self.get_vertical(x, y)
                diag = self.get_diagnol(x, y)

                min = self.get_min(horz, vert, diag)

                self.matrix[x][y] = min[0]
                self.trace_matrix[x][y] = min[1]

    #returns value left of current x, y pos and direction of value
    def get_horizontal(self, x, y):
        return self.matrix[x][y-1] + 1, 'l'

    #returns value above of current x, y pos and direction of value
    def get_vertical(self, x, y):
        return self.matrix[x-1][y] + 1, 'u'

    # returns value diagnol of current x, y pos and direction of value
    def get_diagnol(self, x, y):
        if(self.input1[x-1] == self.input2[y-1]):
            return self.matrix[x-1][y-1], 'd'
        else:
            return self.matrix[x-1][y-1] + 1, 'd'
    
    # returns the minimum along with direction of minimum value
    def get_min(self, horizontal, vertical, diagnol):
           return min(horizontal, vertical, diagnol)

    # returns edit distnace between the two inputs
    def get_distance(self):
        self.distance = self.matrix[-1][-1]
        return self.distance
    
    # prints matrix of integer values
    def print_matrix(self):
        for row in self.matrix:
            print(row)

    # prints the trace matrix
    def print_trace(self):
        for row in self.trace_matrix:
            print(row)

    # calculates realingment of input
    def realign(self):
        holder = ''
        x = len(self.trace_matrix) - 1
        y = len(self.trace_matrix[0]) - 1

        while(holder != 's'):
            holder = self.trace_matrix[x][y]

            if(holder == 'd'):
                self.realign1 += self.input1[x-1]
                self.realign2 += self.input2[y-1]
                x = x - 1
                y = y - 1
            elif(holder == 'l'):
                self.realign1 += '_'
                self.realign2 += self.input2[y-1]
                y = y - 1
            elif(holder == 'u'):
                self.realign1 += self.input1[x-1]
                self.realign2 += '_'
                x = x - 1
            else:
                break

        self.realign1 = self.realign1[::-1]
        self.realign2 = self.realign2[::-1]

    # prints the realignment values
    def print_realignment(self):
        self.realign()
        print(self.realign1)
        print(self.realign2)


def main():
    ed = edit_distance()
    ed.get_input()
    print()

    ed.create_matrix()
    ed.calculate_distance()
    print('The matrices:')
    ed.print_matrix() 
    print()

    ed.print_trace()
    print()

    print('Edit distance is: ' + str(ed.get_distance()))
    print()

    print("The realignment is:")
    ed.print_realignment()

if __name__ == '__main__':
    main()
    input('\n Press ENTER to exit\n')


# NOTE arr = [[0]*len(self.input1)]*len(self.input2) did not work 
# created copies of the same list unable to access individual cells