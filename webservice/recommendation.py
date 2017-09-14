from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql import SparkSession
from pyspark.mllib.recommendation import ALS,MatrixFactorizationModel,Rating
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.evaluation import RegressionEvaluator
from math import sqrt


print "started"
#filename="/home/super/Desktop/data/ml-100k/u.data"
filename="/home/naresh.srikakulapu/work/u.data"

model=None
def train(filename):
    global model
    sc=SparkContext.getOrCreate()
    user = sc.textFile(filename)

    ratings=user.map(lambda l:l.split("\t")).map(lambda l:Rating(int(l[0]),int(l[1]),float(l[2])))
    #split into training & test 
    (training, test) = ratings.randomSplit([0.8, 0.2])
    testdata = test.map(lambda p: (p[0], p[1]))
    rank = 10
    numIterations = 10

    #training the model
    model = ALS.train(training, rank, numIterations)

    #validating the model
    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = test.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
    rmse = sqrt(MSE)
    print rmse 
    print "training done"  
    return "OK"







def recommend(userid):
    
    resultstr="products:"
    print "recommend rec ",userid
    recommedItemsToUsers = model.recommendProductsForUsers(userid)
    
    
    result=recommedItemsToUsers.lookup(userid)
    resulttup=result[0]
    
    for result in resulttup:
        resultstr=resultstr+" "+str(result.product)
        
    print resultstr, "result str"
    return resultstr   
