from flask import Flask, app, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__,template_folder='template')
dic = {0: 'cat', 1: 'dog'}

model = load_model('C:/Users/Shah/Desktop/MAIN APP/model.h5')

model.make_predict_function()

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(100,100))
    i - image.img_to_array(i)/255.0
    #i = i.reshape(1, 100,100,4)
    p = model.predict_classes(i)
    return dic[p[0]]

#routes 
@app.route("/", methods= ['GET','POST'])
def index():
    return render_template('index.html')

#@app.route("/about")
#def about():
    #return "Please Forward the link @usamathesyed"

@app.route("/submit", methods=['GET', 'POST'])
def get_hours():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "C:/Users/Shah/Desktop/MAIN APP/static/" + img.filename
        img.save(img_path)

        p = predict_label(img_path)
    
    return render_template("index.html", prediction = p, img_path = img_path)

if __name__=='__main__':
    #app.debug=True
    app.run(debug= True)
