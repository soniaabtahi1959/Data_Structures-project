# @author Sonia Abtahi - 983663036
# FAZE 1 - Part 1
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def ENQUEUE(self, student_number):
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(student_number)
    def DEQUEUE(self):
        if (len(self.stack1) == 0):
            if (len(self.stack2) == 0):
                return None
        while (len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
# ------------------------------------------------------ Main ----------------------------------------------------------
if __name__ == '__main__':
    Yas_Queue = Queue()
    YAS = []
    print("Hello , Welcome to Yas Restuarant .")
    print("------------------------------------------------")
    answer1 = input("Do you want to make a Yas's Queue ? please enter Yes(yes) Or No(no) :")
    if answer1 in "YESYesyes":
        print("------------------------------------------------")
        lenght = int(input("Please enter your Yas's Queue lenght :"))
        if lenght != 0:
            for i in range(2 * lenght):
                answer2 = input("Please enter your student number and it's action [ ENQUEUE(student_number) , DEQUEUE() ] :")
                action = answer2[0]
                if action == "E":
                    student_number = int(answer2[8:(len(answer2) - 1)])
                    Yas_Queue.ENQUEUE(student_number)
                if action == "D":
                    YAS.append(Yas_Queue.DEQUEUE())
            print("-------------------------------------------------")
            print("Your Yas's Queue is :")
            for i in YAS:
                print(i)
                print("----------")
        else:
            print("--------------------------------------------------")
            print("You can't have a Yas's Queue , Try Again !")
    if answer1 in "NONono":
        print("-------------------------------------------------")
        print("Ok, You don't want to make a Yas's Queue !")
        print("------------------- BYE BYE ! -------------------")
        print("-------------------------------------------------")
        quit()
