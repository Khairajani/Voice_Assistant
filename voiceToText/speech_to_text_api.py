from flask import Flask, request, render_template
import os
import re
import json
import mail_app

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("app.html")

    if request.method == "POST":
        f = request.files['audio_data']
        f_name = f.filename
        if f_name!='':
            f_name = "./upload/"+f_name+".wav"
            with open(f_name, 'wb') as audio:
                f.save(audio)
            print('file uploaded successfully')
            
            return render_template('app.html') #, request="POST")
            #     return render_template('index.html', request="POST")
            # else:
            #     return render_template("index.html")

            # response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            # return response

@app.route("/mail", methods=['GET', 'POST'])
def mail():
    if request.method == "POST":
        mailId = request.form['mailId']
        if mailId:
            if os.path.isfile("./upload/subject.wav") and os.path.isfile("./upload/body.wav"):
                
                subject_path = "./upload/subject.wav"
                body_path = "./upload/body.wav"
                res = mail_app.mail_app(subject_path,body_path,mailId)

                status= 200
                response_type = 'application/json'
                result= {"Status":res}
                response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
                try:
                    os.remove("./upload/subject.wav")
                    os.remove("./upload/body.wav")
                except:
                    pass

                return response
            
            elif os.path.isfile("./upload/subject.wav"):
                status= 400
                response_type = 'application/json'
                result= {"Status":"Failed",'Response':'Body not found'}
                response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
                return response
            
            elif os.path.isfile("./upload/body.wav"):        
                status= 400
                response_type = 'application/json'
                result= {"Status":"Failed",'Response':'Subject not found'}
                response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
                return response
            
            else:    
                status= 400
                response_type = 'application/json'
                result= {"Status":"Failed",'Response':'Subject and Body not found'}
                response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
                return response                

        else:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Failed",'Response':'Recipients Email not found'}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response


if __name__ == "__main__":
    app.run(port=5001,debug=True)
    #app.run(host='0.0.0.0', port=6850, debug=True)