from sklearn.metrics import plot_confusion_matrix, confusion_matrix
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

def evaluate_model(model, X, y):
    y_pred = model.predict(X)
    print(f'Accuracy Score: {round(accuracy_score(y, y_pred), 2)}')
    print(f'Recall Score: {round(recall_score(y, y_pred), 2)}')
    print(f'Precision Score: {round(precision_score(y, y_pred), 2)}')
    print(f'F1 Score: {round(f1_score(y, y_pred), 2)}')
    plot_confusion_matrix(model, X, y,cmap="Blues")
    
