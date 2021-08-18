# first import the libraries and all 
import matplotlib.pyplot as plt
import  numpy as np
import pandas as pd
# y = β0 + β1 x + error # Yeah Dont freak out , b0 or b1 , notations may change , but the format and sum of it will be the same . Its just a basic simple math

def coeiff_data(xs,ys):  # where we find out the B1 and B0 
    mean_x = np.mean(xs)
    mean_y = np.mean(ys)
    m = len(xs)
    numer = 0
    denom = 0
    for i in range(m):  # we can use any other ways for calcuating the b1 or b0 by using loop , of you are familiar with loops and all .. (I was too) 
        numer += (xs[i] - mean_x) * (ys[i]-mean_y)
        denom += (xs[i]- mean_x)**2   
    b1 = numer / denom # B1
    b0 = mean_y - (b1*mean_x) # B2
    return b1,b0   # That's it , the main work is done ! rest is like flowing water ....

xs = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) # our x-axis 
ys = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) # y-axis

b1,b0 = coeiff_data(xs,ys)

x_pred = np.array([3]) # The value we want to precict from x , gives us the Y(axis)
y_pred = b0 + (b1*x_pred) # The formula y^ = b0 + b1 + x

m = len(xs)
## thats it ! The work is done ! now all we have to do is plotting it for visualization and better grasp ...

ss_t = 0 # finding r2 is also simple , you find the error (the differnce between the actual values and our predicted values . for now it does nothing in our program, just for understanding)
ss_r = 0
for i in range(m):
    y_predd = b0 + b1 * xs[i]
    ss_t += (ys[i] - np.mean(ys))**2
    ss_r += (ys[i] - y_predd)**2
r2 = 1 - (ss_r/ss_t)
print(f"The r2 is : {r2}")
if r2 > 0.60 : print("Its a good r2 score ")

#regression_line
reg_line = [(b1*i)+b0 for i in xs] # looping ... you can do it like for i in : then plotting reg_line inside it .....

#plotting for  visualization
plt.scatter(xs,ys,color="blue",label="x axis and y axis") #our data points
plt.plot(xs,reg_line,color="pink",label="regression line") #reg_line
plt.scatter(x_pred,y_pred,color="r",marker="*",s=150,label="the predicted") #our predicted values
plt.legend()
plt.show()

#Done , hope the way it represented to you may find in a better way .... 
