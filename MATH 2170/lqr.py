import numpy as np

def lstsq_constraint(A, b, C, d):   #|Ax-b|^2 is the objective to minimize
    ATA = A.T @ A                   #subject to the constraint Cx=d
    CT = (C.T).reshape((len(ATA), -1))
    p = len(CT[0])
    KKT = np.block([[2*ATA, CT], [CT.T, np.zeros((p, p))]])
    KKTb = np.hstack((2*A.T @ b, d))
    return np.linalg.solve(KKT, KKTb)[:-p]

#Linear Quadratic Regulator
def lqr(A, B, C, a, b, T, rho):     
    n = len(A)
    Bmtx,Cmtx = B.reshape((n,-1)),C.reshape((-1,n))
    m,p = len(Bmtx[0]),len(Cmtx)
    Ablock = np.block([
        [np.kron(np.eye(T+1),Cmtx),np.zeros((p*(T+1),m*T))], 
        [np.zeros((m*T,n*(T+1))),np.sqrt(rho)*np.eye(m*T)]])
    Cblock = np.block([
            [np.kron(np.eye(T,T+1),A) - np.kron(np.eye(T,T+1,1),np.eye(n)),
                  np.kron(np.eye(T),Bmtx)], 
            [np.kron(np.vstack([np.eye(1,T+1,0),np.eye(1,T+1,T)]),np.eye(n)),
                  np.zeros((2*n,m*T))]])
    dblock = np.concatenate((np.zeros(n*T),a,b))
    z = lstsq_constraint(Ablock,np.zeros(len(Ablock)),Cblock,dblock)
    
    x = np.array([z[i*n:(i+1)*n] for i in range(T+1)])
    u = np.array([z[n*(T+1)+(i)*m: n*(T+1)+(i+1)*m] for i in range(T)])
    y = np.array([C @ xt for xt in x])
    return x, u, y 

## Parameters #######
# x_(t+1) = Ax_t + Bu_t
A = np.array([[0.99, 0.03, -0.02, -0.31], [0.01, 0.47, 4.70, 0.00], [0.02, -0.06, 0.40, 0.00], [0.01, -0.04, 0.72, 0.99]])
# enter the transition matrix A
B = np.array([[0.01, 0.99], [-3.44, 1.66], [-0.83, 0.44], [-0.47, 0.25]])
# enter the input matrix B
# y_t = Cx_t
C = np.eye(4)
# enter the output matrix C
a = np.array([0, 0, 0, 1])
# x_0
b = a = np.array([0, 0, 0, 0])
# x_T
T = 120
# the number of iterations in the time series


## Simulations #######
import matplotlib.pyplot as plt
## No Control ##
Xno = np.zeros((T+1,len(a)))  #initialize Xno
Xno[0] = a
for k in range(T):             #simulation without control 
    Xno[k+1] = A @ Xno[k]
# plot output vector y_t (there is no control vector u_t)
Yno = np.array(C @ Xno.T).T
for yi in range(len(Yno[0])):
    plt.plot(np.arange(T+1),Yno[:,yi],label=f"y_t{yi}")
plt.ylabel("y_t")
plt.xlabel("t\n No Control")
plt.ylim(-4,3)
plt.legend()
plt.show()


## Linear Quadratic Control ##
rho = 100
#initialize sequences X (states), U (input/control), Y (output)
X,U,Y = lqr(A,B,C,a,b,T,rho)
# plot input vectors u_t
plt.plot(np.arange(T),U,label=[f"u_t{i}" for i in range(len(U[0]))])
plt.xlabel('t\n rho = ' + str(rho))
plt.ylabel('u_t')
plt.ylim(-0.05,0.25)
plt.legend()
plt.show()
# plot output vectors y_t
plt.plot(np.arange(T+1),Y,label=[f"y_t{i}" for i in range(len(Y[0]))])
plt.xlabel('t\n rho = ' + str(rho))
plt.ylabel('y_t')
plt.ylim(-4,3)
plt.legend()
plt.show()


#Linear State Feedback Control
KT = np.zeros(B.shape)             #initialize/compute state-feedback gain matrix
for  i in range(len(A)):
    X,U,Y = lqr(A,B,C,np.eye(1,len(A),i)[0],b,T,rho)
    KT[i] = U[0]
K = KT.T

ABK = A + B@K    #form matrix A + BK, outer product used to avoid having to reshape vectors as matrices
Xst = np.zeros((T+1,len(A)))   #initialize Xst
Xst[0] = a
for k in range(T):         #simulation with state-feedback control
    Xst[k+1] = ABK @ Xst[k]
Yst = np.array(C @ Xst.T).T
# plot input vectors u_t
plt.plot(np.arange(T), [K @ x for x in Xst[:-1]],label=[f"u_t{i}" for i in range(len(U[0]))])
plt.xlabel("t\n State Feedback Control")
plt.ylabel('u_t')
plt.ylim(-0.05,0.25)
plt.legend()
plt.show()
  # plot output vectors y_t   
plt.plot(np.arange(T+1),Yst,label=[f"y_t{i}" for i in range(len(Y[0]))])
plt.xlabel("t\n State Feedback Control")
plt.ylabel("y_t")
plt.ylim(-4,3)
plt.legend()
plt.show()

## Analysis #######
print("Based on the graphs, nothing seems to have changed. I am unsure if I did it correctly, however" \
"based on that, nothing seems to have changed.") #How do these three simulations compare?
