from flask import *
import requests,json

app = Flask(__name__)
jokers=[]
@app.route('/')
def index():
    url= "https://api.nasa.gov/planetary/apod?api_key=Bc5NBuLFFz7JVcwLlQWB8URnkqOEFAPePtyRfxzf"
    r= requests.get(url)
    data = json.loads(r.text)
    title= data["title"]
    date =data["date"]
    image =data["hdurl"]
    story=data['explanation']
    return render_template("home.html", title=title, date=date, image=image, story=story )



if __name__ == '__main__':
    app.run()