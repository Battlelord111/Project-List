import numpy as np
def computeMSE(observed, predicted):
    #TODO 1: Complete this function
    predicted_vals = np.array(predicted)
    observed_vals = np.array(observed)

    sq_diff = np.square(observed_vals - predicted_vals)

    mse = np.mean(sq_diff)
    return mse


def computeRMSE(observed, predicted):
    #TODO 2: Complete this function
    mse = computeMSE(observed, predicted)
    rmse = np.sqrt(mse)
    return rmse

def computeMAE(observed, predicted):
    # TODO 3: Complete this function
    predicted_vals = np.array(predicted)
    observed_vals = np.array(observed)

    abs_diff = np.absolute(observed_vals - predicted_vals)
    
    mae = np.mean(abs_diff)
    
    return mae

'''
TODO 4: Write driver code that calls the above methods and prints
the MSE, RMSE, and MAE for the following input. (Round
off the results to two decimal places)
    observed = 4,5,12,5,7
    predicted = 5,5,11,4,5
'''
#Driver code
observed = [4,5,12,5,7]
predicted = [5,5,11,4,5]
print(("MSE = {:0.2f}").format(computeMSE(observed,predicted)))
print(("RMSE = {:0.2f}").format(computeRMSE(observed, predicted)))
print(("MAE = {:0.2f}").format(computeMAE(observed, predicted)))