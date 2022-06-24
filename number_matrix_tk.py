import tkinter as tk

class numberMatrix: #get the keys pressed (this code is for a windowed app)
    mode=1
    rounded=1
    getresult=1
    status=0 #1: on; 2:off
    color_green='#2ECC71'
    color_red='#E74C3C'
    color_defaultBg='#17202A'
    color_button='#2E4053'
    color_defaultFg='#F2F3F4'
    color_screen='#ABB2B9'
    
    def __init__(self) -> None:
        self.setup()
        
        
        
    def shift(self):
        self.mode_clear.config(text='clear',command=self.clear)
    
    def alpha(self):
        pass
    
    def normal(self):
        self.mode_clear.config(text='mode',command=self.calc_mode)
    
    
    
    
    def clear(self):
        pass
        #that function is the clear method (shift + mode)
        
    def calc_mode(self):
        pass#the mode method 


    def change_mode(self,mode): #change the mode. Args: literal 1,2,3
        if not self.status: return
        if mode == self.mode: mode = 1
        self.mode = mode
        match mode:
            case 1:self.normal()
            case 2:self.shift()
            case 3:self.alpha()
 
        self.screen_set_mode(mode=mode)

    def on_start(self):#default args and config
        #TODO
        self.status=1
        self.mode = 1
        self.screen_set_mode(mode=1,rounded=8,getresult=1)
        self.button_on.configure(bg=self.color_green,text='Off',command=self.on_off)

    def on_off(self):
        self.status=0
        self.screen_clear_all()
        self.button_on.configure(bg=self.color_red,text='On',command=self.on_start)


    #scrren functions
    def screen_clear_all(self):
        self.screen_widget.delete('1.0',tk.END)
    def screen_clear_mode(self):
        self.screen_widget.delete('1.0','1.0 lineend')
    def screen_clear_result(self):
        self.screen_widget.delete('3.0','3.0 lineend')
    def screen_clear_input(self):
        self.screen_widget.delete('2.0','2.0 lineend')

    def screen_write_input(self,to_write):
        self.screen_widget.insert("2.0 lineend",to_write)
    def screen_write_input(self,to_write):
        self.screen_widget.insert("3.0 lineend",to_write)
    
    def screen_set_mode(self,mode=0,rounded=0,getresult=0):
        m,r,g = (self.screen_widget.get('1.0','1.0 lineend').split()+['']*3)[:3]
        mode = 'Normal' if mode==1 else 'Shift' if mode ==2 else 'Alpha' if mode==3 else m
        rounded = 'Entero' if rounded==-1 else str(rounded) if rounded else r
        getresult = 'Decimal' if getresult==1 else 'Angular' if mode ==2 else 'N.Cient' if mode==3 else g
        to_add=(mode,rounded,getresult)
        self.screen_widget.delete('1.0','1.0 lineend')
        self.screen_widget.insert('1.0','\t'.join(to_add))


    def setup(self):
        self.title ='Scientific Calculator'
        #create the graphic matrix (simulating a cassio calc)
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.config(bg=self.color_defaultBg)
        self.root.geometry('300x550')
        #frame 1: Title
        self.frame1 = tk.Frame(self.root);self.frame1.pack()
        #frame 2: Screen and navegate buttons
        self.frame2 = tk.Frame(self.root);self.frame2.pack()
        #navegate buttons
        self.frame2_2 = tk.Frame(self.root);self.frame2_2.pack()
        #frame 3: Advanced operations 
        self.frame3 = tk.Frame(self.root);self.frame3.pack()
        #frame 4: Basic operations
        self.frame4 = tk.Frame(self.root);self.frame4.pack()

        #add title
        self.titleLab = tk.Label(self.frame1,text=self.title,bg=self.color_defaultBg,fg='#FFFFFF');self.titleLab.pack()
        #add the screen
        self.screen_widget = tk.Text(self.frame2,height=3,bg=self.color_screen,fg='#111111',width=35);self.screen_widget.grid(padx=5,pady=5)  #change the heigh to better perform

        #add navegate button
        self.button_shift = tk.Button(self.frame2_2,text='shift',command=lambda:self.change_mode(2),bg=self.color_button,fg=self.color_defaultFg).grid(row=0,column=0,padx=3,pady=3)
        self.button_alpha = tk.Button(self.frame2_2,text='alpha',command=lambda:self.change_mode(3),bg=self.color_button,fg=self.color_defaultFg).grid(row=0,column=1,padx=3,pady=3)
        self.mode_clear = tk.Button(self.frame2_2,text='mode',bg=self.color_button,fg=self.color_defaultFg,command=self.calc_mode);self.mode_clear.grid(row=0,column=6,padx=3,pady=3)
        self.button_on = tk.Button(self.frame2_2,text='On',command=self.on_start,fg='#FFFFFF',bg=self.color_red);self.button_on.grid(row=0,column=7,padx=3,pady=3)
        self.button_up = tk.Button(self.frame2_2,text=' ^ ',bg=self.color_button,fg=self.color_defaultFg).grid(row=0,column=3,padx=3,pady=3)
        self.button_down = tk.Button(self.frame2_2,text=' v ',bg=self.color_button,fg=self.color_defaultFg).grid(row=0,column=4,padx=3,pady=3)
        self.button_left = tk.Button(self.frame2_2,text=' < ',bg=self.color_button,fg=self.color_defaultFg).grid(row=0,column=2,padx=3,pady=3)
        self.button_right = tk.Button(self.frame2_2,text=' > ',bg=self.color_button,fg=self.color_defaultFg).grid(row=0,column=5,padx=3,pady=3)
        
        #add scientific buttons
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=0,column=0,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=0,column=1,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=0,column=4,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=0,column=5,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=1,column=0,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=1,column=1,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=1,column=2,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=1,column=3,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=1,column=4,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=1,column=5,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=2,column=0,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=2,column=1,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=2,column=2,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=2,column=3,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=2,column=4,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=2,column=5,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=3,column=0,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=3,column=1,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=3,column=2,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=3,column=3,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=3,column=4,padx=2,pady=2)
        self.button_ = tk.Button(self.frame3,text='',bg=self.color_button,fg=self.color_defaultFg);self.button_.grid(row=3,column=5,padx=2,pady=2)
        
        


        self.root.mainloop()

numberMatrix()
