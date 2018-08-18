"""Data module."""

class Data:
    """Class for data aggregation."""
    count =[0,] 
    cont = []
    questions  = dict()
    ans = dict()


    def store_data(self, question):
        """Store data here."""
        self.cont.append(question)
    
    
    def id_generator(self):
        """Generate question id here."""
        self.count[0] = self.count[0] + 100
        return self.count[0]
    

    def store_answer(self):
        """Store answers here"""
        pass
    

    def store_question(self, question):
        """Store question here"""
        if question != "":
            self.questions = {"id": self.id_generator(), "question": question}
            self.store_data(self.questions)
            return True  
        return False
       
