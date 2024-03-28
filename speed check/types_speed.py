from tkinter import *
import random
import ttkthemes
#To apply themes on the buttons
from tkinter import ttk
from time import sleep
import threading

total_time=60
time=0
wrongwords=0
elapsedtimeinmin=0
def start_timer():
    start_button.config(state=DISABLED)
    global time
    #The textarea box will be available for typing
    textarea.config(state="normal")
    #for our cursor to automatically blink we use
    textarea.focus()
    for time in range(1,61):
        elapsed_timer.config(text=time)
        remaining_time=total_time-time
        remaining_timer.config(text=remaining_time)
        #As the elapsed timer directly goes to 60 we waant it to go slowly hence we use
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    reset_button.config(state=NORMAL)   
 #To count wpm,accuracy,wrong words
def count():
    global wrongwords
    while time!=total_time:
    #Here to check total number number words we will get the text typed in text area and break eaxh word in a list by split method 
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    totalwords_count.config(text=totalwords)
    
    para_words_list=label_paragraph['text'].split()
    #Here the zip function will  zip paraword list and entered paragragh in a tuple
    for pair in list(zip(para_words_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords=1

    wrongwords_count.config(text=wrongwords)       

    elapsedtimeinmin=time/60 
    wpm=(totalwords-wrongwords)/elapsedtimeinmin
    wpm_count.config(text=wpm)
    grosswpm=totalwords/elapsedtimeinmin
    accuracy=wpm/grosswpm*100
    accuracy=round(accuracy)
    accuracy_count.config(text=str(accuracy)+'%')

#To start to functions at the same time
def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2=threading.Thread(target=count)
    t2.start()

def reset():
    global time,elapsedtimeinmin
    time=0
    elapsedtimeinmin=0
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer.config(text="0")
    remaining_timer.config(text="0")
    wpm_count.config(text="0")
    accuracy_count.config(text="0")
    totalwords_count.config(text="0")
    wrongwords_count.config(text="0")
    

root=Tk()
root.geometry('960x700')
#To disable the maximize button
root.resizable(0,0)
#To remove the starting manu bar
root.overrideredirect(True)
#Frame for the top bar
mainframe=Frame(root,bd=5)
mainframe.grid()

titleframe=Frame(mainframe,bg="black")
titleframe.grid()

titlelabel=Label(titleframe,text="Typing Speed",font=("algerian",20,"bold"),bg="goldenrod3",fg="white",width=51)
titlelabel.grid(pady=5,padx=3)

#Frame for the text to be shown part

paragraphframe=Frame(mainframe)
paragraphframe.grid(row=1,column=0)
paragraph_list=["A data entry clerk is a member of staff employed to enter or update data into a computer system. Data is often entered into a computer from paper documents using a keyboard. The keyboards used can often have special keys and multiple colors to help in the task and speed up the work. Proper ergonomics at the workstation is a common topic considered. The Data Entry Clerk may also use a mouse, and a manually-fed scanner may be involved. Speed and accuracy, not necessarily in that order, are the key measures of the job; it is possible to do this job from home.",
                "It was a simple green chair. There was nothing extraordinary about it or so it seemed. It was the type of chair one would pass without even noticing it was there, let alone what the actual color of it was. It was due to this common and unassuming appearance that few people actually stopped to sit in it and discover its magical powers.",
                "I am heading back to Colorado tomorrow after being down in Santa Barbara over the weekend for the festival there. I will be making October plans once there and will try to arrange so I'm back here for the birthday if possible.I'll let you know as soon as I know the doctors appointment schedule and my flight plans.",
                "Terrance knew that sometimes it was simply best to stay out of it. He kept repeating this to himself as he watched the scene unfold. He knew that nothing good would come of him getting involved. It was far better for him to stay on the sidelines and observe. He kept yelling this to himself inside his head as he walked over to the couple and punched the man in the face."]
#The paragraphs will be shuffled
random.shuffle(paragraph_list)

#To get paragraph in  multiple lines use wraplenghth
label_paragraph=Label(paragraphframe,text=paragraph_list[0],wraplength=912,justify="left",font=("arial",14,"bold"))
label_paragraph.grid()

#To add text area
textframe=Frame(mainframe)
textframe.grid(row=2,column=0)

textarea=Text(textframe,font=("arial",12,"bold"),width=100,height=10,bd=4,relief="sunken",wrap="word",state="disabled")
textarea.grid()

#To add the Labels
frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time=Label(frame_output,text="Elapsed Time:",font=("Tahuma",12,"bold"),fg="purple")
elapsed_time.grid(padx=3)

elapsed_timer=Label(frame_output,text="0",font=("Tahuma",12,"bold"))
elapsed_timer.grid(row=0,column=1,padx=3)

remaining_time=Label(frame_output,text="Remaining Time:",font=("Tahuma",12,"bold"),fg="purple")
remaining_time.grid(row=0,column=2,padx=3)

remaining_timer=Label(frame_output,text="60",font=("Tahuma",12,"bold"))
remaining_timer.grid(row=0,column=4,padx=3)

wpm_label=Label(frame_output,text="WPM:",font=("Tahuma",12,"bold"),fg="purple")
wpm_label.grid(row=0,column=5,padx=3)

wpm_count=Label(frame_output,text="0",font=("Tahuma",12,"bold"))
wpm_count.grid(row=0,column=6,padx=3)

accuracy_label=Label(frame_output,text="Accuracy:",font=("Tahuma",12,"bold"),fg="purple")
accuracy_label.grid(row=0,column=7,padx=3)

accuracy_count=Label(frame_output,text="0",font=("Tahuma",12,"bold"))
accuracy_count.grid(row=0,column=8,padx=3)

totalwords_label=Label(frame_output,text="Total Words:",font=("Tahuma",12,"bold"),fg="purple")
totalwords_label.grid(row=0,column=9,padx=3)

totalwords_count=Label(frame_output,text="0",font=("Tahuma",12,"bold"))
totalwords_count.grid(row=0,column=10,padx=3)

wrongwords_label=Label(frame_output,text="Wrong Words:",font=("Tahuma",12,"bold"),fg="purple")
wrongwords_label.grid(row=0,column=11,padx=3)

wrongwords_count=Label(frame_output,text="0",font=("Tahuma",12,"bold"))
wrongwords_count.grid(row=0,column=12,padx=3)

#Frame for adding buttons
button_frame=Frame(mainframe)
button_frame.grid(row=4,column=0)

start_button=Button(button_frame,text="Start",font=("MV Boli",10,"bold"),relief="ridge",border=5,width=16,padx=5,bg="black",fg="white",command=start)
start_button.grid(row=0,column=0,padx=5)

reset_button=Button(button_frame,text="Reset",font=("MV Boli",10,"bold"),relief="ridge",border=5,width=16,padx=5,bg="black",fg="white",state=DISABLED,command=reset)
reset_button.grid(row=0,column=1,padx=5)

exit_button=Button(button_frame,text="Exit",font=("MV Boli",10,"bold"),relief="ridge",border=5,width=16,padx=5,bg="black",fg="white",command=root.destroy)
exit_button.grid(row=0,column=2,padx=5)

#To create keyboard
keyboardframe=Frame(mainframe)
keyboardframe.grid(row=5,column=0)

frame1to0=Frame(keyboardframe)
frame1to0.grid(row=0,column=0,pady=3)

Label1=Label(frame1to0,text="1",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label2=Label(frame1to0,text="2",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label3=Label(frame1to0,text="3",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label4=Label(frame1to0,text="4",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label5=Label(frame1to0,text="5",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label6=Label(frame1to0,text="6",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label7=Label(frame1to0,text="7",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label8=Label(frame1to0,text="8",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label9=Label(frame1to0,text="9",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)
Label0=Label(frame1to0,text="0",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=10)

Label1.grid()
Label2.grid(row=0,column=1,padx=10)
Label3.grid(row=0,column=2,padx=10)
Label4.grid(row=0,column=3,padx=10)
Label5.grid(row=0,column=4,padx=10)
Label6.grid(row=0,column=5,padx=10)
Label7.grid(row=0,column=6,padx=10)
Label8.grid(row=0,column=7,padx=10)
Label9.grid(row=0,column=8,padx=10)
Label0.grid(row=0,column=9,padx=10)

frameqtop=Frame(mainframe)
frameqtop.grid(row=6,column=0,pady=3)

Labelq=Label(frameqtop,text="Q",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelw=Label(frameqtop,text="W",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labele=Label(frameqtop,text="E",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelr=Label(frameqtop,text="R",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelt=Label(frameqtop,text="T",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labely=Label(frameqtop,text="Y",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelu=Label(frameqtop,text="U",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labeli=Label(frameqtop,text="I",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelo=Label(frameqtop,text="O",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelp=Label(frameqtop,text="P",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)

Labelq.grid(row=0,column=0,padx=10)
Labelw.grid(row=0,column=1,padx=10)
Labelr.grid(row=0,column=2,padx=10)
Labelt.grid(row=0,column=3,padx=10)
Labely.grid(row=0,column=4,padx=10)
Labelu.grid(row=0,column=5,padx=10)
Labeli.grid(row=0,column=6,padx=10)
Labelo.grid(row=0,column=7,padx=10)
Labelp.grid(row=0,column=8,padx=10)

frameatol=Frame(mainframe)
frameatol.grid(row=7,column=0,pady=3)

Labela=Label(frameatol,text="A",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labels=Label(frameatol,text="S",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labeld=Label(frameatol,text="D",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelf=Label(frameatol,text="F",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelg=Label(frameatol,text="G",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelh=Label(frameatol,text="H",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelj=Label(frameatol,text="J",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelk=Label(frameatol,text="K",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labell=Label(frameatol,text="L",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)

Labela.grid(row=0,column=0,padx=10)
Labels.grid(row=0,column=1,padx=10)
Labeld.grid(row=0,column=2,padx=10)
Labelf.grid(row=0,column=3,padx=10)
Labelg.grid(row=0,column=4,padx=10)
Labelh.grid(row=0,column=5,padx=10)
Labelj.grid(row=0,column=6,padx=10)
Labelk.grid(row=0,column=7,padx=10)
Labell.grid(row=0,column=8,padx=10)

frameztom=Frame(mainframe)
frameztom.grid(row=8,column=0,pady=3)

Labelz=Label(frameztom,text="Z",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelx=Label(frameztom,text="X",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelc=Label(frameztom,text="C",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelv=Label(frameztom,text="V",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelb=Label(frameztom,text="B",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labeln=Label(frameztom,text="N",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)
Labelm=Label(frameztom,text="M",font=("arial",10,"bold"),bg="goldenrod3",fg="black",width=5,height=2,relief="groove",border=8)

Labelz.grid(row=0,column=0,padx=8)
Labelx.grid(row=0,column=1,padx=8)
Labelc.grid(row=0,column=2,padx=8)
Labelv.grid(row=0,column=3,padx=8)
Labelb.grid(row=0,column=4,padx=8)
Labeln.grid(row=0,column=5,padx=8)
Labelm.grid(row=0,column=6,padx=8)

framespace=Frame(mainframe)
framespace.grid(row=9,column=0,pady=3)

Labelspace=Label(framespace,text="",bg="goldenrod3",fg="black",width=45,height=2,relief="groove",border=8)
Labelspace.grid()

#To connect laptop keys to applications keys
def changebg(widget):
    #When the buttons are typed the color will be changed to lightblue
    widget.config(bg="lightblue")
    #After 800 px the color will change to original colr
    widget.after(200,lambda:widget.config(bg="goldenrod3"))

Labelnumbers=[Label1,Label2,Label3,Label4,Label5,Label6,Label7,Label8,Label9,Label0]
Labelalphabets=[Labela,Labelb,Labelc,Labeld,Labele,Labelf,Labelg,Labelh,Labeli,Labelj,Labelk,Labell,Labelm,Labeln,Labelo,Labelp,Labelq,Labelr,Labels,Labelt,Labelu,Labelv,Labelx,Labely,Labelz]
Labelspaces=[Labelspace]

binding_numbers=['1','2','3','4','5','6','7','8','9','0']
binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']

#event is used to store which key is pressed
for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers],lambda event,label=Labelnumbers[numbers]:changebg(label))

for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=Labelalphabets[capital_alphabets]:changebg(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event,label=Labelalphabets[small_alphabets]:changebg(label))

root.bind('<space>',lambda event:changebg(Labelspaces[0])) 

root.mainloop()
