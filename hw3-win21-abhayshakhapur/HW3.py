# Your name: Abhay Shakhapur
# Your student id:
# Your email: abhaysh@umich.edu
# List who you have worked with on this homework:


# import the random module for use in this program
import random

# Create the class Magic_8
class Magic_8:
    def __init__(self, answer_list):
        self.answer_list=answer_list
        self.question_list=[]
        self.answer_history_list=[]
    def __str__(self):
        return str(self.answer_list)
    def shake_ball(self):
        ind = random.randrange(0, (len(self.answer_list)-1))
        self.answer_history_list.append(ind)
        return self.answer_list[ind]
    def check_question(self, q):
        #q = input("Ask a question")
        if q in self.question_list:
            return "I already answered that question"
        else:
            self.question_list.append(q)
            return self.shake_ball()
    def print_history(self):
        response_list = []
        if len(self.answer_history_list)==0:
            print("None yet")
        else:
            for x in self.answer_history_list:
                print("["+str(x)+"]"+" "+str(self.question_list[self.answer_history_list.index(x)])+" - "+str(self.answer_list[x]))
    def generate_n_responses(self, num):
        self.answer_history_list=[]
        run_len=1
        biggest=0
        run_num=0
        for x in range(num):
            self.shake_ball()
        for x in range(len(self.answer_history_list)-1):
            if self.answer_history_list[x+1]==self.answer_history_list[x]:
                run_len=run_len+1
            else:
                run_len=1
            if biggest<run_len:
                biggest=run_len
                run_num = self.answer_history_list[x]
        print(self.answer_history_list)
        return "longest run was length of "+str(biggest)+" for index "+str(run_num)
        
        
        
  
    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    # it sets this object's answer_list (instance variable) to the passed list of possible answers
    # it sets this object's question_list (instance variable) to the an empty list
    # it sets this object's answer_history_list (instance variable) to an empty list 

    # create the __str__ method
    # It should return a string with all the possible answers 
    # in answer_list separated by commas
    # For example : "Yes, No, Not clear"

    # create the shake_ball method
    # it randomly picks an index from 0 to the number of items in the answer_list minus one
    # it adds that index to the end of the answer_history_list
    # it returns the answer at the picked index

    # create the check_question method that takes a question
    # it checks if the question is in the question_list and if so returns 
    #         "I already answered that question!”
    # Otherwise it adds the question to the question_list and
    # returns the answer from shake_ball

    # create the print_history method
    # prints "[answer index] question - answer" for each of the indices in the answer_history_list
    # from the first to the last with each on a single line.  If there are not items in the 
    # answer_history_list it prints "None yet"
    # it does not return anything!
            
    # EXTRA POINTS
    # create the generate_n_responses method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random response n times by calling shake_ball
    # then returns the index and length of the longest consecutive run
    # It should reset the answer_history_list to an empty list first. 
    # A run is a repetition of the same number consecutively in a list.
    # Ex: If 10 random answers are  [1,5,6,3,2,4,1,4,4,4] then three 4's is the longest run
    # hence the function should return "longest run was length of 3 for index 4
    

def main():

    # You are welcome to replace the answer_list with your desired answers
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8(answer_list)

    # get the first question or quit

    # loop while question is not "quit"
   
        # get an answer from check_question

        # print question - answer

        # get the next question or quit 
main()

def test():
    
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_history()
    print()

    print("Asking the Question: Am I hungry?")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Am I hungry? again")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Should I go for a walk?")
    print(bot2.check_question("Should I go for a walk"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()
    

    print("Testing generate_n_responses method with 200 responses")
    print(bot2.generate_n_responses(200))
test()



# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    #test() - uncomment when you are ready to test your magic 8 ball





