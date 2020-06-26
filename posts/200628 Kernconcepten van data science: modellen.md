# Kernconcepten van data science: modellen

Een kernconcept binnen data science en analytics zijn **modellen**. Een model te defineren als *een versimpele weergave van de werkelijkheid, ten behoeve van een gespecificeerd doel*. Deze simplificatie vindt plaats op basis van assumpties over *wat wel* en *wat niet* belangrijk is voor deze specifieke toepassing. Het model abstraheert details die niet belangrijk zijn weg en behoudt datgene wat wel van belang is. Zo is een routekaart een weergave van de wereld met als doel om navigeren te vereenvoudigen. Modelen abstraheren details weg die niet van toepassing.

> Een model is een versimpele weergave van de werkelijkheid ten behoeve van een gespecificeerd doel.

## Modelleringstechnieken

- **Statistisch model**: modeleren waarbij begrip van relaties van belang is. Omvat hypothesevorming vooraf; welke variabele beïnvloedt wat? Wat zijn de verbanden? Uiteindelijke model valideert deze hypothese.  
- **Machine learning model**: modeleren waarbij begrip van relaties tussen variablen **niet** van belang is, en het gaat om een zo goed mogelijke voorspelling van de target variabele te doen. Geen hypothesevorming. "Leert" zelf patronen in de data; training en validatie van split in data (train- en testset).

## Doeleinden

- **Descriptieve modellen**: begrip opdoen van een bestaand fenomeen
- **Voorspelmodellen** (*predictive model*): zo goed mogelijk benaderen van een vooraf gespecificeerde target variabele. een formule om een bepaalde waarde van keuze te benaderen. Die formule kan wiskundig zijn, of een *logical statement* zoals een *business rule*.

### Aantekeningen

Lift: how much more prevalent a pattern is than would be expected by chance


Data science is a set of fundamental principles that guide the extraction of knowledge from data


Data mining is the extraction of knowledge from data, via technologies that incorporate these principles


Widest application of data-mining techniques are in marketing


A predictive model abstracts way most of the complexity of the world, focusing in on a particular set of indicators that correlate in some way with a quantity of interest


In our churn-prediction example, we would like to take the data on prior churn and extract patterns, for example patterns of behavior, that are useful - that can help us to predict those customers who are most likely to leavy in the future, or that can help us design better services


Extracting useful knowledge from data to solve business problems can be treated systematically by following a process with reasonably well-defined stages


From a large mass of data, information technology can be used to find informative descriptive attributes of entities of interest


If you look too hard at a set of data, you will find something - but it might not generalize beyond the data that you are looking at (overfitting)


Formulating data mining solutions and evaluating the results involves thinking carefully about the contexted in which they will be used


Underlying the extensive body of techniques for mining data is a much smaller set of fundamental concepts compromising data science


An important principe of data science is that data mining is a process with fairly well-understood stages


Fundamental concepts


Classification and class probability estimation attempt to predict, for each individual in a population, which of a (small) set of classes this individual belong to


A closely related task is scoring or class probability estimation. A scoring model applied to an individual produces, instead of a class prediction, a score representing the probability that the indivual belongs to each class. Classification and scoring are very closely related


Regression ("value estimation") attempts to estimate or predict, for each individual, the numerical value of some variable for that individual


Informally, classification predicts whether something will happen, whereas regression predicts how much something will hapen


Similarity matching attempts to identify similar individuals based on data known about them. For example, IBM is interested in finding companies similar to their best business customers, in order to focus their sales force on the best opportunities.


Clustering attempts to group individuals in a population together by their similarity, but not driven by any purpose


Co-occurance grouping attempts to find associations between entities based on transactions involving them.


When there is no target, the data mining is referred to as unsupervised.


The value for the target variable for an individual is often called the individual's label, emphasizing that often (not always) one must incur expense to actively label the data.


Two main subclasses of supervised data mining, classification and regression, are distinguished by the type of target. Regression involves a numeric target while classification involves a categorical (often binary) target.


Recall that the primary goal of data science for business is to support decision making, and that we started the process by focusing on the business problem we would like to solve.


