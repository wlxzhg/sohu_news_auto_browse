import os
import time
import random

# //阅读新闻点击位置
TAP_X = 500
TAP_Y = 800

# //返回点击位置
RET_X = 100
RET_Y = 100

# //滑动起始位置
SWIPE_START_X = 1000
SWIPE_START_Y = 1700
SWIPE_END_X = 1000
SWIPE_END_Y = 700

# //阅读新闻篇数
NEWS_NUM = 30
# //翻看页数
PAGES = 7
# //每屏停留时间 (秒)
LOOK_TIME = 10
#操作等待时间（秒）
SLEEP_TIME = 2 

#分享次数
SHARE_NUM = 5
#分享-坐标
#文章分享按钮
X1 = 989;Y1=1854;
#微信分享位置
X2 = 100;Y2=1250;
#文件助手
X3 = 265; Y3 = 837;
#最后分享
X4 = 810; Y4 = 1324;
#返回搜狐新闻
X5 = 600; Y5 = 1150;

def main():
	times = SHARE_NUM;
	while times > 0:

		times = times - 1
		print("开始分享第",SHARE_NUM - times,"篇新闻");

		os.system('adb shell input tap %d %d' % (TAP_X,TAP_Y)); #点击新闻
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input tap %d %d' % (X1,Y1)); #点击分享
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input tap %d %d' % (X2,Y2)); #选择微信分享
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input tap %d %d' % (X3,Y3)); #文件助手
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input tap %d %d' % (X4,Y4)); #分享
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input tap %d %d' % (X5,Y5)); #返回搜狐新闻
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input tap %d %d' % (RET_X,RET_Y)); #返回
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));

		os.system('adb shell input swipe %d %d %d %d' % (SWIPE_START_X,SWIPE_START_Y,SWIPE_END_X,SWIPE_END_Y)); #翻页
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));
		pass

	times = NEWS_NUM;
	while times > 0:
		times = times - 1;
		os.system('adb shell input tap %d %d' % (TAP_X,TAP_Y)); #点击新闻
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));
		print("点击第",(NEWS_NUM - times),"篇新闻");
		page = PAGES;
		while page > 0:
			page = page - 1;
			print("浏览第",(NEWS_NUM-times),"篇新闻的第",(PAGES-page),"页");
			time.sleep(random.uniform(LOOK_TIME-2,LOOK_TIME+2));
			#下滑翻页
			os.system('adb shell input swipe %d %d %d %d' % (SWIPE_START_X,SWIPE_START_Y,SWIPE_END_X,SWIPE_END_Y)); 
		print("点击返回");
		os.system('adb shell input tap %d %d' % (RET_X,RET_Y)); #返回
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));
		os.system('adb shell input swipe %d %d %d %d' % (SWIPE_START_X,SWIPE_START_Y,SWIPE_END_X,SWIPE_END_Y)); #翻页
		time.sleep(random.uniform(SLEEP_TIME - 0.5,SLEEP_TIME + 0.5));
		
if __name__ == '__main__':
	main()
