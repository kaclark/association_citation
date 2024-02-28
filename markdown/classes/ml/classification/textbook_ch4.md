# CLASSIFICATION

####4.1 Classification

Classification is a machine learning problem seeking to map from input &Ropf;^d to outputs in an unordered set. Examples of classification output sets could be {apples, oranges, pears} if we're trying to figure out what type of fruit we have, or {heartattack, noheartattack} is we're working in an emergency room and trying to give the best medical care to a new patient. We focus on an essential simple case, binary classification, where we aim to find a mapping from &Ropf;^d to two outputs. While we should think of the outputs as not having an order, it's often convenient to encode them as {-1,+1}. As before, let the letter h (for hypothesis) represent a classifier, so the classification process looks like:

x &rarr; h &rarr; y

Like regression, classification is a supervised learning problem, in which we are given a training data set of the form

D&#8345; &equals; {(x&#8317;&sup1;&#8318;, y&#8317;&sup1;&#8318;), ..., (x&#8317;&#8319;&#8318;, y&#8317;&#8319;&#8318;)}

We will assume that each x&#8317;&sup1;&#8318; is a d x 1 column vector. The intended meaning of this data is that, when given an input x&#8317;&sup1;&#8318;, the learned hypothesis should generate output y&#8317;&sup1;&#8318;.

What makes a classifier useful? As in regression, we want it to work well on new data, making good predictions on examples it hasn't seen. but we don't know exatly what data this classifier might be tested on when we use it in the real world. So, we have to assume a connection between the training data and testing data; typically, they are drawn independently from the same probability distribution.

In classification, we will often use 0-1 loss for evaluation (as discussed in Section 1.3). For that choice, we can write the training error and the testing error. In particular, given a training set D&#8345; and a classifier h, we define the training error of h to be 

E&#8345;(h) = $\frac{1}{n}$ $\sum_{i=1}^{n}$ 
