import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y_train ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to train your model using training CRPs
	# X_train has 32 columns containing the challeenge bits
	# y_train contains the responses

	# THE RETURNED MODEL SHOULD BE A SINGLE VECTOR AND A BIAS TERM
	# If you do not wish to use a bias term, set it to 0
  X_feature = my_map(X_train)
  clf = LogisticRegression(random_state = 42, max_iter = 1000,dual = False , penalty = 'l2', C=10)
  clf.fit(X_feature, y_train)
  w = clf.coef_[0]
  b = clf.intercept_
  return w, b

################################
# Non Editable Region Starting #
################################
def my_map( X ):

################################
#  Non Editable Region Ending  #
################################

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
  X_feature = []
  D = 1 - 2 * X
  D_rev = np.flip(D, axis=1)
  X_rev = np.cumprod(D_rev, axis=1)
  C = np.flip(X_rev, axis=1)
  indices = np.triu_indices(32, k=1)
  combinations = C[:, indices[0]] * C[:, indices[1]]
  X_feature = np.concatenate((combinations, C), axis=1)
  return X_feature