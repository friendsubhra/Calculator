import mathematics as m
import tkinter as tk

exp=""
dis=""
second=True
def sec2nd():
    global second
    if second == True:
        btn_sin.place_forget()
        btn_asin.place(x=dimx/14,y=7*dimy/14,anchor="center")

        btn_sec.place_forget()
        btn_asec.place(x=dimx/14,y=9*dimy/14,anchor="center")

        btn_cos.place_forget()
        btn_acos.place(x=3*dimx/14,y=7*dimy/14,anchor="center")

        btn_csc.place_forget()
        btn_acsc.place(x=3*dimx/14,y=9*dimy/14,anchor="center")

        btn_tan.place_forget()
        btn_atan.place(x=5*dimx/14,y=7*dimy/14,anchor="center")

        btn_cot.place_forget()
        btn_acot.place(x=5*dimx/14,y=9*dimy/14,anchor="center")

        btn_2nd.place_forget()
        btn_1st.place(x=dimx/14,y=5*dimy/14,anchor="center")

        second=False
    return
def fir1st():
    global second
    if second == False:
        btn_asin.place_forget()
        btn_sin.place(x=dimx/14,y=7*dimy/14,anchor="center")

        btn_asec.place_forget()
        btn_sec.place(x=dimx/14,y=9*dimy/14,anchor="center")

        btn_acos.place_forget()
        btn_cos.place(x=3*dimx/14,y=7*dimy/14,anchor="center")

        btn_acsc.place_forget()
        btn_csc.place(x=3*dimx/14,y=9*dimy/14,anchor="center")

        btn_atan.place_forget()
        btn_tan.place(x=5*dimx/14,y=7*dimy/14,anchor="center")

        btn_acot.place_forget()
        btn_cot.place(x=5*dimx/14,y=9*dimy/14,anchor="center")

        btn_1st.place_forget()
        btn_2nd.place(x=dimx/14,y=5*dimy/14,anchor="center")

        second=True
    return
def percent():
    global dis, exp
    dis+="%"
    exp+="/100"
    equation.set(dis)
def number(x):
    global exp, dis
    exp+=str(x)
    dis+=str(x)
    equation.set(dis)
def add():
    global exp, dis
    exp+="+"
    dis+="+"
    equation.set(dis) 
def sub():
    global exp, dis
    exp+="-"
    dis+="-"
    equation.set(dis)
def multi():
    global exp, dis
    exp+="*"
    dis+="x"
    equation.set(dis)
def divide():
    global exp, dis
    exp+="/"
    dis+="÷"
    equation.set(dis)
def dot():
    global exp, dis
    exp+="."
    dis+="."
    equation.set(dis)
def pow():
    global exp, dis
    exp+="**"
    dis+="^"
    equation.set(dis)
def sqr():
    global exp, dis
    exp+="**2"
    dis+="^2"
    equation.set(dis)
def sqrrt():
    global exp, dis
    exp+="m.sqrroot("
    dis+="√("
    equation.set(dis)
def bktop():
    global exp, dis
    exp+="("
    dis+="("
    equation.set(dis)
def bktcls():
    global exp, dis
    exp+=")"
    dis+=")"
    equation.set(dis)
def sin():
    global exp, dis
    exp+="m.sin("
    dis+="sin("
    equation.set(dis)
def cos():
    global exp, dis
    exp+="m.cos("
    dis+="cos("
    equation.set(dis)
def tan():
    global exp, dis
    exp+="m.tan("
    dis+="tan("
    equation.set(dis)
def sec():
    global exp, dis
    exp+="m.sec("
    dis+="sec("
    equation.set(dis)
def csc():
    global exp, dis
    exp+="m.cosec("
    dis+="cosec("
    equation.set(dis)
def cot():
    global exp, dis
    exp+="m.cot("
    dis+="cot("
    equation.set(dis)
def asin():
    global exp, dis
    exp+="m.asin("
    dis+="asin("
    equation.set(dis)
def acos():
    global exp, dis
    exp+="m.acos("
    dis+="acos("
    equation.set(dis)
def atan():
    global exp, dis
    exp+="m.atan("
    dis+="atan("
    equation.set(dis)
def asec():
    global exp, dis
    exp+="m.asec("
    dis+="asec("
    equation.set(dis)
def acsc():
    global exp, dis
    exp+="m.cosec("
    dis+="cosec("
    equation.set(dis)
def acot():
    global exp, dis
    exp+="m.acot("
    dis+="acot("
    equation.set(dis)
def log():
    global exp, dis
    exp+="m.log(base=10,num="
    dis+="log("
    equation.set(dis)
def ln():
    global exp, dis
    exp+="m.log(num="
    dis+="ln("
    equation.set(dis)
def fact():
    global exp, dis
    i=-1
    while True:
        if type(exp[i])!=int:
            exp=exp[:i]+"m.fact("+exp[i:]+")"
            break
        i-=1
    dis+="!"
    equation.set(dis)
def pi():
    global exp, dis
    exp+="m.pi"
    dis+="π"
    equation.set(dis)
