class Expense:
    
    def __init__(self,amount,category,date_str,note=''):
        '''
        i am declaring the single expense data in here
        '''
        self.amount = float(amount)
        self.category=str(category).strip()
        self.date = str(date_str).strip()
        self.note = str(note).strip()
        
    def date_tuple (self):
        '''
        making year , month , date seperate for future filtering like anyone can track there expense by date or year 
        
        '''
        
        parts = self.date.strip('-')
        
        if len(parts)!=3:
            return (0,0,0)
        
            
        year=  int(parts[0])
        month= int (parts[1])
        date=  int(parts[2])
        
        return year, month,date
    
    def to_dic(self):
        '''
        saving it in dictionary format so that i can convert  this into pandas dataset for data analysis
        '''
        
        return {
            
            'Amount': self.amount,
            'Category': self.category,
            'Date'  : self.date,
            'Note':self.note
        }
    
    def __repr__(self):
        
        return f"Expense(Amount : {self.amount}) , Category : {self.category},Date : {self.date}"  
    

class ExpenseManager :
    
    def __init__(self):
        
        '''
    we will work with multiple expense here.if nothing given it will hold a empty expense list and category set
        '''
        self.expense=[]
        self.category = set()
        
              