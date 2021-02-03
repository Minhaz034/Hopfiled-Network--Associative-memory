#created:20/11/20
#updated: 24/11/20
#author: minhaz_bin_farukee_1503034
import numpy as np

def convert_to_bipolar(X):
    for i in range(len(X)):
        if X[i] == 0:
            X[i] = -1
        elif X[i]==1:
            X[i] = 1
    return X 

def Weight(x):
    w = np.zeros([len(x),len(x)])
    for i in range(len(x)):
        for j in range(i,len(x)):
            if i == j:
                w[i,j] = 0
            else:
                w[i,j] = x[i]*x[j]
                w[j,i] = w[i,j]    
    return w
    

def update_until_unchanged(w,y_vec):
    m = len(y_vec)
    print("y_vec shape=",m)
    print("w shape:",w.shape)
    
    while(True):
        print("Updating...")
        sum = 0;
        #print(sum)
        for i in range(m):        
            
            u_temp = y_vec[i]
            
            #print("previous state:",u_temp)
            u = np.dot(w[i][:],y_vec)
            #print("u=" , u)            
            if u >= 0:
                y_vec[i] = 1
            elif u < 0:
                y_vec[i] = 0
            #print("Current state",y_vec[i])    
            print(" node",i, "Previous State:",u_temp,"New state:",y_vec[i])    
            
            if u_temp != y_vec[i]:
                #print("soman hoy nai")
                sum=sum+1
            elif u_temp==y_vec[i]:
                #print("soman hoise")
                sum=sum+0
            
        print(sum)
        if sum==0:
             print("States are not changing anymore")
             break
    return y_vec


Y = np.array([1,0,1,0,0])
print("Input sequence:")
print(Y)
Y= convert_to_bipolar(Y)

X1 = np.array([1,0,1,0,1])
X2 = np.array([0,1,0,1,0])
X3 = np.array([1,0,1,0,0])
X4 = np.array([1,1,1,0,0])
X5 = np.array([1,0,1,1,0])
X6 = np.array([0,0,1,0,0])


X1 = convert_to_bipolar(X1)
X2 = convert_to_bipolar(X2)
X3 = convert_to_bipolar(X3)
X1 = convert_to_bipolar(X1)
X2 = convert_to_bipolar(X2)
X3 = convert_to_bipolar(X3)

W1 = Weight(X1)
W2 = Weight(X2)
W3 = Weight(X3)
W4 = Weight(X4)
W5 = Weight(X5)
W6 = Weight(X6)

W_f = W1+W2+W3+W4+W5+W6
y_res= update_until_unchanged(W_f,Y)
#y_res = convert_to_binary(y_res)


print("Final Weight:")
print(W_f)

print("        Output from Hopfield net:")
print("        ",y_res)



