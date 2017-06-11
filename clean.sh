
#redis-cli -h ubuntu02 -a Hc10086cn/ keys "SinaSpider:dupefilter*"|xargs redis-cli -h ubuntu02 -a Hc10086cn/ del
#redis-cli -h ubuntu02 -a Hc10086cn/ keys "SinaSpider:dupefilter*"|xargs redis-cli -h ubuntu02 -a Hc10086cn/ del
#redis-cli -h ubuntu02 -a Hc10086cn/ del "SinaSpider:dupefilter251263"


ps -ef|grep launch.py|grep -v grep|cut -c 7-12|xargs kill -9
ps -ef|grep scrapy|grep -v grep|cut -c 7-12|xargs kill -9
ps -ef|grep phantomjs|grep -v grep|cut -c 7-12|xargs kill -9
ps -ef|grep python|grep -v grep|cut -c 7-12|xargs kill -9

