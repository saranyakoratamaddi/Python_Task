#7. Student Result Generator (Method Overloading Concept) 
#A school system calculates student results differently depending on available data. Create a Result class where a method can calculate the result using either two 
#subjects or three subjects. 





class Result:
    def __init__(self,sub1,sub2,sub3=None):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def result(self):
        if self.sub3 is not None:
            total=self.sub1+self.sub2+self.sub3
            average=total/3
            print(f"3 Subjects total: {total} \n Average is : {average}")
        else:
            total=self.sub1+self.sub2
            average=total/2
            print(f"Total of two Subjects is: {total} \n Average is : {average}")
s1=Result(97,65,87)
s1.result()
s2=Result(97,65)
s2.result()
                
            
        
            
