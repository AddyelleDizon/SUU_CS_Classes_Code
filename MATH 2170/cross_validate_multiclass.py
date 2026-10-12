import numpy as np
from sklearn.metrics import confusion_matrix as errors #true neg, false pos, false neg, true pos
from sklearn.datasets import load_iris

boolean = lambda b : 2*int(b)-1

def cross_validate_multiclass(X, y, p=2, folds=5):
    m, n = X.shape
    partition = np.array_split(np.random.permutation(m), folds)
    c = np.zeros((p, folds, n))
    training_matrix = np.zeros((folds, p, p)) 
    test_matrix = np.zeros((folds, p, p))
    IsType = np.array([np.array([boolean(yi == j) for yi in y]) for j in range(p)])
    
    for k in range(folds):
        test_index = partition[k]
        training_index = np.concatenate(partition[:k] + partition[k+1:])
        for j in range(p):
            a = np.linalg.lstsq(X[training_index], IsType[j, training_index], rcond=None)[0]
            c[j, k, :] = a 
        training_matrix[k] = errors(y[training_index], [np.argmax([c[j, k] @ x for j in range(p)]) for x in X[training_index]])
        test_matrix[k] = errors(y[test_index], [np.argmax([c[j, k] @ x for j in range(p)]) for x in X[test_index]])
    return c, training_matrix, test_matrix

###################### IRIS EXAMPLE ##################################################
iris = load_iris()
iris_names = iris['target_names']
iris_types = iris['target']
iris_data = np.array(iris['data'])

n = len(iris_types)
X = np.column_stack([iris_data, np.ones(n)])  # add bias term
coeff, train_matrix, test_matrix = cross_validate_multiclass(X, iris_types, len(iris_names))

# Display coefficients and models
for j in range(len(iris_names)):
    print(iris_names[j])
    print(coeff[j], "\n")
    model = "+".join([str(round(np.mean(coeff[j,:,i]),4)) + "x_" + str(i+1) for i in range(5)])
    print("y = " + model[:-3] + "\n")

print("Training Confusion Matrix\n", train_matrix, "\n")    
print("Test Confusion Matrix\n", test_matrix)

accuracy = np.array([[np.trace(train_matrix[j])/sum(sum(train_matrix[j])),
                      np.trace(test_matrix[j])/sum(sum(test_matrix[j]))] for j in range(5)])
print("\nAccuracy = [training, test]\n", accuracy, "\n\n", sum(accuracy)/5, "\n\n")

###################### PREDICTION FOR NEW VECTORS ####################################
new_vectors = np.array([[4, 3, 2, 1],
                        [1, 1, 1, 1]])
new_vectors = np.column_stack([new_vectors, np.ones(new_vectors.shape[0])])  # add bias term

# Average coefficients across folds
avg_coeff = np.mean(coeff, axis=1)

# Predict function
def predict_multiclass(X_new, avg_coeff):
    preds = []
    for x in X_new:
        responses = [avg_coeff[j] @ x for j in range(avg_coeff.shape[0])]
        preds.append(np.argmax(responses))
    return np.array(preds)

predictions = predict_multiclass(new_vectors, avg_coeff)
predicted_names = [iris_names[p] for p in predictions]

for vec, pred in zip(new_vectors, predicted_names):
    print(f"Input vector {vec[:-1]} predicted as: {pred}")