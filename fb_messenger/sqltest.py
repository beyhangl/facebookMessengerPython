# -*- coding: utf-8 -*-


import MySQLdb
from pprint import pprint
from fbmq import Page
import fbmq
from fbmq import Attachment, Template, QuickReply, Page



def letsinsert (userid,text,seq):
   
 db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="mysql",  # your password
                     db="facebook")        # name of the data base

 cur = db.cursor()
 db.autocommit(True)

# Use all the SQL you like
 if str(userid) !='XXX':
   pprint("insert into talks (userid,text,seq) values ('"+str(userid).encode("utf-8")+"','"+str(text).encode("utf-8")+"','"+str(seq).encode("utf-8")+"')")
   cur.execute("insert into talks (userid,text,seq) values ('"+str(userid).encode("utf-8")+"','"+str(text).encode("utf-8")+"','"+str(seq).encode("utf-8")+"')")
   cur.execute("commit")

   cur.execute("select text from talks where ID =(select max(ID) from talks )")
   data = cur.fetchall()
   for row in data :
     last_talk=str(row[0])
   pprint(last_talk)
   page = fbmq.Page('XXX')

   evet_hayir = [QuickReply(title="Evet", payload="PICK_ACTION"),QuickReply(title="Hayir", payload="PICK_COMEDY")]
   bagis = [QuickReply(title="XXX", payload="PICK_ACTION"),QuickReply(title="XXX", payload="PICK_COMEDY"),QuickReply(title="XXX", payload="PICK_COMEDY")]
   #pprint("insert into talks (userid,text,seq) values ('"+str(userid).encode("utf-8")+"','"+str(text).encode("utf-8")+"','"+str(seq).encode("utf-8")+"')")
   #cur.execute("insert into talks (userid,text,seq) values ('"+str(userid).encode("utf-8")+"','"+str(text).encode("utf-8")+"','"+str(seq).encode("utf-8")+"')")
   #cur.execute("commit")
   cur.close ()

   if last_talk=='evet' or last_talk=='Evet':
       page.send('XX', 

          "XXXX!",

          quick_replies=bagis,

          metadata="DEVELOPER_DEFINED_METADATA")

   elif last_talk=='XXX' or last_talk=='XXX' or last_talk=='XX':
        page.send('XX', str(last_talk) +"' XXX!")

   elif last_talk.isdigit() and len(str(last_talk))== 10:
        page.send('XX',  "XXXX!")

   elif last_talk.isdigit() and len(str(last_talk))== 5:
        page.send('XX',  "XXX")
   elif last_talk=='meraba' or last_talk=='selam' or last_talk=='Merhaba' or last_talk=='XX' or last_talk=='XX' or  last_talk=='merhaba' or last_talk=='hey' or last_talk=='Hey' or last_talk=='Selam':
        page.send('XX', 

          "XX XXX XX XX XXX  ?",

          quick_replies=evet_hayir,

          metadata="DEVELOPER_DEFINED_METADATA")
   else :
    page.send('XX',  "XX XX ,X XX XX XX ? ")
  

# print all the first cell of all the rows

#for row in cur.fetchall():

#    print row[0]


 db.commit()
 db.close()


