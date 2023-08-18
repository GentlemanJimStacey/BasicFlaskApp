from flask import Flask,jsonify,request
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello there!"

@app.route('/version', methods = ['GET'])
def version():
    if(request.method == 'GET'):
        data = {
            "App Version" : "v1.0"
        }

        return jsonify(data)

@app.route("/is_prime")
def primeCheck():
    PRIME_HTML = """
     <html><body>
         <h1>Prime!</h1>.
     </body></html>"""
    NOTPRIME_HTML = """
     <html><body>
         <h1>Not Prime!</h1>.
      </body></html>"""
    stringNum = request.args['number']
    num = int(stringNum)
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return NOTPRIME_HTML.format(num)
                break
        else:
            return PRIME_HTML.format(num)
    else:
        return NOTPRIME_HTML.format(num)

@app.route('/weather', methods = ['GET'])
def weather():
    if(request.method == 'GET'):
        zipCode = request.args['zip']
        url = f"https://api.openweathermap.org/data/2.5/weather?zip="+zipCode+",us&appid=b21a2633ddaac750a77524f91fe104e7"
        r = requests.get(url).json()
        return r

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