def e():
    global exp, dis
    exp+="m.e"
    dis+="e"
    equation.set(dis)
def CE():
    global exp, dis
    exp=""
    dis=""
    equation.set(dis)
def equals():
    global exp, dis
    try:
        res=eval(exp)
    except:
        equation.set("error!")
        return CE()
    res=round(res,9)
    if res==int(res):
        res=int(res)
    exp=str(res)
    dis=str(res)
    equation.set(dis)

leng=7
brdth=2
border=0
size=25
orange="#ff6600"
white="#ffffff"
black="#1b1b1b"
blue="#1520A6"

win=tk.Tk(className="Calculator")
dimy=714
dimx=980
win.geometry(f"{dimx}x{dimy}")
win.configure(bg=black)

equation=tk.StringVar()
expression_field=tk.Entry(win, textvariable=equation,fg=white,bg=black,justify="right",relief="flat",font=("Helvetica", str(45+1)),width=leng*4)
expression_field.place(x=7*dimx/14,y=2*dimy/14,anchor="center")

btn_2nd=tk.Button(win,text="2nd",bd=border,font=("Helvetica", str(size)),command=sec2nd,relief="flat",height=brdth,width=leng)
btn_2nd.place(x=dimx/14,y=5*dimy/14,anchor="center")
btn_sin=tk.Button(win,text="sin",bd=border,font=("Helvetica", str(size)),command=sin,relief="flat",height=brdth,width=leng)
btn_sin.place(x=dimx/14,y=7*dimy/14,anchor="center")
btn_sec=tk.Button(win,text="sec",bd=border,font=("Helvetica", str(size)),command=sec,relief="flat",height=brdth,width=leng)
btn_sec.place(x=dimx/14,y=9*dimy/14,anchor="center")
btn_n=tk.Button(win,text="n!",bd=border,font=("Helvetica", str(size)),command=fact,relief="flat",height=brdth,width=leng)
btn_n.place(x=dimx/14,y=11*dimy/14,anchor="center")
btn_exp=tk.Button(win,text="x^y",bd=border,font=("Helvetica", str(size)),command=pow,relief="flat",height=brdth,width=leng)
btn_exp.place(x=dimx/14,y=13*dimy/14,anchor="center")

btn_1st=tk.Button(win,text="1st",bd=border,font=("Helvetica", str(size)),command=fir1st,relief="flat",height=brdth,width=leng)
btn_asin=tk.Button(win,text="asin",bd=border,font=("Helvetica", str(size)),command=asin,relief="flat",height=brdth,width=leng)
btn_asec=tk.Button(win,text="asec",bd=border,font=("Helvetica", str(size)),command=asec,relief="flat",height=brdth,width=leng)

btn_pi=tk.Button(win,text="π",bd=border,font=("Helvetica", str(size)),command=pi,relief="flat",height=brdth,width=leng)
btn_pi.place(x=3*dimx/14,y=5*dimy/14,anchor="center")
btn_cos=tk.Button(win,text="cos",bd=border,font=("Helvetica", str(size)),command=cos,relief="flat",height=brdth,width=leng)
btn_cos.place(x=3*dimx/14,y=7*dimy/14,anchor="center")
btn_csc=tk.Button(win,text="csc",bd=border,font=("Helvetica", str(size)),command=csc,relief="flat",height=brdth,width=leng)
btn_csc.place(x=3*dimx/14,y=9*dimy/14,anchor="center")
btn_log=tk.Button(win,text="log",bd=border,font=("Helvetica", str(size)),command=log,relief="flat",height=brdth,width=leng)
btn_log.place(x=3*dimx/14,y=11*dimy/14,anchor="center")
btn_sqr=tk.Button(win,text="sqr",bd=border,font=("Helvetica", str(size)),command=sqr,relief="flat",height=brdth,width=leng)
btn_sqr.place(x=3*dimx/14,y=13*dimy/14,anchor="center")

btn_acos=tk.Button(win,text="acos",bd=border,font=("Helvetica", str(size)),command=acos,relief="flat",height=brdth,width=leng)
btn_acsc=tk.Button(win,text="acsc",bd=border,font=("Helvetica", str(size)),command=acsc,relief="flat",height=brdth,width=leng)

btn_e=tk.Button(win,text="e",bd=border,font=("Helvetica", str(size)),command=e,relief="flat",height=brdth,width=leng)
btn_e.place(x=5*dimx/14,y=5*dimy/14,anchor="center")
btn_tan=tk.Button(win,text="tan",bd=border,font=("Helvetica", str(size)),command=tan,relief="flat",height=brdth,width=leng)
btn_tan.place(x=5*dimx/14,y=7*dimy/14,anchor="center")
btn_cot=tk.Button(win,text="cot",bd=border,font=("Helvetica", str(size)),command=cot,relief="flat",height=brdth,width=leng)
btn_cot.place(x=5*dimx/14,y=9*dimy/14,anchor="center")
btn_ln=tk.Button(win,text="ln",bd=border,font=("Helvetica", str(size)),command=ln,relief="flat",height=brdth,width=leng)
btn_ln.place(x=5*dimx/14,y=11*dimy/14,anchor="center")
btn_sqrrt=tk.Button(win,text="√",bd=border,font=("Helvetica", str(size)),command=sqrrt,relief="flat",height=brdth,width=leng)
btn_sqrrt.place(x=5*dimx/14,y=13*dimy/14,anchor="center")

