from flask import Flask, request, render_template
import os
import json
import read_app

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods = ['GET', 'POST'])

def upload_file():
   if request.method == 'GET':
      return render_template('upload.html')
   
   if request.method == 'POST':
      f = request.files['file']
      f_name = f.filename
      if f_name!='':

         if '.txt' not in f_name and '.docx' not in f_name and '.pdf' not in f_name:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Please Upload text/word/pdf file only"}

            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

         else: 
            f_name = "./upload/"+f_name
            f.save(f_name)
            
            read_app.read_app(f_name)
            return render_template('play.html')

            # status= 200
            # response_type = 'application/json'
            # result= {"Status":"File Uploaded Successfully"}

            # response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            # return response
      
      else:
         status= 400
         response_type = 'application/json'
         result= {"Status":"Please upload any file"}

         response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
         return response

if __name__ == '__main__':
   app.run(debug=True)
   