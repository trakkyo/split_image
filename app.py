from flask import Flask, render_template, request
import os, sys, logging, urllib, shutil


app = Flask(__name__)

logging.basicConfig(filename='./logger.log', level=logging.DEBUG)

def _make_file_path(index):
    imgfilelist = []
    traintype = []
    relativepath = 'static/'
    filename = '{:0=6}'.format(index)

    for train in ['train_A', 'train_B']:
        filepath = os.path.join(relativepath, train, filename + '.jpg')
        if os.path.isfile(filepath):
            imgfilelist.append(os.path.join(relativepath, train, filename + '.jpg'))
            traintype.append(train)

    return imgfilelist, traintype

@app.route("/")
def root():
    count = 0
    imgfilelist, _ = _make_file_path(count)
    # subject to exist the first image
    if len(imgfilelist) == 0:
        return 'static/train_[A|B]/000000.jpg does not exist'

    return render_template("index.html", imgfilelist = imgfilelist, count = count)

@app.route("/next")
def test():
    res = urllib.parse.unquote(request.args.get('use_img'))
    type, count = res.split(',')

    imgfilelist, traintype = _make_file_path(int(count))
    if type == '1':
        # save file
        savepath = 'save/'
        for imgfile, type in zip(imgfilelist, traintype):
            shutil.copy(imgfile, os.path.join('savepath', type))

    imgfilelist, _ = _make_file_path(int(count) + 1)
    if len(imgfilelist) == 0:
        return 'Finished'

    return render_template("index.html", imgfilelist = imgfilelist, count = int(count) + 1)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
