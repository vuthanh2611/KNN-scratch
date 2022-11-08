def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0
    

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    # https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9.

    true_positive=0
    false_positive=0
    true_negative=0
    false_negative=0
    for i in range(len(prediction)):
        if prediction[i]==ground_truth[i] and prediction[i]==1:
            true_positive+=1
        elif prediction[i]!=ground_truth[i] and prediction[i]==1 :
            false_positive+=1
        elif prediction[i]==ground_truth[i] and prediction[i]==0 :
            true_negative+=1
        else:
            false_negative+=1
                
    precision=true_positive/(true_positive+false_positive)
    recall=true_positive/(true_positive+false_negative)
    f1=2*(precision*recall)/(precision+recall)
    accuracy=(true_positive+true_negative)/len(prediction)
    
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    num_acc=0
    for i in range(len(prediction)):
        if prediction[i]==ground_truth[i]:
            num_acc+=1
                
    accuracy=num_acc/len(prediction)
                
    
    
    return accuracy
