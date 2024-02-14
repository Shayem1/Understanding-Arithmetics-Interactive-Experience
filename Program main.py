
from tkinter import *
import customtkinter
import math
from tkinter import ttk, messagebox                                                                         #Importing packages that are required for the program to run
from PIL import Image, ImageTk
import googletrans
import textblob
import time
import os

def Program():
    global fullscreen, apply
        
    def close_app():
        root.destroy()

    def switch_screen_toggle():
        global fullscreen
        if fullscreen == False:
            root.attributes("-fullscreen", True)
            fullscreen = True                                                                   #Lets the program know what is happening
        else:
            root.attributes("-fullscreen", False)
            fullscreen = False


    root = customtkinter.CTk()
    root.title("Understanding Arithmetics: Interactive Experience")                            #Title of the program
    root.geometry("1280x720")                                                                  #The size of the program (startup)
    root.minsize(width=1280, height=720)                                                         #minimum resolution for the program
    root.iconbitmap("images\program_icon.ico")                                                  #icon of the program
    
    

    def scaler(event):                                                                    #scales the background image in the begining to the size of the screen
        new_width = event.width                                                              #Gets information about window
        newx_multi = new_width/1920                                                            #scales objects to the x-axis
        new_height = event.height                   
        newy_multi = new_height/1080                                                            #scales objects to the y-axis
        avg_multi = (newx_multi+newy_multi)/2                                                     #scales objects to the average of x and y axis (for non-aspect ratio resolutions)

        try:
            image = copy_of_image.resize((new_width,new_height))                                       #resizes image
            photo = ImageTk.PhotoImage(image)
            background.config(image = photo)                                                              #configures/updates the background image
            background.image = photo                                                                     #Deletes old images --> increases efficiency
        except:pass

        if menu_screen_state == True:
            try:
                start_button.configure(font=("Comic Sans MS Bold",50*avg_multi)) 
                options_button.configure(font=("Comic Sans MS Bold",50*avg_multi))
                exit_button.configure(font=("Comic Sans MS Bold",50*newx_multi))                              #adjusts text size to match the screen resolution
            except:
                pass
            
        
        if options_menu_state == True:
            try:
                apply_button.configure(font=("Comic Sans MS Bold",50*newx_multi))
                fullscreen_checkbox.configure(font=("Comic Sans MS Bold",50*newx_multi))
                translated_combo.configure(font=("Comic Sans MS Bold",50*newx_multi))
            except:
                pass
            
        
    def translate_text():
        global start, options, exit, apply, fullscreen_text
        try:                                                                                #Getting the languages from the dictionary Keys
            for key, value in languages.items():                                            #Get the "From Language" key
                if (value == original_combo.get()):
                    from_language_key=key
            for key,value in languages.items():                                             #Get the "To Language" key
                if (value ==translated_combo.get()):
                    to_language_key=key
            
            if translated_combo.get() == "english":                                         #English can't be translated to english
                '''example.configure(text = "example text in english")'''                         #Translating to english will set it to defualt text
                start = "START"
                options = "OPTIONS"
                exit = "EXIT"
                apply = "APPLY"
                fullscreen_text = "FULLSCREEN"


        

            if translated_combo.get() != "english":                                         #Runs this if the selected language was not english
                
                '''example = (textblob.TextBlob("example text in english").translate(from_lang=from_language_key, to=to_language_key))'''
                start = (textblob.TextBlob("START").translate(from_lang=from_language_key, to=to_language_key))
                options = (textblob.TextBlob("OPTIONS").translate(from_lang=from_language_key, to=to_language_key))
                exit = (textblob.TextBlob("EXIT").translate(from_lang=from_language_key, to=to_language_key))
                apply = (textblob.TextBlob("APPLY").translate(from_lang=from_language_key, to=to_language_key))
                fullscreen_text = (textblob.TextBlob("FULLSCREEN").translate(from_lang=from_language_key, to=to_language_key))
                
            for j in range(0,int(len(languages.values()))):                                 #Translating to selected language
                if language_list[j]==translated_combo.get():
                    original_combo.current(j)
            
        
        except Exception as e:
            messagebox.showerror("Translator",e)

        if menu_screen_state == True:                                                                   #Checks which objects to change
            try:
                start_button.configure(text=start)                                                      #Applies translation
                options_button.configure(text=options)
                exit_button.configure(text=exit)
            except:pass
        
        if options_menu_state == True:
            try:
                apply_button.configure(text=apply)
                fullscreen_checkbox.configure(text=fullscreen_text)
            except:pass
        

    def options_menu():

        global original_combo, language_list, translated_combo, languages, options_menu_state, background, copy_of_image
        global options_frame, back_button_options_menu, apply_button, fullscreen_text, fullscreen_checkbox
        global back_button

        menu_screen_state = False                                                            #Lets the program know whats happening
        options_menu_state = True

        try:
            start_menu_frame.destroy()                                                              #Clears the window
            background.destroy()
            icon_button.destroy()
        except: pass
        

        image = Image.open("images\options_menu.png")                                           #opens the image file
        copy_of_image = image.copy()                                                                #creates a copy of the image file
        photo = ImageTk.PhotoImage(image)
        background = Label(root, image = photo)                                                          #Assigns the image to the label
        background.bind("<Configure>", scaler)                                                     #Configures the image to the screen
        background.pack(fill=BOTH, expand = YES) 
        
        options_frame = customtkinter.CTkFrame(root, border_width=5, corner_radius=30, bg_color="#F1EDE3", fg_color="light grey", border_color="grey", width=200, height=200)
        options_frame.place(relx = 0.35, rely= 0.55, anchor = W)


        languages=googletrans.LANGUAGES                                                     #Obtains languages from google translate
        language_list=list(languages.values())

        original_combo=ttk.Combobox(options_frame,width=20,value=language_list)                    #Creating Comboboxes for languages
        original_combo.current(21)

        
        fullscreen_checkbox = customtkinter.CTkCheckBox(options_frame, text=fullscreen_text, command=switch_screen_toggle, hover_color="#D3D3D3",font=("Comic Sans MS Bold",30), text_color="#453735")
        fullscreen_checkbox.pack(padx=20 ,pady = 20,fill=BOTH, expand = YES)
        if fullscreen == True:
            fullscreen_checkbox.select()
        
        translated_combo=customtkinter.CTkComboBox(options_frame, values=language_list, font=("Comic Sans MS Bold",30), text_color="#453735")
        translated_combo.set("english")                                                     #Setting default language to english
        translated_combo.pack(padx=20 ,fill=BOTH, expand = YES)
        
        back_button = Image.open("images\Back.png")
        back_button = back_button.resize((50,50))
        back_button_options_menu = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(back_button), command=menu_screen, text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)
        back_button_options_menu.place(relx=0.03, rely=0.95, anchor= CENTER)
        
        apply_button = customtkinter.CTkButton(options_frame,text=apply, command= translate_text, font=("Comic Sans MS Bold",30), text_color="#453735", corner_radius=60)
        apply_button.pack(padx=20, pady=20 ,fill=BOTH, expand = YES)
         



    def menu_screen():
        global background, start_button, options_button, exit_button, start_menu_frame, copy_of_image, icon, icon_button, menu_screen_state, options_menu_state

        try:
            background.destroy()
            options_frame.destroy()
            back_button_options_menu.destroy()
        except:
            pass

        menu_screen_state = True
        options_menu_state = False


        image = Image.open("images\Learn_Arithmetic.png")                                           #opens the image file
        copy_of_image = image.copy()                                                                #creates a copy of the image file
        photo = ImageTk.PhotoImage(image)
        background = Label(root, image = photo)                                                          #Assigns the image to the label
        background.bind("<Configure>", scaler)                                                     #Configures the image to the screen
        background.pack(fill=BOTH, expand = YES)                                                         #packs the label onto the GUI

        start_menu_frame = customtkinter.CTkFrame(master=root, border_width=5, corner_radius=30, bg_color="white", fg_color="light grey", border_color="grey")
        start_menu_frame.place(relx=0.45, rely = 0.7, anchor = CENTER)                                                      #Frame in the start_menu




        start_button = customtkinter.CTkButton(start_menu_frame, text = start, font=("Comic Sans MS Bold",50), text_color="#453735", fg_color="#BDBDBD", corner_radius=25, hover_color="#E3E3E3")
        start_button.pack(padx=20, pady = 20,fill=BOTH, expand = YES)

        options_button = customtkinter.CTkButton(start_menu_frame, text = options, font=("Comic Sans MS Bold",50), text_color="#453735", fg_color="#BDBDBD", corner_radius=25, hover_color="#E3E3E3", command=options_menu)
        options_button.pack(padx=20,fill=BOTH, expand = YES)

        exit_button = customtkinter.CTkButton(start_menu_frame, text = exit, font=("Comic Sans MS Bold",50), text_color="#453735", fg_color="#BDBDBD", corner_radius=25, hover_color="#E3E3E3", command= close_app)
        exit_button.pack(padx=20, pady = 20,fill=BOTH, expand = YES)

        icon = Image.open("images\maximise.png")                                                    #Maximise/minimise icon
        icon = icon.resize((30,30))
        icon_button = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(icon), command=switch_screen_toggle, text="", width=0, fg_color="#453735", corner_radius=0, hover=DISABLED)
        icon_button.place(x=5, y=5)                                                                 #Icon is an interactive toggle button

    menu_screen()

                                          


    root.mainloop()


#configurations of the program
start = "START"
options = "OPTIONS"
exit = "EXIT"
apply = "APPLY"
fullscreen_text = "FULLSCREEN"
fullscreen = False

Program()
