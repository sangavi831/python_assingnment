import mysql.connector
import datetime
import smtplib

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movies"
)

mycursor = mydb.cursor()


sql = "INSERT INTO booking ( movie_name,persons,shows_available,showdatetime, amount) VALUES (%s, %s,%s,%s,%s)"

try:
    
    
    movies = ["karudan","maharaja","premalu","kalki"]
    print(movies)
    movie_avail = input("Enter movie name to check availability: ")

    if movie_avail in movies:
        movie_name = movie_avail  
        if movie_avail=="karudan":
         print(f"your {movie_avail} is available")
         avail_shows=["3pm","6pm"]
         print(avail_shows)
         shows=input("enter your show timings:")
         if shows in avail_shows:
            print("your show timing is available")
            shows_available=shows
            cost_1 = 150
            no_of_persons=int(input("enter no.of.persons:"))
            persons=no_of_persons
            cost=cost_1*no_of_persons
            x=datetime.datetime.now()
            showdatetime=x
            gst_percentage = 6
            gst_amount = (cost * gst_percentage) / 100
            net_price = cost + gst_amount
            amount = net_price
            print("payment done")
        if movie_avail=="maharaja":
         print(f"your {movie_avail} is available")
         avail_shows=["11am","3pm","6pm"]
         print(avail_shows)
         shows=input("enter your show timings:")
         if shows in avail_shows:
            print("your show timing is available")
            shows_available=shows
            cost1 = 170
            no_of_persons=int(input("enter no.of.persons:"))
            persons=no_of_persons
            cost=cost1*no_of_persons
            gst_percentage = 6
            gst_amount = (cost * gst_percentage) / 100
            net_price = cost + gst_amount
            amount = net_price
            print("payment done")
            x=datetime.datetime.now()
            showdatetime=x
        if movie_avail=="premalu":
         print(f"your {movie_avail} is available")
         avail_shows=["6pm"]
         print(avail_shows)
         shows=input("enter your show timings:")
         if shows in avail_shows:
            print("your show timing is available")
            shows_available=shows
            cost1 = 110
            no_of_persons=int(input("enter no.of.persons:"))
            persons=no_of_persons
            cost=cost1*no_of_persons
            x=datetime.datetime.now()
            showdatetime=x
            gst_percentage = 6
            gst_amount = (cost * gst_percentage) / 100
            net_price = cost + gst_amount
            amount = net_price
            print("payment done")
        if movie_avail=="kalki":
         print(f"your {movie_avail} is available")
         avail_shows=["11pm","3pm","6pm","10pm"]
         print(avail_shows)
         shows=input("enter your show timings:")
         if shows in avail_shows:
           print("your show timing is available")
           shows_available=shows
           cost1 = 110
           no_of_persons=int(input("enter no.of.persons:"))
           persons=no_of_persons
           cost=cost1*no_of_persons
           x=datetime.datetime.now()
           showdatetime=x
           gst_percentage = 6
           gst_amount = (cost * gst_percentage) / 100
           net_price = cost + gst_amount
           amount = net_price
           print("payment done")
           
        def bill():
         f=open("bill.txt","w")
         f.write(f"{movie_name} is sucessfully booked on {shows_available} and the amount is {amount}\n\nthank you for booking!!\n\n on{showdatetime}")
         print("bill generating...")
         val = (movie_name,persons,shows_available,showdatetime, amount)
         mycursor.execute(sql, val)
         mydb.commit()  # 
         print("Data saved successfully")
        bill()
            
        def emailsending():
         try:
          receiver_mails=["lokeshwaribhavani3@gmail.com"]
          for i in receiver_mails:
           f=open("bill.txt","r")
          txt= f.read()
          print(i,txt)
          s=smtplib.SMTP('smtp.gmail.com',587)
          s.starttls()
          s.login("sangavis831@gmail.com","nmlv cxqv pffu trho")
          message=(f" {txt}\n\nthank you and visit again!")
          s.sendmail("sangavis831@gmail.com",i,message)
          s.quit()
          print("mail sent sucessfully")
         except:
           print("not sent")
        emailsending() 
    else:
        print("Movie not available. Data not saved.")

except:
    print("Invalid input. Please enter numeric values for ID.")
finally:
     mycursor.close()
     mydb.close()
