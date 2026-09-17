
class Student:
    def calculate_result(self,name,math,python,java):
        marks =[math,python,java]
        total = 0
    
        for mark in marks:
           total += mark
        average = total/len(marks)
        print("Name:",name)
        print("Total:",total)
        print("Average:",average)
        
        if average >=90:
           print("Grand A")
        elif average >=75:  
            print("Grand B")
        elif average >=60:  
            print("Grand C")
        else:     
           print("Grand D")
           
student = Student() 
student.calculate_result("Shristi",90,85,95)      
        
        
          
        
        
        
        
    
    