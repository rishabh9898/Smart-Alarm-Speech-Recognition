import datefinder
import winsound
import datetime

def alarm(text):
	Date_Time_Alarm=datefinder.find_dates(text)
	for match in Date_Time_Alarm:
		print(match)
	StringAlarm=str(match)
	TimeAlarm=StringAlarm[11:]
	print(TimeAlarm)
	HourAlarm=int(TimeAlarm[:-6])
	MinAlarm=int(TimeAlarm[3:-3])

	while True:
		if HourAlarm==datetime.datetime.now().hour:
			if MinAlarm==datetime.datetime.now().minute:
				print("Alarm is running")
				winsound.PlaySound("C:\\Users\\ruhel\\Downloads\\Never Gonna Give You Up Original.mp3",winsound.SND_LOOP)
			elif MinAlarm>datetime.datetime.now().minute:
				break






	print(HourAlarm)
	print(MinAlarm)


alarm("Set Alarm at 6:35 pm ")


