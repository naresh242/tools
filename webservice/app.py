import flask
import logging
import json
import os
import recommendation as rm
app = flask.Flask(__name__)
@app.route('/train', methods=['POST'])
def train():
    try:

        req = flask.request.get_json(silent=True, force=True)
        filename = req.get("filename")
        status=rm.train(filename)
        logging.info('train started')

        res={"status":status}
        res = json.dumps(res, indent=4)
        r = flask.make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r
    except Exception as err:
        logging.info('train failed: %s', err)
        res = {"status": "failed"}
        res = json.dumps(res, indent=4)
        r = flask.make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r
@app.route('/test', methods=['POST'])
def test():
    try:

        req = flask.request.get_json(silent=True, force=True)
        userid = req.get("userid")
	print int(userid)
	result=rm.recommend(int(userid))
	print "after rfecommend calling"	
        print result 

        logging.info('test started')

        res={
            "message":result
        }
        res = json.dumps(res, indent=4)
        r = flask.make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r
    except Exception as err:
        logging.info('test failed: %s', err)
        res={"message":"error"}
        res = json.dumps(res, indent=4)
        r = flask.make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
