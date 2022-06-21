import tkinter as tk

class numberMatrix: #get the keys pressed (this code is for a windowed app)

    def __init__(self) -> None:
        self.setup()


    def change_mode(self,mode): #change the mode. Args: literal 1,2,3
            self.mode = mode

    def on_start(self):#default args and config
        #TODO
        self.mode = 1


    #scrren functions
    def screen_clear_mode(self):
        self.screen_widget.delete('1.0','lineend')
    def screen_clear_result(self):
        self.screen_widget.delete('3.0','lineend')
    def screen_clear_input(self):
        self.screen_widget.delete('2.0','lineend')

    def screen_write_input(self,to_write):
        self.screen_widget.insert("2.0 lineend",to_write)
    def screen_write_input(self,to_write):
        self.screen_widget.insert("3.0 lineend",to_write)
    
    def screen_set_mode(self,mode='',rounded='',getresult=''):
        m,r,g = self.screen_widget.get('1.0','lineend').split()

        mode = mode if mode else m
        mode = 'Shift' if mode == 2 else 'Alpha' if mode ==3 else 'Normal'
        rounded = rounded if rounded else r
        getresult = getresult if getresult else g
        to_add=(mode,rounded,getresult)
        self.screen_widget.delete('1.0','lineend')
        self.screen_widget.insert('1.0','    '.join(to_add))


    def setup(self):
        #mode:
        #1: normal
        #2: shift
        #3: alpha

        self.mode = 0

        #create the graphic matrix (simulating a cassio calc)
        self.root = tk.Tk()
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
        self.title = 'Scientific Calculator'
        self.titleLab = tk.Label(self.frame1,text=self.title);self.titleLab.pack()
        #add the screen
        self.screen_widget = tk.Text(self.frame2,height=5);self.screen_widget.pack()  #change the heigh to better perform

        #add navegate buttons
        self.button_shift = tk.Button(self.frame2_2,text='shift',command=lambda:self.change_mode(2)).grid(row=0,column=0)
        self.button_alpha = tk.Button(self.frame2_2,text='alpha',command=lambda:self.change_mode(3)).grid(row=0,column=1)
        self.mode_setup = tk.StringVar(value='mode' if self.mode != 2 else 'setup')
        self.button_mode_setup = tk.Button(self.frame2_2,textvariable=self.mode_setup).grid(row=0,column=6)
        self.button_on = tk.Button(self.frame2_2,text='On',command=self.on_start).grid(row=0,column=7)
        self.button_up = tk.Button(self.frame2_2,text=' ^ ').grid(row=0,column=3)
        self.button_down = tk.Button(self.frame2_2,text=' v ').grid(row=0,column=4)
        self.button_left = tk.Button(self.frame2_2,text=' < ').grid(row=0,column=2)
        self.button_right = tk.Button(self.frame2_2,text=' > ').grid(row=0,column=5)
        #add scientific buttons


        self.root.mainloop()

numberMatrix()