# Residue-Similarity (R-S) scores
Compute the RS scores for the data

The rs_score.py computes the R-score, S-score and RS-score for each data. This requires your feature and a set of labels for your features.
These labels can be from the true-label or from your predicted labels. For true-labels, R-,S- and RS-score reveals the geometric property of the data.

You can utilize RS score in 2 ways. If you have a train-test split, you can compute RS scores for the test split, using the training set as the embedding space.
If there is not train-test split, you can compute RS scores by using the entire data.

python rs_score.py has 3 main codes.
* rs(Xtrain, ytrain, Xtest, ytest, metric = 'euclidean')
  * This is used for training/testing split data
  * Xtrain is the training data
  * ytrain is the training label
  * Xtest is the testing data
  * ytest is the testing label
* rs_full(X, y, metric = 'euclidean')
  * This is used when the RS scores of all data is used
  * X is the data
  * y is the class or cluster label
* rs_index(rs_score, y, label )
  * This is used to obtain the CRI and CSI
  * rs_score: obtained from above code
  * y is the class or cluster label
  * label: the unique labels, as a list
 

rs_plot is used to produce the RS plot
* Once you obtain the rs_score from rs() or rs_full(), run adjustCoordinate
  * adjustCoordinate(rs_score, y, max_col = None)
    * y is the predicted label
    * max_col is the number of columns you want in the RS plot
* constructFigure(rs_score, y, color_discrete_map = color_discrete_map,  symbol_discrete_map = symbol_discrete_map)
    * rs_score: the coordinate adjusted RS scores from adjustCoordinate
    * y is the predicted label. This is used to color the points on the RS plot
    * color_discrete_map, symbol_discrete_map these are 2 parameters from plotly. Please refer to plotly's documentation on styling markers and colors.
