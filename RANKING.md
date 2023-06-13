# Text Ranking

Process of ordering text by some criteria of relevance. The goal of text ranking is to generate an ordered list of texts retrieved from a corpus in response to a query for a particular task.

Ranking of query is one of the fundamental problems in information retrieval (IR).
Given a query $q$ and a collection $D$ of documents that match the query, the problem is to rank, that is, sort, the documents in $D$ according to some criterion so that the "best" (most relevant) results appear early in the result list displayed to the user.

## Vector Space
Text (query and documents) are reresented as BoW TF-IDF vectors. The similarity score between query and each document can be found by calculating cosine value between query weight vector and document weight vector using cosine similarity. Desired documents can be fetched by ranking them according to similarity score and fetched top k documents which has the highest scores or most relevant to query vector.


## Learning to Rank
Learning to Rank (L2R or LTR), or machine-learned ranking (MLR), is the application of machine learning techniques for the creation of ranking models for information retrieval systems.

### Pointwise Ranking
Pointwise Ranking use a linear or parametric regression approach and aims to predict the score a human would assign to the relevance of a document-query pair using the feature vector containing the numeric data on the search query used and the document itself. For example, based on a search query of “ultra portable laptop”, the model predicts the relevance scores it would expect a human to assign for each document (or product page).

You simply feed the model your feature vectors, get the predicted scores back from the regression model using Pointwise Ranking, and order the search results from the highest score to the lowest. To compare the accuracy of results, the predicted score can be compared to the actual score, and the Mean Squared Error (MSE) can be used to measure this.

The other approach you can use is to predict the rank that each document would achieve, if they were ranked by a human moderator. For example, if I search for “apple laptop”, I’d expect to see “MacBook Pro 13"” at the top of the results, rather than “apple laptop sleeve”. The model would then be used to predict the rank (1, 2, 3 etc.) for each document or product and this could be compared to the ranks assigned by the human moderator.

### Pairwise Ranking
Pairwise Ranking looks at pairs of documents and predicts which document should be considered more relevant and which should be considered less relevant, and then uses the outputs to help improve the model. Two common Pairwise Ranking algorithms are RankNet and LambdaRank. Both were developed by one man - Christopher Burges - and his team at Microsoft.

RankNet is a feed-forward neural network that is given pairs of documents to predict whether one will appear before the other in search results. Although it’s a bit of a black box, under the hood it adjusts weights in the neural network so relevant documents become more relevant and irrelevant documents become even less relevant.

LambdaRank was based on RankNet and also uses a feed-forward neural net, but aims to tackle the issue around relevance at the top of the search results in a way which RankNet didn’t do. As it uses an improved distance metric for determining its accuracy, it gives extra weight to improved accuracy at the top of the result set, where most people are looking and judging the search result performance. Results from LambdaRank are therefore stronger than those of RankNet.

### Listwise Ranking
Listwise approaches directly look at the entire list of documents and try to come up with the optimal ordering for it. LambdaMART, for instance, is essentially a version of LambdaRank which uses boosted decision trees to move documents to leaf nodes and obtain the scores which are used to determine ranks.

## Evaluation

**Precision**

Precision measures the exactness of the retrieval process. If the actual set of relevant documents is denoted by I and the retrieved set of documents is denoted by O, then the precision is | I intersect O | / | O |

**Recall**

Recall is a measure of completeness of the IR process. If the actual set of relevant documents is denoted by I and the retrieved set of documents is denoted by O, then the recall is | I intersect O | / | I |

**F1 Score**

F1 Score tries to combine the precision and recall measure. It is the harmonic mean of the two. If P is the precision and R is the recall then the F-Score is 2 [(P * R) / (P + R)]

**Average Precision**

Precision and recall are single-value metrics based on the whole list of documents returned by the system. For systems that return a ranked sequence of documents, it is desirable to also consider the order in which the returned documents are presented.

**MAP (Mean Average Precision)**

Mean average precision (MAP) for a set of queries is the mean of the average precision scores for each query.

**DCG (Discounted Cumulative Gain)**

SUM rel_i / log_2 (i + 1)


**NDCG (Normalised Discounted Cumulative Gain)**

A means of measuring accuracy. NDCG uses the predicted rank, the actual rank, and the true score, to give you a distance metric that considers the rankings at the top to be more important than those at the bottom. The normalising bit comes from dividing the discounted cumulative gain by the optimal discounted cumulative gain achieved by returning perfectly relevant results. Since NDCG is so important at the top of the results set, it’s often calculated only for the top set of results, i.e. NDCG@K.

## References

[https://towardsdatascience.com/learning-to-rank-a-complete-guide-to-ranking-using-machine-learning-4c9688d370d4](https://towardsdatascience.com/learning-to-rank-a-complete-guide-to-ranking-using-machine-learning-4c9688d370d4)

## Example Notebook

[https://colab.research.google.com/drive/1hG8dkzqxUXtzPyK9RoAnefKBfhFehL7C](https://colab.research.google.com/drive/1hG8dkzqxUXtzPyK9RoAnefKBfhFehL7C)
