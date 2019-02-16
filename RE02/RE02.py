#word1 = "The "
#word2 = "quick "
#word3 = "brown "
#word4 = "fox "
#word5 = "jumps "
#word6 = "over "
#word7 = "the "
#word8 = "lazy "
#word9 = "dog "
#print(word1+word2+word3+word4+word5+word6+word7+word8+word9)


#HTML
#h = input("What is the tag? ")
#text = input("What is the text? ")
#print("<" + h + ">" + text + "</" + h + ">")

#cast
#str_n = input("What is the number?")
#n=int(str_n)
#str_nn=str_n+str_n
#str_nnn=str_nn+str_n
#nn=int(str_nn)
#nnn=int(str_nnn)
#
#print(n+nn+nnn)

#INTERESTS
#str_P = input("How much is the principal amount? (P) ")
#str_r = input("What is the interest rate? (r) ")
#str_n = input("How many times per year do you pay the interest? (n) " )
#t = 2
#
#P=int(str_P)
#r=float(str_r)
#n=int(str_n)
#
#amount=P*(1+(r/n))**(n*t)
#
#print("Amount: ", amount)

#ALLARM
import datetime
now = datetime.datetime.today()
now_hour = now.hour
now_min = now.minute

delay_hour = 8     
delay_min = 30

alarm_hour = (now_hour + delay_hour) % 23
alarm_min = (now_min + delay_min) % 60

print('Now: ' + str(now_hour) + ':' + str(now_min))
print('Alarm: ' + str(alarm_hour) + ':' + str(alarm_min))








#conversion (to minutes)
#delay_total_min = delay_hour*60 + delay_min
#total_minutes = delay_total_min + now_hour*60 + now_min
#
#alarm_hour = total_minutes//60
#if alarm_hour>=24:
#    alarm_hour -= 24
#
#alarm_minute = total_minutes%60
#








