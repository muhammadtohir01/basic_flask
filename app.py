from flask import Flask

app = Flask(__name__)

@app.route('/about')
def hello_world():
    return "№ 1.\
Manba: “Elektr zanjirlar nazariyasi” A.A. Tulyaganov, S.S. Parsiyev, V.A. Tulyaganova, A.M. Abdullayev. 2018.\
Qiyinlik darajasi– 1\
Elektr zanjirda tok kuchining o‘lchov birligi nimada o‘lchanadi?\
Amper\
Volt\
Vatt\
Om\
№ 2.\
Manba: “Elektronika” X.K. Aripov, A.M. Abdullayev, N.B. Alimova, X.X. Bustanov, Ye.V. Obyedkov, Sh.T. Toshmatov. 2011.\
Qiyinlik darajasi – 1\
Ikkita p-n o‘tishga va uchta elektrodga ega bo‘lgan, signallarni tok, kuchlanish va quvvat bo‘yicha kuchaytiruvchi yarimo‘tkazgichli asbob qanday ataladi?\
bipolyar tranzistor\
unipolyar tranzistor\
Diod\
stablitron\
\
№ 3.\
Manba: “Elektronika” X.K. Aripov, A.M. Abdullayev, N.B. Alimova, X.X. Bustanov, Ye.V. Obyedkov, Sh.T. Toshmatov. 2011.\
Qiyinlik darajasi – 1\
Yuqori va o‘ta yuqori chastotali qurilmalarda ishlatish uchun mo‘ljallangan diodlar qanday nomlanadi?\
yuqori chastotali diodlar\
to‘g‘rilovchi diodlar\
impulsli diodlar\
tunelli diodlar\
"
if __name__ == '__main__':
    # Run the app in local network
    app.run()