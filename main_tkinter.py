import tkinter as tk
import langdetect as detect
from deep_translator import GoogleTranslator
import pyttsx3
from langcodes import Language

def detectLanguage(text):
    answer = detect.detect(text)
    return Language.make(language=answer).display_name()

def trans_to_english():
    trans = GoogleTranslator(target='en')
    val = text_box_2.get(1.0,"end-1c")
    ans= trans.translate(val)
    ans_lab2.config(text="Translated Text: \n"+ans)
def trans_to_hindi():
    transH = GoogleTranslator(target='hi')
    val = text_box_3.get(1.0,"end-1c")
    ans = transH.translate(val)
    ans_lab3.config(text="Translated Text: \n"+ans)

def text_to_speech():
    tts_engine = pyttsx3.init()
    val = text_box_4.get(1.0,"end-1c")
    tts_engine.say(val)
    tts_engine.setProperty("rate",50)
    tts_engine.runAndWait()

def set_label_text():
    val = text_box_1.get(1.0,'end-1c')
    ans = detectLanguage(val)
    ans_lab.config(text="Detected Language: "+ans)
    
def ch_LD():
    Lang_dec.pack(fill='both',expand=1)
    Lang_trans.pack_forget()
    Lang_trans_hi.pack_forget()
    TTs.pack_forget()

def ch_LT():
    Lang_trans.pack(fill='both',expand=1)
    Lang_dec.pack_forget()
    Lang_trans_hi.pack_forget()
    TTs.pack_forget()

def ch_LTH():
    Lang_trans_hi.pack(fill='both',expand=1)
    Lang_trans.pack_forget()
    Lang_dec.pack_forget()
    TTs.pack_forget()

def ch_TTS():
    TTs.pack(fill='both',expand=1)
    Lang_trans.pack_forget()
    Lang_trans_hi.pack_forget()
    Lang_dec.pack_forget()

frame = tk.Tk()
frame.title("Play Lang")
frame.config(bg="gray")
frame.geometry("900x600")
Heading1 = tk.Label(frame,text="TASK ROUND APP",font=('Times New Roman', 22, 'bold','underline'))
Heading1.pack()
butt_frame = tk.Frame(frame)
Lang_dec = tk.Frame(frame)
Lang_trans = tk.Frame(frame)
Lang_trans_hi = tk.Frame(frame)
TTs = tk.Frame(frame)
ld = tk.Button(butt_frame,text="Language Detection",command=ch_LD)
lt = tk.Button(butt_frame,text="Language Translation",command=ch_LT)
lth = tk.Button(butt_frame,text="Hindi Translation",command=ch_LTH)
tts = tk.Button(butt_frame,text="TTS",command=ch_TTS)
ld.grid(row=1,column=0,padx=5)
lt.grid(row=1,column=1,padx=5)
lth.grid(row=1,column=2,padx=5)
tts.grid(row=1,column=3)
butt_frame.pack(pady=20)
Heading2 = tk.Label(Lang_dec,text="Language Detection",font=('Times New Roman', 18, 'bold','underline'))
Heading2.pack()
label1 = tk.Label(Lang_dec,text='Enter the data to check language: ',font=('Times New Roman', 14, 'bold'),justify=tk.LEFT)
label1.pack(pady=20,padx=20,side=tk.TOP)
text_box_1 = tk.Text(Lang_dec,height=5,width=50)
text_box_1.pack(pady=20,padx=20,side=tk.TOP,expand=True,fill=tk.BOTH)
ans_lab = tk.Label(Lang_dec,text="Detected Language: ",font=('Times New Roman', 14, 'bold'))
ans_lab.pack(pady=20,padx=20,side=tk.TOP)
tr_butt = tk.Button(Lang_dec,text='Detect',command=set_label_text)
tr_butt.pack(pady=20,padx=20,side=tk.TOP)
Heading3 = tk.Label(Lang_trans,text="TRANSLATE TO ENGLISH",font=('Times New Roman', 18, 'bold','underline'))
Heading3.pack()
label2 = tk.Label(Lang_trans,text='Enter data to translate: ',font=('Times New Roman', 14, 'bold'),justify=tk.LEFT)
label2.pack(pady=20,padx=20,side=tk.TOP)
text_box_2 = tk.Text(Lang_trans,height=5,width=50)
text_box_2.pack(pady=5,padx=20,side=tk.TOP,expand=True,fill=tk.BOTH)
ans_lab2 = tk.Label(Lang_trans,text="Translated Text: ",font=('Times New Roman', 14, 'bold'))
ans_lab2.pack(pady=20,padx=20,side=tk.TOP)
check_butt = tk.Button(Lang_trans,text='Translate',command=trans_to_english)
check_butt.pack(pady=20,padx=20,side=tk.TOP)
Heading4 = tk.Label(Lang_trans_hi,text="TRANSLATE TO HINDI",font=('Times New Roman', 18, 'bold','underline'))
Heading4.pack()
label3 = tk.Label(Lang_trans_hi,text='Enter data to translate: ',font=('Times New Roman', 14, 'bold'),justify=tk.LEFT)
label3.pack(pady=20,padx=20,side=tk.TOP)
text_box_3 = tk.Text(Lang_trans_hi,height=2,width=50)
text_box_3.pack(pady=5,padx=20,side=tk.TOP,expand=True,fill=tk.BOTH)
ans_lab3 = tk.Label(Lang_trans_hi,text="Translated Text: ",font=('Times New Roman', 14, 'bold'))
ans_lab3.pack(pady=20,padx=20,side=tk.TOP)
check_butt2 = tk.Button(Lang_trans_hi,text='Translate',command=trans_to_hindi,justify=tk.LEFT)
check_butt2.pack(pady=20,padx=20,side=tk.TOP)
Heading2 = tk.Label(TTs,text="TEXT TO SPEECH",font=('Times New Roman', 18, 'bold','underline'))
Heading2.pack()
text_box_4 = tk.Text(TTs,height=2,width=50)
text_box_4.pack(pady=10,padx=20,side=tk.TOP,expand=True,fill=tk.BOTH)
check_butt3 = tk.Button(TTs,text='SPEAK!',command=text_to_speech,justify=tk.LEFT)
check_butt3.pack(pady=25,padx=20,side=tk.TOP)
frame.mainloop()
