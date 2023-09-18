# 실시간 대학 경쟁률 체크 알림

<div>
  대학 원서 지원시 학과별 경쟁률을 체크하려면 진학사/유웨이 어플라이에서 조회해야합니다. <br>
  매번 어플라이에 들어가서 조회하는것이 귀찮아서 이를 자동화하고자 하였습니다. <br>
  리눅스 서버에서 Job Scedule을 이용하여 20분 간격으로 구동하였습니다. <br>
  학과별 경쟁률 정보는 Beautiful Soup를 이용하여 웹스클롤을 진행하였습니다. <br>
  Beautiful Soup를 처음 사용해봐서 코드를 매우 비효율적으로 작성하였습니다. 지원기간이 5일밖에 안되기에 효율적인 코드보다 기능에 우선을 두고 기능을 만들었습니다. <br>
  혹시 코드를 사용하실 분이 계실지는 모르겠지만 html_parser,find_all,for문 부분을 간단히 정리해보시길 바랍니다. <br>
  제발 대학 합격하길...<br>
</div>
<div><h2>Skill Stack</h2>
  <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/python-999999?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/nginx-00FF80?style=for-the-badge&logo=nginx&logoColor=black">
  <img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> 
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
</div>

<div><h2>편의사항</h2>
  기존의 리눅스 서버에서 tail -f nohup.out으로 결과를 볼 수 밖에 없어서 ssh 접속없이는 결과를 조회할 수 없었습니다. <br>
  그래서 생각해낸 방법이 webpage에서 정해진 시간당 redirect를 할까? 하고 생각하였지만, webhook과 같이 알림을 보내는것이 좋겠다고 생각하였습니다 <br>
  제일 좋은것은 카카오톡 알림톡 같이 보내는것이지만 카카오톡 알림톡은 비용도 비용이고 사업자가 있어야지만 가능하기에 학생수준에서는 불가능하였습니다. <br>
  이때 제한을 가장 덜 받는게 google mail을 이용하여 서비스를 제공하는것이 가장 좋겠다고 생각이 들었습니다. <br>
  아무래도 웹을 배우지 않았다보니 대형회사에서 구축한 서비스를 적절히 활용하는것이 좋다고 생각하였습니다. <br>
  이때문에 20분에 한번씩 SMTP를 이용하여 메일을 자동으로 보내주도록 설계하였습니다. <br>
  덕분에 밖에서 편하게 알림 수신이 가능합니다! <br>
</div>

<div><h2>Result</h2>
  <b>Webhook</b><br>
  <img width="300" alt="스크린샷 2023-09-18 오전 9 59 31" src="https://github.com/jangwonjun/jangwonjun/assets/41234293/4843c55d-a434-46fb-9ae1-4c6cd53ba858"> <br>
  <b>Email</b><br>
  <img width="450" alt="스크린샷 2023-09-18 오전 10 01 18" src="https://github.com/jangwonjun/jangwonjun/assets/41234293/2cb4b173-e681-43ce-838c-634f21b85105">
</div>
