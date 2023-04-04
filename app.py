from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
# def hello_world():
#     r=request.args
#     name=r['name']
#     data={
#         'apple':2,
#         'banana':4,
#         'ananas':1
#     }
#     return {name:data.get(name,'not fonud')}
@app.route('/get_sum')
    
def sum():
    r=request.args
    s=0
    a=int(r['a'])
    b=int(r['b'])
    s=a+b
    print(type(s))
    return {'summa':s}
if __name__ == '__main__':
    # Run the app in local network
    app.run()