btn_atan=tk.Button(win,text="atan",bd=border,font=("Helvetica", str(size)),command=atan,relief="flat",height=brdth,width=leng)
btn_acot=tk.Button(win,text="acot",bd=border,font=("Helvetica", str(size)),command=acot,relief="flat",height=brdth,width=leng)

btn_bktop=tk.Button(win,text="(",bd=border,font=("Helvetica", str(size)),command=bktop,relief="flat",height=brdth,width=leng)
btn_bktop.place(x=7*dimx/14,y=5*dimy/14,anchor="center")
btn_7=tk.Button(win,text="7",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(7),relief="flat",height=brdth,width=leng)
btn_7.place(x=7*dimx/14,y=7*dimy/14,anchor="center")
btn_4=tk.Button(win,text="4",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(4),relief="flat",height=brdth,width=leng)
btn_4.place(x=7*dimx/14,y=9*dimy/14,anchor="center")
btn_1=tk.Button(win,text="1",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(1),relief="flat",height=brdth,width=leng)
btn_1.place(x=7*dimx/14,y=11*dimy/14,anchor="center")
btn_0=tk.Button(win,text="0",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(0),relief="flat",height=brdth,width=leng)
btn_0.place(x=7*dimx/14,y=13*dimy/14,anchor="center")


btn_bktcls=tk.Button(win,text=")",bd=border,font=("Helvetica", str(size)),command=bktcls,relief="flat",height=brdth,width=leng)
btn_bktcls.place(x=9*dimx/14,y=5*dimy/14,anchor="center")
btn_8=tk.Button(win,text="8",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(8),relief="flat",height=brdth,width=leng)
btn_8.place(x=9*dimx/14,y=7*dimy/14,anchor="center")
btn_5=tk.Button(win,text="5",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(5),relief="flat",height=brdth,width=leng)
btn_5.place(x=9*dimx/14,y=9*dimy/14,anchor="center")
btn_2=tk.Button(win,text="2",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(2),relief="flat",height=brdth,width=leng)
btn_2.place(x=9*dimx/14,y=11*dimy/14,anchor="center")
btn_dot=tk.Button(win,text=".",bg=white,bd=border,font=("Helvetica", str(size)),command=dot,relief="flat",height=brdth,width=leng)
btn_dot.place(x=9*dimx/14,y=13*dimy/14,anchor="center")


btn_percent=tk.Button(win,text="%",bd=border,font=("Helvetica", str(size)),command=percent,relief="flat",height=brdth,width=leng)
btn_percent.place(x=11*dimx/14,y=5*dimy/14,anchor="center")
btn_9=tk.Button(win,text="9",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(9),relief="flat",height=brdth,width=leng)
btn_9.place(x=11*dimx/14,y=7*dimy/14,anchor="center")
btn_6=tk.Button(win,text="6",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(6),relief="flat",height=brdth,width=leng)
btn_6.place(x=11*dimx/14,y=9*dimy/14,anchor="center")
btn_3=tk.Button(win,text="3",bg=white,bd=border,font=("Helvetica", str(size)),command=lambda : number(3),relief="flat",height=brdth,width=leng)
btn_3.place(x=11*dimx/14,y=11*dimy/14,anchor="center")
btn_equals=tk.Button(win,text="=",fg=white,bg=blue,bd=border,font=("Helvetica", str(size)),command=equals,relief="flat",height=brdth,width=leng)
btn_equals.place(x=11*dimx/14,y=13*dimy/14,anchor="center")

btn_CE=tk.Button(win,text="CE",fg=white,bg=orange,bd=border,font=("Helvetica", str(size)),command=CE,relief="flat",height=brdth,width=leng)
btn_CE.place(x=13*dimx/14,y=5*dimy/14,anchor="center")
btn_div=tk.Button(win,text="÷",fg=white,bg=orange,bd=border,font=("Helvetica", str(size)),command=divide,relief="flat",height=brdth,width=leng)
btn_div.place(x=13*dimx/14,y=7*dimy/14,anchor="center")
btn_multi=tk.Button(win,text="x",fg=white,bg=orange,bd=border,font=("Helvetica", str(size)),command=multi,relief="flat",height=brdth,width=leng)
btn_multi.place(x=13*dimx/14,y=9*dimy/14,anchor="center")
btn_sub=tk.Button(win,text="-",fg=white,bg=orange,bd=border,font=("Helvetica", str(size)),command=sub,relief="flat",height=brdth,width=leng)
btn_sub.place(x=13*dimx/14,y=11*dimy/14,anchor="center")
btn_add=tk.Button(win,text="+",fg=white,bg=orange,bd=border,font=("Helvetica", str(size)),command=add,relief="flat",height=brdth,width=leng)
btn_add.place(x=13*dimx/14,y=13*dimy/14,anchor="center")

win.mainloop()
