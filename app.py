from flask import Flask, request, render_template
import os
import requests, json

global translator_endpoint    
global cog_key    
global cog_region

from dotenv import load_dotenv


app= Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')

try:
    load_dotenv()
    cog_key = os.environ.get("COG_SERVICE_KEY")
    cog_region = os.environ.get("COG_SERVICE_REGION")      
    translator_endpoint = 'https://api.cognitive.microsofttranslator.com'   
except Exception as ex:        
    print(ex)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #text = request.form['text']
        #Aquí es donde procesarías el texto. Por ahora, solo devolvemos el mismo texto.
        #source_language = ''
        #translated_text = text
        #source_language = 'en'    
        ##Use the Translator detect function    
        #path = '/detect'    
        #url = translator_endpoint + path    
        ## Build the request    
        #params = {        
        #    'api-version': '3.0'    }    
        #headers = {    
        #    'Ocp-Apim-Subscription-Key': cog_key,    
        #    'Ocp-Apim-Subscription-Region': cog_region,    
        #    'Content-type': 'application/json'    }    
        #body = [{        
        #    'text': text    
        #    }]    
        ## Send the request and get response    
        #request = requests.post(url, params=params, headers=headers, json=body)    
        #response = request.json()    
        ## Parse JSON array and get language    
        #source_language = response[0]["language"]    
        #translated_text = text
        ##Hasta aqui cambié para fuente
        #return render_template('index.html', translated_text=translated_text,lang_detected=source_language)  
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
