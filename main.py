import mysql.connector
import smtplib
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election"
)
mycursor = mydb.cursor()


insert_vote_sql = "INSERT INTO election_result (voter_id, dmk, admk, bjp, nota) VALUES (%s, %s, %s, %s, %s)"
check_voter_sql = "SELECT voter_id FROM election_result WHERE voter_id = %s"

def check_voter(voter_id):
    mycursor.execute(check_voter_sql, (voter_id,))
    return mycursor.fetchone() 

def save_vote(voter_id, dmk, admk, bjp, nota):
    val = (voter_id, dmk, admk, bjp, nota)
    mycursor.execute(insert_vote_sql, val)
    mydb.commit()

try:
    voter_id = int(input("Enter your voter ID: "))

    if check_voter(voter_id):
        print("Already voted")
    else:
        print("Vote accepted")
        print("Press 1 to vote for DMK")
     
        print("Press 2 to vote for ADMK")
        print("Press 3 to vote for BJP")
        print("Press 4 to vote for NOTA")
        
        vote = int(input("Enter your choice: "))
        
        dmk, admk, bjp, nota = 0, 0, 0, 0
        
        if vote == 1:
            dmk = 1
            print("Your vote for DMK has been saved successfully")
        elif vote == 2:
            admk = 1
            print("Your vote for ADMK has been saved successfully")
        elif vote == 3:
            bjp = 1
            print("Your vote for BJP has been saved successfully")
        elif vote == 4:
            nota = 1
            print("Your vote for NOTA has been saved successfully")
        else:
            print("Invalid choice")
        
        save_vote(voter_id, dmk, admk, bjp, nota)
        print("Data saved successfully")
    

    def emailsending():
         try:
          receiver_mails=["lokeshwaribhavani3@gmail.com"]
          for i in receiver_mails:
           f=open("vote.txt","r")
           txt=f.read()
           print(i,txt)
           s=smtplib.SMTP('smtp.gmail.com',587)
           s.starttls()
           s.login("sangavis831@gmail.com","nmlv cxqv pffu trho")
           message=(f" {txt}\n\nthank you for voting!")
           s.sendmail("sangavis831@gmail.com",i,message)
           s.quit()
           print("mail sent sucessfully")
         except:
           print("not sent")
    emailsending() 

except ValueError:
    print("Please enter numerical values")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    mycursor.close()
    mydb.close()