Data warehouses collect and coalesce data from across an enterprise, often from multiple transaction-processing systems, each with its own database.


Data warehousing may be seen as a facilitating technology of data mining. It is not always necessary, as most data mining does not access a data warehouse, but firms that decide to invest in data warehouses often can apply data mining techniques much more broadly and more deeply in the organization.


Information is a quantity that reduces uncertainty about something


A model is a simplified representation of reality created to serve a purpose. It is simplified based on some assumptions about what is and what is not important for the specific purpose.


For example, a map is a model of the physical world


Each of these abstracts away details that are not relevant to their main purpose and keep those that are.


A predictive model is a formula for estimating the unknown value of interest: the target. The formula could be mathematical, or it could be a logical statement such as a rule.


In common usage, prediction means to forecast a future event. In data science, prediction more generally means to estimate an unknown value.


This is in contrast to descriptive modeling, where the primary purpose of the model is not to estimate a value but instead gain insight into the underlying phenomenon or process.


Supervised learning is model creation where the model describes a relationship between a set of selected variables (attributes or features) and a predefined variable called the target variable. The model estimates the value of the target variable as a function (possibily a probabilistic function) of the features.


An instance or example represents the fact or a data point.


An instance is also sometimes called a feature vector, because it can be represented as a fixed-length ordered collection (vector) of feature values.


The creation of models from data is known as model induction. Induction is a term from philosophy that refers to generalizing from specific cases to general rules (or laws, or truths).


Deduction starts with general rules and specific facts, and creates other specific facts from them


The input data for the induction algorithm, used for inducing the model, are called the training data. They are called labeled data because the value for the target variable is known.


Recall that a predictive model focuses on estimating the value of some particular target variable of interest


Entrophy is a measure of disorder that can be applied to a set, such as one of our individual segments


With entrophy to measure how disordered any set is, we can define information gain (IG) to measure how much an attribute improves (decreases) entrophy over the whole segmentation it creates.


As we have seen, predictive modeling involves finding a model of the target variable in terms of other descriptive attributes.


The data miner specifies the form of the model and the attributes; the goal of the data mining is to tune the parameters so that the model fits the data as well as possible. This general approach is called parameter learning or parametric modeling.


We now have a parameterized model: the weights of the linear function (w_i) are the parameters. The data mining is going to "fit" this parameterized model to a particular dataset - meaning specifically, to find a good set of weights on the features.


Our general procedure will be to define an objective function that represents our goal, and can be articulated for a particular set of weights and a partical set of data.


On of the most useful data mining techniques of all: logistic regression.


Logistic regression applies linear models to class probability estimation, which is particulary useful for many applications.


Linear regression, logistic regression, and support vector machines are all very similar instances of our basic fundamental technique: fitting a (linear) model to data. The key difference is that each uses a different objective function.


In short, support vector machines are linear discriminants.


SVMs choose based on a simple, elegant idea: instead of thinking about seperating with a line, first fit the fattest bar between the classes.


Then once the widest bar is found, the linear discriminant will be the center line through the bar.


The term "loss" is used across data science as a general term for error penalty.


Within this same framework for fitting linear models to data, by choosing a different objective function we can produce a model designed to give accurate estimates of class probability. The most common procedure by which we do this is called logistic regression.


What is important to understand is what logistic regression is doing. It is estimating the log-odds, or more loosely, the probability of class membership (a numeric quantity) over a categorical class.


A classification tree uses decision boundaries that are perpendicular to the instance-space axes, whereas the linear classifier can use decision boundaries of any direction or orientation. This is a direct consequence of the fact that classification trees select a single attribute at a time whereas linear classifiers use a weighted combination of all attributes.


A classification tree is a "piecewise" classifier that segments the instance space recursively when it has to, using a divide-and-conquer approach. A linear classifier places a single decision surface through the entire space.


The two most common families of techniques that are based on fitting the parameters of complex, nonlinear functions are nonlineair SVMs and neural networks.


One can think of nueral networks as a "stack" of models


We could think of this very roughly as first creating a set of "experts" in different facets of the problem (the first-layer models), and then learning how to weight the opinions of these different experts (the second-layer model).


