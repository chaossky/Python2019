#-*- coding: utf-8 -*- 
from datetime import datetime

file=open('dataset_gg.txt','w')
#dataset=['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']
# dataset=['개포동','논현동','대치동','도곡동','삼성동','세곡동','수서동','신사동','압구정동','역삼동','율현동','일원동','자곡동','청담동']
#dataset=['강일동','고덕동','길동','둔촌동','명일동','상일동','성내동','암사동','천호동']
#dataset=['미아동','번동','수유동','우이동']
#dataset=['가양동','개화동','공항동','과해동','내발산동','등촌동','마곡동','방화동','염창동','오곡동','오쇠동','외발산동','화곡동']
#dataset=['남현동','봉천동','신림동']
#dataset=['광장동','구의동','군자동','능동','자양동','중곡동','화양동']
#dataset=['가리봉동','개봉동','고척동','구로동','궁동','신도림동','오류동','온수동','천왕동','항동']
#dataset=['가산동','독산동','시흥동']
#dataset=['공릉동','상계동','월계동','중계동','하계동']
#dataset=['도봉동','방학동','쌍문동','창동']
#dataset=['답십리동','신설동','용두동','이문동','장안동','전농동','제기동','청량리동','회기동','휘경동']
#dataset=['노량진동','대방동','동작동','본동','사당동','상도1동','상도동','신대방동','흑석동']
#dataset=['공덕동','구수동','노고산동','당인동','대흥동','도화동','동교동','마포동','망원동','상수동','상암동','서교동','성산동','신공덕동','신수동','신정동','아현동','연남동','염리동','용강동','중동','창전동','토정동','하중동','합정동','현석동']
#dataset=['남가좌동','냉천동','대신동','대현동','미근동','봉원동','북가좌동','북아현동','신촌동','연희동','영천동','옥천동','창천동','천연동','충정로2가','충정로3가','합동','현저동','홍은동','홍제동']
#dataset=['내곡동','반포동','방배동','서초동','신원동','양재동','우면동','잠원동']
#dataset=['금호동1가','금호동2가','금호동3가','금호동3가','도선동','마장동','사근동','상왕십리동','성수동1가','성수동2가','송정동','옥수동','용답동','응봉동','하왕십리동','행당동','홍익동']
#dataset=['길음동','돈암동','동선동1가','동선동2가','동선동3가','동선동4가','동선동5가','동소문동1가','동소문동2가','동소문동3가','동소문동4기','동소문동5가','동소문동6가','동소문동7가','보문동1가','보문동2가','보문동3가','보문동4가','보문동5가','보문동6가','보문동7가','삼선동1가','삼선동2가','삼선동3가','삼선동4가','삼선동5가','상월곡동','석관동','성북동','성북동1가','안암동1가','안암동2가','안암동3가','안암동4가','안암동5가','장위동','정릉동','종암동','하월곡동']
dataset=['가락동','거여동','마천동','문정동','방이동','삼전동','석촌동','송파동','신천동','오금동','잠실동','장지동','풍납동']
length_001=len(dataset)
for i in range(length_001):
    str=dataset[i]+"과외\n"
    file.write(str)

for i in range(length_001):
    str=dataset[i]+"영어과외\n"
    file.write(str)

for i in range(length_001):
    str=dataset[i]+"수학과외\n"
    file.write(str)

for i in range(length_001):
    str=dataset[i]+"국어과외\n"
    file.write(str)

file.close()
now=datetime.now()
print ("%s.%s.%s - %s:%s" %(now.year, now.month, now.day, now.hour, now.minute))