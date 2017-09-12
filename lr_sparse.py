#!/usr/bin/python 
import time
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.datasets import load_svmlight_file
from sklearn import metrics

def validation(trainfile, testfile,resultfile='', _C=1.0, _penalty='l2', _tol=0.0001,_class_weight='balanced'):
	print _C
	print 'Load training data...'
	#trainfile = open(trainfile)
	train_x,train_y = load_svmlight_file(trainfile)

	print 'Train data size=',train_x.shape
	print 'Load test data...'
	testfile = open(testfile)
	test_x,test_y = load_svmlight_file(testfile)
	#test_y = testdata[:,0]
	#test_len = test_x.shape[0]
	#print 'Test data size=',test_len
	
	print 'Normalization...'
	minmax_scaler = preprocessing.MaxAbsScaler()
	normed_train_x = minmax_scaler.fit_transform(train_x)
	normed_test_x = minmax_scaler.transform(test_x)
	
	#smaller C means stronger regularization
	print 'Model training...'
	time1 = time.time()
	lr = LogisticRegression(C=_C,penalty=_penalty,tol=_tol)
	lr.fit(normed_train_x,train_y)
	time2 = time.time() - time1
	print 'training time:'+str(time2)
	
	print 'Weight'
	outfile = open('weight.txt','w')
	print len(lr.coef_[0])
	for item in lr.coef_[0]:
		outfile.write(str(item)+'\n')

	#parameters = lr.get_params(deep=True)
	#print parameters
	#out = open('../casetudy/weights')
	
	print 'Predict...'
	
	pred_y = lr.predict(normed_test_x)
	test_len = len(pred_y)
	print test_len
	'''if resultfile!='':
		outfile = open(resultfile,'w')
		for i in range(test_len):
			outfile.write(str(int(test_y[i]))+','+str(int(pred_y[i]))+'\n')	
		outfile.close()	
		return'''
	
	print 'Get precision,recall and f-score...'
	p_1 = metrics.precision_score(test_y,pred_y,pos_label=1)
	r_1 = metrics.recall_score(test_y,pred_y,pos_label=1)
	f_1 = 0.65*p_1+0.35*r_1
	print 'spam:','p=',p_1,'r=',r_1,'f=',f_1
	
	p_0 = metrics.precision_score(test_y,pred_y,pos_label=0)
	r_0 = metrics.recall_score(test_y,pred_y,pos_label=0)
	f_0 = 0.65*p_0+0.35*r_0
	print 'norm:','p=',p_0,'r=',r_0,'f=',f_0
	
	
	score = 0.7*f_1+0.3*f_0
	print "Score = ",score