The tradeoff is that as we increase the amount of flexibility we have to fit the data, we increase the chance that we fit the data too well.


Linear modeling techniques incude traditional linear regression, and linear discriminants as SVMs.


Finding chance occurances in data that look like interesting patterns, but which do not generalize, is called overfitting the data


Generalization is the property of a model or modeling process, wherby the model applies to data that were not used to build the model


Overfitting is the tendency of data mining procedures to tailor models to the training data, at the expense of generalization to previously unseen data points


Generally, there will be more overfitting as one allows the model to be more complex.


We've discussed in the previous chapters two very different sorts of modeling procedures: recursive partitioning of the data as done for tree induction, and fitting a numeric model by finding an optimal set of parameters, for example the weights in a linear model.


A procedure that grows trees until the leaves are pure tend to overfit


But at some point the tree starts to overfit: it acquires details of the training set that are not characteristic of the population in general, as represented by the holdout set


Cross-validation is a more sophisticated holdout training and testing procedure.


Cross-validation begins by splitting a labeled dataset into k partitions called folds.


By this point you should know enough to mistrust any performance measurement done on the training set, because overfitting is a very real possibility


A plot of the generalization performance against the amount of training data is called a learning curve


The learning curve may show that generalization performance has leveld off so investing in more training data is probably not wortwhile; instead, one should accept the current perforamnce or look for another way to improve the model, such as by devising better features.


Complexity control: finding the "right" balance between fit to the data and the complexity of the model


Models will be better if they fit the data better, but they also will be better if they are simpler.


Do remember that regularization is trying to optimize not just the fit to the data, but a combination of fit to the data and simplicity of the model


This general approach to optimizing the parameter values of a data mining procedure is known as grid search


Data mining involves a fundamental trade-off between model complexity and the possiblity of overfitting. A conplex model may be necessary if the phenomonon producing the data is itself complex. but complex models run the risk of overfitting training data (ie modeling details of the dataset not found in the general population)


The best strategy is to recognize overfitting by testing with a holdout set


A learning curve show model performance on testing data plotted against the amount of training data used


A common experimental methodology called cross-validation specifies a systemic way of splitting up a dataset such that it generates multiple performance measures.


The general method for reining in model complexity to avoid overfitting is called model regularization.


Many methods in data science may be seen in this light: as methods for organizing the space of data instances (representations of important objects) so that instances near each other are treated similarly for some purpose.


This idea of dinding natural groupings in the data may be called unsupervised segmentation, or simply clustering.


Unsupervised modeling does not focus on a target variable. Instead it looks for other sorts of regularities in a set of data.


TFIDF (Term Frequency times Inverse Document Frequency) scores represent the frequency of the word in the document, penalized by the frequency of the word in the corpus


It is a commonly used in text applications to measure the similarity of documents


It is useful to think of a positive example as one worthy of attention or alarm, and a negative example as uninteresting


Classification accuracy is a popular metric because it's very easy to measure. Unfortunately, it is usually to simplistic for applications of data mining techniques to real business problems.


A confusion matrix for a problem involving n classes is a n x n matrix with the columns labeled with actual classes and the rows labeled with predicted classes.


The error of the classifier are the false positives (negative instances classed as positive) and false negatives (positives classified as negative).


Unfortunately, as the class distribution becomes more skewed, evaluation based on accuracy breaks down.


Another problem with simple classification accuracy as a metric is that it makes no distinction between false positive and false negative errors. By counting them together, it makes the tacit assumption that both errors are equally important. With real-world domains this is rarely the case. These are typically very different kind of errors with very different costs because the classifications have consequences of different severity.


Ideally, we should estimate the cost or benefit to each decision a classifier can make. Once, aggregated, these will produce an expected profit (or expected benefit or expected cost) estimate for the classifier.


True positive rate: TP/(TP+FN)


False negative rate: FN/(TP+FN)


Consider carefully what is desired from the data mining results. Maximizing simple prediction accuracy is usally not an appropriate goal.


The expected value calculation is a good framework for organizing this thinking. It will help to frame the evaluation, and in the event that the final deployed model produces unacceptable results, it will help identify what is