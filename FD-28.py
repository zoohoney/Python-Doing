from flask import Flask
app = Flask(__name__)

@app.route("/") # @ <ㅡ 데코레이더 이해하기 
def hellow():
    return "플라스크 동작 확인!"

if __name__ == "__main__":
    app.run()
# 만약 Error: [Errno 98] Address already in use 에러 발생시 
# netstat -an | grep 5000
# sudo lsof -i :5000
# sudo kill -9 [PID] //[PID] 부분에 앞에 번호를 입력 하여 kill 하기
import tensorflow as tf
tf.__version__

