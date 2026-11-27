#8. Pie Chart with Conditional Data 
#Scenario: 
#scores = np.array([40, 60, 80, 30, 90]) 
#Task: 
#● Categorize into: 
#○ Pass (>50) 
#○ Fail (<=50) 
#● Count using NumPy/Pandas 
#● Plot pie chart for Pass vs Fail





import matplotlib.pyplot as plt
import numpy as np
score = np.array([40, 60, 80, 30, 90])
pass_count=np.sum(score>50)
fail_count=np.sum(score<=50)
label=['Pass(>50)','Fail(<=50)']
counts=[pass_count,fail_count]
colors=['#4CAF50','#F44336']
plt.pie(counts,labels=label,autopct='%1.1f%%',startangle=90,colors=colors)
plt.title('Pass vs Fial Distribution')
plt.axis('equal')
plt.show()
       

