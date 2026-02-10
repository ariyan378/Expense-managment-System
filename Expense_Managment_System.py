

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
        
    def add_expense(self,expense):
        
        if  not isinstance(expense,Expense):
            raise TypeError('add_expense expects an Expense object')
        self.expense.append(expense)
        self.category.append(expense.category)
        
    def remove_expense_by_index(self, index):
        
        if index <0 or index >len(self.expense):
            
            raise IndexError('Index out of range')
        
        removed  = self.expense.pop(index)
        
        self._rebuild_category()
        
        return removed
    
    def _rebuild_category(self):
        
        new_set = set()
        
        for e in self.expense:
            new_set.add(e.category)
        
        self.category=new_set
    
    def list_expense(self):
        return [e.to_dict() for e in self.expense]
    
    def filter_by_category(self,category):
        return[ e for e in self.expense if e.category.lower()==category.lower()]       
    
    def filter_by_month(self, year, month):
        
        result=[]
        
        y,m,_=e.date_tuple()        
        for e in self.expense:
            if y == year and m == month:
                result.append(e)
        
        
        return result
    
    def total_expense(self):
        
        total = 0.0
        
        for e in self.expense:
            total+=e.amount 
            
            
        return total
    
    def total_by_category (self):
        
        total={}  
        
        for e in self.expense:
            if e.category not in total:
                total[e.category]=0.0
                
            total[e.category]+=e.amount
        
        return total
    
    
