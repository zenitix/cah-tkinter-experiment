import random
from tkinter import *
from humanitycards import *

class CAH:
    def __init__(self):
        window = Tk()#creates the window
        window.title("Cards Against Humanity")#changes title
        window.configure(background='black')#changes the window color behind the elements
        window.iconbitmap(r'cah.ico')#changes the window icon in the top left corner, disable if you're on linux
        #window.geometry('{}x{}'.format(600, 600))# sets the window size if wanted, right now the window is sizing itself based on the element sizes

        #creates card position labels
        Label(window, text = "Black Card: ", bg = "black", fg="white", font="verdana 10 bold",
              width=16, height = 6, relief = SUNKEN).grid(row = 1, column = 1, sticky = W)
        Label(window, text = "White Card (1): ", bg = "black", fg="white", font="verdana 10 bold",
              width=16, height = 3, relief = SUNKEN).grid(row = 2, column = 1, sticky = W)
        Label(window, text = "White Card (2): ", bg = "black", fg="white", font="verdana 10 bold",
              width=16, height = 3, relief = SUNKEN).grid(row = 3, column = 1, sticky = W)

        
        #anything with self before it, the self is to make sure other parts can see the object
        #without self prefix, things in other def-s can't read assigned objects
        #the "StringVar()" are impotant for the text varible wich are used for changing what the text says
        #the self.ent-s create the changing card text
        #the columnspan is important so the buttons don't fly all over the place
        #wraplength breaks the lines, seems to be in pixels, dispite what the documents might say
        #justify makes the text go left when the line breaks
        #width is in characters and height is in lines
        #anchor will change wich way the text site, in this case to the left, seems to follow the compass in this case but not always true
        self.lbl1 = StringVar()
        self.ent1 = Label(window, textvariable = self.lbl1, width=50, height = 6, relief = SUNKEN, anchor = W,
                          bg = "black", fg="white", font="verdana 10 bold", wraplength = 450, justify = LEFT)
        self.ent1.grid(row=1, column = 2, columnspan = 3)
        self.lbl2 = StringVar()
        self.ent2 = Label(window, textvariable = self.lbl2, width=50, height = 3, relief = SUNKEN, anchor = W,
                          bg = "black", fg="white", font="verdana 10 bold", wraplength = 450, justify = LEFT)
        self.ent2.grid(row=2, column = 2, columnspan = 3)
        self.lbl3 = StringVar()
        self.ent3 = Label(window, textvariable = self.lbl3, width=50, height = 3, relief = SUNKEN, anchor = W,
                          bg = "black", fg="white", font="verdana 10 bold", wraplength = 450, justify = LEFT)
        self.ent3.grid(row=3, column = 2, columnspan = 3)

        #makes button for generating the cards and displaying them
        btcah = Button(window, text = "Generate", bg="black", fg="white", font="verdana 10 bold", width = 15, command = self.gencah)

        #makes a variable for the radial buttons to use, then makes the radial buttons
        #important that radial button all share the same varible, not the chase with check boxes
        #tried setting the radial color to white on black like rest of program, but couldn't see the indicator dot
        self.v1 = IntVar()
        btsinggen = Radiobutton(window, text = "Generate Single", bg = "black", fg = "red", font="verdana 10 bold",
                                relief = RIDGE, variable = self.v1, value = 1)
        btdoubgen = Radiobutton(window, text = "Generate Double", bg = "black", fg = "red",  font="verdana 10 bold",
                                relief = RIDGE, variable = self.v1, value = 2)
        btrandgen = Radiobutton(window, text = "Generate Random", bg = "black", fg = "red",  font="verdana 10 bold",
                                relief = RIDGE, variable = self.v1, value = 3)

        #places the button-button and radial button on the window and controlls their location
        btcah.grid(row = 4, column = 1)
        btsinggen.grid(row = 4, column = 2)
        btdoubgen.grid(row = 4, column = 3)
        btrandgen.grid(row = 4, column = 4)

        window.mainloop()#very important, creates the loop

        #called from the main button, based on what radial buttons are pressed filled the varible labels with text
        #none selected will default random
    def gencah(self):
        #randomly chooses the cards it wants to use each time the button is pressed
        cah1result = random.choice(cah1pick)
        cah2result = random.choice(cah2pick)
        cah3result = random.choice(cah3pick)
        white1 = random.choice(cah2pick)
        white2 = random.choice(cah2pick)
        #used for single option
        if self.v1.get() == 1:
            self.lbl1.set(cah1result)
            self.lbl2.set(cah2result)
            self.lbl3.set(" ")
        #used for double option
        elif self.v1.get() == 2:
            self.lbl1.set(cah3result)
            self.lbl2.set(white1)
            self.lbl3.set(white2)
        #used for random option, chooses if it will use single or double on it's own
        #else means that if no radial option was selected, it will use this too
        #in hindsight, it was really not important to bind a value to the third radial button
        else:
            blackuse = int(random.choice(blackselect))
            if blackuse == 1:
                self.lbl1.set(cah1result)
                self.lbl2.set(cah2result)
                self.lbl3.set(" ")
            if blackuse == 3:
                self.lbl1.set(cah3result)
                self.lbl2.set(white1)
                self.lbl3.set(white2)

CAH()#makes all the things happen
