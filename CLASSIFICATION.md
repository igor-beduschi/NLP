# Text Classification

Process of categorizing text into one or more different classes. Text classifiers can be used to organize and structure text.

![Spam Classifier](https://developers.google.com/static/machine-learning/guides/text-classification/images/TextClassificationExample.png)

## Text Classification Steps
![Classification Steps](https://developers.google.com/static/machine-learning/guides/text-classification/images/Workflow.png)

1. Gather Data
2. Explore Data
3. Prepare Data
4. Build and Evaluate Model
5. Tune Hyperparameters
6. Deploy Model



## Classification Approaches
### Rule-Based
Classify text into organized groups by using a set of handcrafted linguistic rules.

Positive:
  - Human comprehensible
  - Can be improved over time

Negative:
  - Requires deep knowledge of the domain
  - Time-consuming: generating rules for a complex system can be quite challenging and usually requires a lot of analysis and testing
  - Difficult to maintain and scale: adding new rules can affect the results of the pre-existing rules.

### ML-Based
Learns to make classifications based on past observations by using pre-labeled examples as training data.

Positive:
  - Usually much more accurate than human-crafted rule-based approaches
  - Easier to maintain and you can always tag new examples to learn new tasks

Negative:
  - Needs a rich source of examples to be trained

## ML-Based Algorithms
### Naive Bayes
The Naive Bayes family of statistical algorithms are some of the most used algorithms in text classification and text analysis.

Naive Bayes is based on Bayes’s Theorem, which helps us compute the conditional probabilities of the occurrence of two events, based on the probabilities of the occurrence of each individual event.

One of the members of that family is Multinomial Naive Bayes (MNB) with a huge advantage, that you can get really good results even when your dataset isn’t very large (~ a couple of thousand tagged samples) and computational resources are scarce.

![Naive Bayes](https://uc-r.github.io/public/images/analytics/naive_bayes/naive_bayes_icon.png)

### Decision Tree
Decision trees are among the most popular machine learning algorithms given their intelligibility and simplicity.

A decision tree or a classification tree is a tree in which each internal (non-leaf) node is labeled with an input feature. The arcs coming from a node labeled with an input feature are labeled with each of the possible values of the target feature or the arc leads to a subordinate decision node on a different input feature. Each leaf of the tree is labeled with a class or a probability distribution over the classes, signifying that the data set has been classified by the tree into either a specific class, or into a particular probability distribution

![Decision Tree](https://res.cloudinary.com/dyd911kmh/image/upload/v1677504957/decision_tree_for_heart_attack_prevention_2140bd762d.png)

### Support Vector Machines (SVM)
SVM draws a line or "hyperplane" that divides a space into two subspaces. One subspace contains vectors (tags) that belong to a group, and another subspace contains vectors that do not belong to that group. The optimal hyperplane is the one with the largest distance between each tag.

Doesn’t need much training data to start providing accurate results

Requires more computational resources than Naive Bayes

Faster and more accurate

![SVM](https://monkeylearn.com/static/446109c153d4467a6e7982ad0d22b570/d8712/image15.webp)

### Logistic Regression
It uses a decision boundary, regression, and distance to evaluate and classify the dataset.

![LogReg](https://images.contentstack.io/v3/assets/blt71da4c740e00faaa/blt65fc9f784a7f2d8d/62b4fe1859fa7e0f945d7d53/text-classification-linear-svm.png)

### Gradient Boosted Trees
It gives a prediction model in the form of an ensemble of weak prediction models, which are typically decision trees.

![GBT](https://www.researchgate.net/publication/351542039/figure/fig1/AS:1022852723662850@1620878501807/Flow-diagram-of-gradient-boosting-machine-learning-method-The-ensemble-classifiers_W640.jpg)

### Multi-Layer Perceptrons

![MLP](https://miro.medium.com/v2/resize:fit:1400/1*MmrWSRkddKWmY7uAnp6DgQ.jpeg)

### Deep Learning
Hierarchical machine learning, using multiple algorithms in a progressive chain of events. It’s similar to how the human brain works when making decisions, using different techniques simultaneously to process huge amounts of data.

Requires much more training data than traditional machine learning algorithms

High accuracy

Lower-level engineering and computation

![Deep Learning](https://editor.analyticsvidhya.com/uploads/75211cnn-schema1.jpg)

### How to Choose de Best Model?

![Choose Model](https://developers.google.com/static/machine-learning/guides/text-classification/images/TextClassificationFlowchart.png)

## Classification Challenges
- Training Data: Providing your algorithm with low-quality data will result in poor future predictions. However, a very common problem among machine learning practitioners is feeding the training model with a data set that is too detailed that include unnecessary features. Overcrowding the data with irrelevant data can result in a decrease in model performance. When it comes to choosing and organizing a data set, Less is More.

- Overfitting: the model begins to learns unintended patterns since training has lasted too long . Be cautious when achieving high accuracy on the training set since the main goal is to develop models that have their accuracy rooted in the testing set (data the model has not seen before).

- Underfitting: training model still has room for improvement and has not yet reached its maximum potential. Poorly trained models stem from the length of time trained or is over-regularized to the dataset.

## Applications
- Filtering Spam: By searching for certain keywords, an email can be categorized as useful or spam.
- Categorizing Text: By using text classifications, applications can categorize different items(articles, books, etc) into different classes by classifying related texts such as the item name, description, and so on. Using such techniques can improve the experience as it makes it easier for users to navigate throughout a database.
- Identifying Hate Speech: Certain social media companies use text classification to detect and ban comments or posts with offensive mannerisms as not allowing any variation of profanity to be typed out and chatted in a multiplayer children's game.
- Marketing and Advertising: Companies can make specific changes to satisfy their customers by understanding how users react to certain products. It can also recommend certain products depending on user reviews toward similar products. Text classification algorithms can be used in conjunction with recommender systems, another deep learning algorithm that many online websites use to gain repeat business.
- Opinion Mining and Sentiment Analysis: reading a text for opinion polarity (positive, negative, neutral, and beyond). Companies use sentiment classifiers on a wide range of applications, like product analytics, brand monitoring, market research, customer support and workforce analytics.
- Topic Labeling: understanding what a given text is talking about. It’s often used for structuring and organizing data, such as organizing customer feedback by topic or organizing news articles by subject.
- Language Detection: classifying incoming text according to its language. These text classifiers are often used for routing purposes (e.g., route support tickets according to their language to the appropriate team).
- Intent Detection: understand the reason behind feedback. Maybe it’s a complaint, or maybe a customer is expressing intent to purchase a product. It’s used for customer service, marketing email responses, generating product analytics, and automating business practices. Intent detection with machine learning can read emails and chatbot conversations and automatically route them to the correct department.

## Datasets
1. [IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
2. [Amazon Reviews Dataset](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)
3. [Yelp Reviews Dataset](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset)
4. [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
5. [Opin Rank Review Dataset](http://archive.ics.uci.edu/ml/datasets/opinrank+review+dataset)
6. [Twitter US Airline Sentiment Dataset](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
7. [Hate Speech and Offensive Language Dataset](https://github.com/t-davidson/hate-speech-and-offensive-language)
8. [Reuters News](http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html)
9. [20 Newsgorups](http://qwone.com/~jason/20Newsgroups/)
10. [Spambase](https://archive.ics.uci.edu/ml/datasets/Spambase)

## Example Notebook

[https://colab.research.google.com/drive/1gQfiLNYPhpCC-gmUD_ofNa0BNeIpfHXG](https://colab.research.google.com/drive/1gQfiLNYPhpCC-gmUD_ofNa0BNeIpfHXG)
