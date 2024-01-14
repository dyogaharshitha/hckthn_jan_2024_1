"""
The api return sequence of numbers upto the specified limit and replaces multiples of int1, int2 and int18int2 with
str1, str2 and str1str2 respectively

***
	The time complexity is
	O(limit/n) if n= int1 if int1 < int2 else int2
	Algorithm uses dynamic programming while replacing the sequence with
	selected string
 ***

 this api has four endpoints home page , generate sequence , statistics of server, stop server
"""
import signal
from datetime import datetime
from collections import Counter

import flask
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import os
app = Flask(__name__)
api = Api(app)

#global logger
_log_stat_ = {'dateandtime': [], 'query': []}

# to generate desired sequence add five parameters int1, int2, limit, str1,str2
#  to the url
class Sequence(Resource):
	def get(self):
		dt = request.args.to_dict()
		int1 = int(dt["int1"]) ; int2 = int(dt["int2"]) ; limit = int(dt["limit"])
		str1 = dt["str1"] ; str2 = dt["str2"]
		_log_stat_['dateandtime'].append(datetime.now())
		_log_stat_['query'].append("int1"+str(int1)+"int2"+str(int2)+"limit"+str(limit)+" "+str1+str2)
		seqnc = range(limit+1) ; seqnc= list(seqnc)

		s = str1 + str2 ;
		if int1 < int2:
			itr = limit // int1; skp = int2 // int1 ;
			s1= str1 ; s2 = str2; i1 = int1 ; i2 = int2 ;  itr2 = limit//int2
		else:
			itr = limit // int2 ; skp = int1 // int2 ; itr2 = limit // int1
			s1 = str2 ; s2 = str1; i1 = int2 ; i2 = int1 ;
		for i in range(1, itr+1):
			seqnc[i*i1] = s1
			if i%skp == 0 and i//skp <= itr2  :
				seqnc[(i//skp) *i2] = s2
			if i % i2 ==0:
				seqnc[i*i1] = s ;
		return jsonify({'data':seqnc[1:]})

class stat(Resource):
	def get(self):
		if _log_stat_['query'] == []:
			return "no queries yet"
		cntr = Counter(_log_stat_['query'])
		cmmn = cntr.most_common(1)
		return jsonify(({'most coomon qury and count':cmmn}))

class stpsrvr(Resource):
	def get(self):
		os.kill(os.getpid(), signal.SIGINT)
# on the terminal type: curl http://127.0.0.1:5000/
# returns url format for api when we use GET.
# returns the data that we send when we use POST.
class hme(Resource):
	def get(self):
		return  "query in the format /seq?int1&int2&limit&str1&str2"

api.add_resource(stat, '/stat')
api.add_resource(Sequence,'/seq')
api.add_resource(stpsrvr,'/stop')
api.add_resource(hme, '/', endpoint='hme')

#if __name__ == '__main__':

	#app.run(debug = True)
