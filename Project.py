from cProfile import label
from distutils.cmd import Command
from email.mime import image
import os
from re import L, U
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import random
import sqlite3
import tkinter



root = Tk()
root.title("Quiz Game")
#หน้าหลักหน้าแรก
def Homepage():
    Canvas(root,height=600,width=500)
    bg3_label =Label(root,image=pic_three)
    bg3_label.place(x=0,y=0)

    #ใส่ข้อความในหน้าจอ *fg คือสีข้อความ *bg คือสีพื้นหลังข้อความ
    mylabel1 = Label(root,text=" Welcome to Quiz Game ",fg="black",font=20).place(x=125,y=100)

    
#เข้าสู่ระบบ
    def four():
        
        Canvas(root,height=600,width=500)
        bg1_label =Label(root,image=pic_one)
        bg1_label.place(x=0,y=0)
        
        Label(root,text="Username").place(x=20,y=20)
        Label(root,text="Password").place(x=20,y=70)

        text1 = StringVar()
        text2 = StringVar()

        entry1=Entry(root,bd=5,textvariable=text1)
        entry1.place(x=140,y=20)
            
        entry2=Entry(root,bd=5,textvariable=text2)
        entry2.place(x=140,y=70)

        



        def login():
            global username
            username=text1.get()
            password=text2.get()
            conn=sqlite3.connect(r"C:\Users\ACER\Desktop\python\python\pythontest.db")
            c=conn.cursor()
            c.execute(' SELECT * FROM TEST WHERE username=? and password=? ',(username,password))
            collect = c.fetchall()
            conn.commit()
            
            if len(collect) == 0:
                z=tkinter.messagebox.showerror("Error","Please enter no more than 10 characters.")

               
            elif len(collect) == 1:
                z=tkinter.messagebox.showinfo("Save","We have saved the systems")
                beforestart()
                                                                                 
        #หน้าที่เป็นคำถาม
        def  beforestart():            
            boxscore = []
            
            #def six_Starwar():
            def question1():
                lable1 = Label( root,image=pic_five).place(x=0,y=0) 
                QA1 = Label(root,text="1.ใครเป็นผู้บงการให้ฝั่งสหพันธ์การค้าโจมตีดาว Naboo ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question2()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question2()
                ANS1 = Button(root,text="1.Darth Sidious",command=Score_quizgame).place(x=150,y=200)
                ANS2 = Button(root,text="2.Darth Tyranus",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Darth Vader",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Darth Ravan",command=Score_quizgame2).place(x=400,y=250)
            def question2():
                lable2 = Label( root,image=pic_five).place(x=0,y=0) 
                QA2 = Label(root,text="2.ใครคืออาจารย์ของ Obi-Wan Kenobi ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question3()                        
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question3()                        
                ANS1 = Button(root,text="1.Count Dooku",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Master Yoda",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Qui-Gon Jinn",command=Score_quizgame).place(x=150,y=250)
                ANS4 = Button(root,text="4.Asoka Tano",command=Score_quizgame2).place(x=400,y=250)
            def question3():
                lable3 = Label( root,image=pic_five).place(x=0,y=0) 
                QA3 = Label(root,text="3.นักล่าค่าหัวที่ Darth Sidious จ้างมาเพื่อสังหาร Padmé Amidala คือใคร ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question4()                        
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question4()                        
                ANS1 = Button(root,text="1.boba fett",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Geff kaga",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Boss",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Jango Fett",command=Score_quizgame).place(x=400,y=250)
            def question4():
                lable4 = Label( root,image=pic_five).place(x=0,y=0) 
                QA4 = Label(root,text="4.กองทัพทหารโคลนถูกสร้างขึ้นที่ดางดวงใด ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question5()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question5()
                ANS1 = Button(root,text="1.coruscant ",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Baboo",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Kamino",command=Score_quizgame).place(x=150,y=250)
                ANS4 = Button(root,text="4.Exegol",command=Score_quizgame2).place(x=400,y=250)
            def question5():
                lable5 = Label( root,image=pic_five).place(x=0,y=0) 
                QA5 = Label(root,text="5.หนังภาคแรกที่ฉายของ Star wars คือภาคที่เท่าไหร่ ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question6()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question6()
                ANS1 = Button(root,text="1.ภาค 1",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.ภาค 4",command=Score_quizgame).place(x=400,y=200)
                ANS3 = Button(root,text="3.ภาค 7",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.ภาค 2",command=Score_quizgame2).place(x=400,y=250)
            def question6():
                lable6 = Label( root,image=pic_five).place(x=0,y=0) 
                QA6 = Label(root,text="6.Luke Skywalker เกิดที่ดาวอะไร ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question7()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question7()
                ANS1 = Button(root,text="1.Polis Massa",command=Score_quizgame).place(x=150,y=200)
                ANS2 = Button(root,text="2.Tatooine",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.coruscant",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.alderaan",command=Score_quizgame2).place(x=400,y=250)
            def question7():
                lable7 = Label( root,image=pic_five).place(x=0,y=0) 
                QA7 = Label(root,text="7.Leia Organa เกิดที่ดาวอะไร ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question8()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question8()
                ANS1 = Button(root,text="1.cpruscant",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.yavin",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.alderaan",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Polis Massa",command=Score_quizgame).place(x=400,y=250)
            def question8():
                lable8 = Label( root,image=pic_five).place(x=0,y=0) 
                QA8 = Label(root,text="8.ยานประจำตัวของ Boba Fett ชือว่าอะไร ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question9()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question9()
                ANS1 = Button(root,text="1.sanado-blood",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.X-wing",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Slave 1",command=Score_quizgame).place(x=150,y=250)
                ANS4 = Button(root,text="4.Razor Crest",command=Score_quizgame2).place(x=400,y=250)
            def question9():
                lable9 = Label( root,image=pic_five).place(x=0,y=0) 
                QA9 = Label(root,text="9.ใครคืออดีตคนรักของ Obi-Wan ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question10()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question10()
                ANS1 = Button(root,text="1.anakin skywakler",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Satine Kryze",command=Score_quizgame).place(x=400,y=200)
                ANS3 = Button(root,text="3.padme",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.sabine wren",command=Score_quizgame2).place(x=400,y=250)
            def question10():
                lable10 = Label( root,image=pic_five).place(x=0,y=0) 
                QA10 = Label(root,text="10.ใครคือทหารโคลนที่ Anakin ไว้ใจมากที่สุด ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        showscore()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        showscore()
                ANS1 = Button(root,text="1.Captain Rex",command=Score_quizgame).place(x=150,y=200)
                ANS2 = Button(root,text="2.commander cody",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.commander wolf",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.five",command=Score_quizgame2).place(x=400,y=250)
            def showscore():
                lable1 = Label( root,image=pic_nine).place(x=0,y=0)
                gg=[]
                for i in boxscore:
                    if i == 1 :
                        gg.append(1)
                print(gg)
                score =len(gg)
                z=sqlite3.connect(r"C:\Users\ACER\Desktop\python\python\pythontest.db")
                z.cursor()
                z.execute(f"INSERT INTO SCORE(username,score) VALUES(?,?)",(username,score,))
                z.commit()
                lable11 = Label(root,text=score,font=('Arail',30),fg='blue',bg='white').place(x=300,y=300)
                
            
            #def seven_Avengers():
            def question11():
                lable1 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA1 = Label(root,text="1.หนังเปิดจักวาล MCU คือเรื่องใด   ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question12()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question12()      
                ANS1 = Button(root,text="1.Iron Man",command=Score_quizgame).place(x=150,y=200)
                ANS2 = Button(root,text="2.Hulk",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.avenger",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.spiderman home coming",command=Score_quizgame2).place(x=400,y=250)
            def question12():
                lable12 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA12 = Label(root,text="2.ใครเป็นคนสร้างชุดให้แก่ Peter Parker ใน spider man home comimg ").place(x=150,y=100) 
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question13()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question13()    
                ANS1 = Button(root,text="1.Hank Pym",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Tony Strak",command=Score_quizgame).place(x=400,y=200)
                ANS3 = Button(root,text="3.Reed Richards",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Bruce banner",command=Score_quizgame2).place(x=400,y=250)
            def question13():
                lable13 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA13 = Label(root,text="3.ใครคือคนที่ได้รับตำแหน่ง Captain America ต่อจาก Steve Roger ").place(x=150,y=100) 
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question14()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question14()     
                ANS1 = Button(root,text="1.sam",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.John Walker",command=Score_quizgame).place(x=400,y=200)
                ANS3 = Button(root,text="3.winter solider",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Black widow",command=Score_quizgame2).place(x=400,y=250)
            def question14():
                lable14 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA14 = Label(root,text="4.ใครคือคนที่อยู่เบื้องหลังเหตุการณ์ Civir War ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question15()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question15()      
                ANS1 = Button(root,text="1.doctor doom",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.mandarin",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.mordo",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Baron Simo",command=Score_quizgame).place(x=400,y=250)
            def question15():
                lable15 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA5 = Label(root,text="5.ใครคือคนที่คิดค้นชุด Antman ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question16()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question16()      
                ANS1 = Button(root,text="1.Hank Pym",command=Score_quizgame).place(x=150,y=200)
                ANS2 = Button(root,text="2.Reed Richards",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Tony Strak",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Bruce banner",command=Score_quizgame2).place(x=400,y=250)
            def question16():
                lable16 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA16 = Label(root,text="6.Black Widow ปรากฏตัวครั้งแรกในหนังเรื่องอะไร ").place(x=150,y=100)
               
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question17()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question17()      
                ANS1 = Button(root,text="1.Avanger",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Hulk",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Iron Man 2",command=Score_quizgame).place(x=150,y=250)
                ANS4 = Button(root,text="4.america the first avenger",command=Score_quizgame2).place(x=400,y=250)
            def question17():
                lable17 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA17 = Label(root,text="7.Hawkeye ปรากฏตัวครั้งแรกในหนังเรื่องอะไร ").place(x=150,y=100) 
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question18()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question18()     
                ANS1 = Button(root,text="1.Avenger ",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Ironman3",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Captain america the first avenger",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Thor",command=Score_quizgame).place(x=400,y=250)
            def question18():
                lable18 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA18 = Label(root,text="8.Wanda ได้รชิงคัมภี Darkhold มาจากใคร ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question19()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question19()      
                ANS1 = Button(root,text="1.Agatha",command=Score_quizgame).place(x=150,y=200)
                ANS2 = Button(root,text="2.Docter Strange",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.Vision",command=Score_quizgame2).place(x=150,y=250)
                ANS4 = Button(root,text="4.Quiksilver",command=Score_quizgame2).place(x=400,y=250)
            def question19():
                lable19 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA19 = Label(root,text="9.ใครคือคนที่มาท้าชิงบัลลังค์กับ T'Challa ").place(x=150,y=100)
                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        question20()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        question20()      
                ANS1 = Button(root,text="1.Nakia",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.Okoye",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.killmonger",command=Score_quizgame).place(x=150,y=250)
                ANS4 = Button(root,text="4.Zuri",command=Score_quizgame2).place(x=400,y=250)
            def question20():
                lable20 = Label( root,image=pic_eight).place(x=0,y=0) 
                QA20 = Label(root,text="10.ธานอสได้รับ Souls Stone มาได้อย่างไร ").place(x=150,y=100)                
                def Score_quizgame():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(1)
                        showscore()
                def Score_quizgame2():
                    z=tkinter.messagebox.askquestion("QA","Are you sure?")
                    if z=="yes":
                        boxscore.append(0)
                        showscore()                            
                ANS1 = Button(root,text="1.แย่งมาจากThor",command=Score_quizgame2).place(x=150,y=200)
                ANS2 = Button(root,text="2.ดึงมาจากหัวของVision",command=Score_quizgame2).place(x=400,y=200)
                ANS3 = Button(root,text="3.สละชีวิตของ Gamora",command=Score_quizgame).place(x=150,y=250)
                ANS4 = Button(root,text="4.Docter Strange ให้มา",command=Score_quizgame2).place(x=400,y=250)
            def showscore():
                lable2 = Label( root,image=pic_ten).place(x=0,y=0)
                gg=[]
                for i in boxscore:
                    if i == 1 :
                        gg.append(1)
                print(gg)
                score =len(gg)
                z=sqlite3.connect(r"C:\Users\ACER\Desktop\python\python\Pythontest.db")
                z.cursor()
                z.execute(f"INSERT INTO SCORE(username,score) VALUES('{username}','{score}')")
                z.commit()
                lable12 = Label(root,text=score,font=('Arail',30),fg='blue',bg='white').place(x=300,y=300)
                                                                                             
            Canvas(root,height=600,width=500)
            Button(root,image=pic_six,command=question1).place(x=0,y=0)
            Button(root,image=pic_seven,command=question11).place(x=325,y=0)


        Button(root,text="login",command=login,height=3,width=13,bd=6).place(x=100,y=120)

        
        
        
#ระบบสมัคร
    def five():
        
        Canvas(root,height=600,width=300)
        bg2_label =Label(root,image=pic_two)
        bg2_label.place(x=0,y=0)


        ULabel = Label(root,text="Username").place(x=40,y=20)
        Tex = StringVar()
        Mytex = Entry(root,textvariable=Tex).place(x=140,y=20)

        PLabel = Label(root,text="Password").place(x=40,y=70)
        Tex2 = StringVar()
        Mytex2 = Entry(root,textvariable=Tex2).place(x=140,y=70)

        
        def Signup () :

            usernamesave = Tex.get()
            passwordsave = Tex2.get()
            print(usernamesave)

            if len(usernamesave) > 10 or len(usernamesave) == 0:
                z=tkinter.messagebox.showerror("Error","Please enter no more than 10 characters.")
                                
            elif len(usernamesave) == 10 or len(usernamesave) < 10 :
                username = usernamesave
                z=tkinter.messagebox.showinfo("Save","We have saved the systems")
                
                if len(passwordsave) > 13 or len(passwordsave) == 0:
                    z=tkinter.messagebox.showerror("Error","Please enter no more than 13 characters.")
                                
                elif len(passwordsave) == 13 or len(passwordsave) < 13 :
                    password = passwordsave
                    z=tkinter.messagebox.showinfo("save","We have saved the systems")
            
            z=sqlite3.connect(r"C:\Users\ACER\Desktop\python\python\pythontest.db")
            z.cursor()
            z.execute(f"INSERT INTO TEST(username,password) VALUES(?,?)",(username,password,))
            z.commit()                            
        But1 = Button(root,text="Okay",font=10,command = Signup).place(x=100,y=120)
        
  
    

    #กดปุ่ม   
    btn4 = Button(root,text="   Sign in   ",fg="black",command = four).place(x=150,y=200) #ไปdef 4
    btn5 = Button(root,text="   Sign up   ",fg="black",command = five).place(x=250,y=200)



    #ปิดโปรแกรม
    def Exitprogram():
        tkinter.messagebox.askquestion("ยันยืน","คุณต้องการปิดโปรแกรมหรือไม่")
        root.destroy()

    #สร้างเมนู
    myMenu = Menu()
    root.config(menu=myMenu)   

    #เพิ่มเมนูย่อย
    menuitem = Menu()
    menuitem.add_command(label="sign in",command=four)
    menuitem.add_command(label="Homepage",command=Homepage)
    menuitem.add_command(label="Exit",command=Exitprogram)
    #เพิ่มเมนู
    myMenu.add_cascade(label="Menu",menu=menuitem)
   

#ที่เก็บรูป
pic_one=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\Game-Quiz.png")
pic_two=PhotoImage(file="\\Users\\ACER\\Dropbox\\My PC (LAPTOP-OTJMF40F)\\Downloads\\shikimori5.png")
pic_three=PhotoImage(file="\\Users\\ACER\\Dropbox\\My PC (LAPTOP-OTJMF40F)\\Downloads\\ชิกิโมริ4.png")
pic_four=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\Game-Quiz.png")
pic_five=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\Starwar 3.png")
pic_six=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\รูปปกอีกรูป.png")
pic_seven=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\รูปปกรูปที่2.png")
pic_eight=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\รูปคำถาม.png")
pic_nine=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\scoreQuiz.png")
pic_ten=PhotoImage(file="\\Users\\ACER\\Desktop\\picture of project\\scoreQuiz 2.png")

#กำหนดขนาดหน้าจอ(x)และตำแหน่งหน้าจอ(+)
root.geometry("625x400+500+50")
root.resizable(0,0)
Homepage()
root.mainloop()