#3. Product Rating System 
#An e-commerce website stores product ratings: 
#[4, 5, 3, 4, 2] 
#Task: 
#● Convert it to a NumPy array. 
#● Print the first and last rating using indexing.




import numpy as np
rating=[4, 5, 3, 4, 2]
ratingarr=np.array(rating)
print(ratingarr)
print("First Rating:",ratingarr[0])
print("Last Rating:",rating[-1])
