from modules.sw import univ_ratio
from modules.identify_email import Send_Email
from flask import Flask, request, redirect, render_template, url_for

sched = BackgroundScheduler()


app = Flask(__name__, static_url_path='/static')

@sched.scheduled_job('cron', minute='*/10', id='univ_ratio_check')
def univ_ratio_check():
    #10분 간격으로 메일 송신 호출
    current_time = time.strftime("%H:%M:00")
    print(current_time)
    univ_ratio("대학경쟁률 실시간 조회(학교별로 업데이트 시간이 달라요!)")


sched.start()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=False, port=FLASK_ENUM.PORT)