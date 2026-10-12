import numpy as np

###EXERCISE 1 #################################
#Use the adjacency matrix for the graph in Example 3.2.4 (below), 
#compute the number of walks from A to D of length 10 
#and the number of walks from B to F of length 20.

#the adjacency matrix of graph G
AG = np.array([[0,1,1,1,0,0],#A
              [1,0,1,0,0,0],#B
              [1,1,0,0,0,0],#C
              [1,0,0,0,1,1],#D
              [0,0,0,1,0,1],#E
              [0,0,0,1,1,0]])#F

#compute A^10
a = np.linalg.matrix_power(AG,10)
aa = a[0, 3]
print("The number of paths from A to D of length 10 is ", aa) 
#what from A^10 tells us about the paths from A to D of length 10?
#solution = 1560

b = np.linalg.matrix_power(AG, 20)
bb = b[1, 5]
#next, compute A^20 and find the number of paths from B to F of length 20. 
print("The number of paths from B to F of length 20 is ", bb) 
#solution = 5640122


###EXERCISE 2 #################################
#For the following time series, smooth the series using the probabilities [1/3, 1/3, 1/3], 
#[1/6, 2/3, 1/6], [1/4, 1/2, 1/4], [1/5, 1/5, 1/5, 1/5, 1/5], [1/16, 1/4, 3/8, 1/4, 1/16], 
#and [1/8, 1/8, 1/2, 1/8, 1/8]. Submit a graphic for the original line graph and all 
#six possible smoothings. Make some observations and guesses about how the probability vector 
#affects the smoothing process. 

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid') #use 'seaborn-whitegrid' if error with plt

#the time series
X = np.array([10,9.371811379420594,8.875298622037981,8.875298622037981,9.413188493680384,9.413188493680384,
              10.005260023166363,10.005260023166363,10.62924298508378,11.464006184635922,11.464006184635922,
              11.464006184635922,11.464006184635922,11.887537216409891,11.136357062824521,11.136357062824521,
              11.057236630582612,11.057236630582612,10.798318071238844,10.798318071238844,10.063193063599943,
              10.063193063599943,10.796002894317288,10.43359762177321,10.43359762177321,10.43359762177321,
              10.43359762177321,10.394463477531714,10.600431329399168,10.400426591397789,10.400426591397789,
              10.771488728209894,10.771488728209894,11.577428139463887,12.111630742901735,12.111630742901735,
              12.111630742901735,11.866406250515109,12.271076219242298,12.89479859610239,12.856672009243878,
              13.286290696282679,12.96551346165231,12.639422476641586,12.455528414123775,12.329913288075115,
              12.695004069851635,13.561852105032148,14.061248398716605,14.061248398716605,13.648903814339857,
              13.055503739700121,13.055503739700121,13.880262477461535,13.071931815648279,13.675560912985013,
              13.749740729848668,13.717702822891262,13.90157793563202,13.90157793563202,13.90157793563202,
              13.90157793563202,13.147497519777575,13.147497519777575,12.575565131897557,12.707883909724249,
              12.882675782526304,13.701097368923673,13.701097368923673,14.630008125430347,13.676289173463838,
              13.148556398889397,13.153805401097026,12.395273542254046,11.824495878620004,11.518982735863297,
              12.062092410196717,12.476569666258783,12.383819715681016,12.383819715681016,12.493781195029124,
              11.603802562792879,11.95629293894893,12.473014374446954,12.473014374446954,12.452996449041787,
              11.677758550423894,11.228792060302096,11.228792060302096,12.003606594060193,12.003606594060193,
              11.123108018696819,10.295494633158782,10.295494633158782,10.295494633158782,11.151995486321882,
              10.854998525756114,11.25897818776794,11.949393024607282,11.902840036110444])
#graph X
plt.plot(range(len(X)), X)   
plt.xlim(0,len(X)) 
plt.ylim(8, 15)  
plt.show()

#convolution by [1/3, 1/3, 1/3]
Y = np.convolve(X, [1/3, 1/3, 1/3])
plt.plot(range(98), Y[2:100])   #You need to trim off the first and last two terms as they 
plt.xlim(0,len(Y))              #behave weird.  
plt.ylim(8, 15)  
plt.show()

#Now, convolve by [1/6, 2/3, 1/6], [1/4, 1/2, 1/4], [1/5, 1/5, 1/5, 1/5, 1/5], 
#[1/16, 1/4, 3/8, 1/4, 1/16], and [1/8, 1/8, 1/2, 1/8, 1/8].

a = np.convolve(X, [1/6, 2/3, 1/6])
b = np.convolve(X, [1/4, 1/2, 1/4])
c = np.convolve(X, [1/5, 1/5, 1/5, 1/5, 1/5])
d = np.convolve(X, [1/16, 1/4, 3/8, 1/4, 1/16])
e = np.convolve(X, [1/8, 1/8, 1/2, 1/8, 1/8])

plt.plot(range(98), a[2:100])   #You need to trim off the first and last two terms as they 
plt.xlim(0,len(a))              #behave weird.  
plt.ylim(8, 15)  
plt.show()

plt.plot(range(98), b[2:100])   #You need to trim off the first and last two terms as they 
plt.xlim(0,len(b))              #behave weird.  
plt.ylim(8, 15)  
plt.show()

plt.plot(range(98), c[2:100])   #You need to trim off the first and last two terms as they 
plt.xlim(0,len(c))              #behave weird.  
plt.ylim(8, 15)  
plt.show()

plt.plot(range(98), d[2:100])   #You need to trim off the first and last two terms as they 
plt.xlim(0,len(d))              #behave weird.  
plt.ylim(8, 15)  
plt.show()

plt.plot(range(98), e[2:100])   #You need to trim off the first and last two terms as they 
plt.xlim(0,len(e))              #behave weird.  
plt.ylim(8, 15)  
plt.show()

#Make some observations and guesses about how the probability vector 
#affects the smoothing process. 
print()

# It looks like it has a completely different smoothness levels. Some make the graphs spiky, while others are more smoother.