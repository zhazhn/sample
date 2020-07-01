start_time=67.30
end_time=124.89
hour=int(start_time/60/60)
min=int(start_time/60)-hour*60
sec=int(start_time)-min*60-hour*60*60
msec=int((start_time-sec)*1000) 
msec=int((start_time-int(start_time))*1000)

e_hour=int(end_time/60/60)
e_min=int(end_time/60)-e_hour*60
e_sec=int(end_time)-e_min*60-e_hour*60*60
e_msec=int((end_time-e_sec)*1000)
e_msec=int((end_time-int(end_time))*1000)


msg1='{}:{}:{},{} --> {}:{}:{},{}'.format(hour,min,sec,msec, e_hour,e_min,e_sec,e_msec)+'\n'
print(msg1)

print(int(end_time))