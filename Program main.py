
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
    global fullscreen, language, incorrect_counter, correct_counter, J
        
    def close_app():
        root.destroy()

    def read_text():
        global text_file, language
        try:
            
            language = translated_combo.get()
            print(language)
        except: pass

        file_path = "Text files\\"+language+".txt"
        print(file_path)
        files = open(file_path, encoding='utf-8')
        text_file = []
        for i in files.readlines():
            add = i.replace("Ã·","÷")
            add = add.replace("\n","")
            text_file.append(add)
        try:
            fullscreen_checkbox.configure(text = text_file[5])
            apply_button.configure(text = text_file[6])
            root.title(text_file[150])
        except: pass

        
    read_text()    

    def switch_screen_toggle():
        global fullscreen
        if fullscreen == False:
            root.attributes("-fullscreen", True)
            fullscreen = True                                                                   #Lets the program know what is happening
        else:
            root.attributes("-fullscreen", False)
            fullscreen = False

    

    root = customtkinter.CTk()
    root.title(text_file[150])                            #Title of the program
    root.geometry("1280x720")                                                                  #The size of the program (startup)
    root.minsize(width=1280, height=720)                                                         #minimum resolution for the program
    root.iconbitmap("images\program_icon.ico")                                                  #icon of the program
    
    

    def scaler(event):                                                                    #scales the background image in the begining to the size of the screen
        global avg_multi, newx_multi
        new_width = event.width                                                              #Gets information about window
        newx_multi = new_width/1920                                                            #scales objects to the x-axis
        new_height = event.height                   
        newy_multi = new_height/1080                                                            #scales objects to the y-axis
        avg_multi = (newx_multi+newy_multi)/2                                                     #scales objects to the average of x and y axis (for non-aspect ratio resolutions)

        if menu_screen_state == True:
            try:
                MS_image = MS_copy_of_image.resize((new_width,new_height))                                       #resizes image
                MS_photo = ImageTk.PhotoImage(MS_image)
                MS_background.config(image = MS_photo)                                                              #configures/updates the background image
                MS_background.image = MS_photo 

                start_button.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi) 
                options_button.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                exit_button.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)                              #adjusts text size to match the screen resolution
                title1.configure(font=("Comic Sans MS Bold",140*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                title2.configure(font=("Comic Sans MS Bold",140*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
            except:
                pass
        
        if options_menu_state == True:
            try:
                OS_image = OS_copy_of_image.resize((new_width,new_height))                                       #resizes image
                OS_photo = ImageTk.PhotoImage(OS_image)
                OS_background.config(image = OS_photo)                                                              #configures/updates the background image
                OS_background.image = OS_photo 

                apply_button.configure(font=("Comic Sans MS Bold",50*newx_multi))
                fullscreen_checkbox.configure(font=("Comic Sans MS Bold",50*newx_multi))
                translated_combo.configure(font=("Comic Sans MS Bold",50*newx_multi))
            except:
                pass

        if level_selection_state == True:
            try:
                LS_image = LS_copy_of_image.resize((new_width,new_height))                                       #resizes image
                LS_photo = ImageTk.PhotoImage(LS_image)
                LS_background.config(image = LS_photo)                                                              #configures/updates the background image
                LS_background.image = LS_photo 

                title3.configure(font=("Comic Sans MS Bold",120*avg_multi))
                lvl1.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl2.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl3.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl4.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl5.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl6.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl7.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl8.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl9.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl10.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl11.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl12.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl13.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl14.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl15.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl16.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl17.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl18.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl19.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
                lvl20.configure(font=("Comic Sans MS Bold",50*avg_multi), width = 140*newx_multi, height = 42*newy_multi)
            except: 
                pass

        if level_menu_state == True:
            try:
                LM_image = LM_copy_of_image.resize((new_width,new_height))                                       #resizes image
                LM_photo = ImageTk.PhotoImage(LM_image)
                LM_background.config(image = LM_photo)                                                              #configures/updates the background image
                LM_background.image = LM_photo

                question.configure(font=("Comic Sans MS Bold",45*avg_multi), wraplength = 855*newx_multi)
                answer3.configure(font=("Comic Sans MS Bold",45*avg_multi), width = newx_multi*375, height = newy_multi*113)
                answer1.configure(font=("Comic Sans MS Bold",45*avg_multi), width = newx_multi*375, height = newy_multi*113)
                answer2.configure(font=("Comic Sans MS Bold",45*avg_multi), width = newx_multi*375, height = newy_multi*113)
                answer4.configure(font=("Comic Sans MS Bold",45*avg_multi), width = newx_multi*375, height = newy_multi*113)

                explanation.configure(font=("Comic Sans MS Bold",45*avg_multi), wraplength = 1305*newx_multi)
            except: pass

            
        

    def options_menu():

        global original_combo, language_list, translated_combo, languages, options_menu_state, OS_background, OS_copy_of_image
        global options_frame, back_button_options_menu, apply_button, fullscreen_checkbox, level_selection_state, menu_screen_state
        global back_button, translated_combo

        menu_screen_state = False                                                            #Lets the program know whats happening
        options_menu_state = True
        level_selection_state = False

        try:
            start_menu_frame.destroy()                                                              #Clears the window
            MS_background.destroy()
            icon_button.destroy()
        except: pass
        

        OS_image = Image.open("images\options_menu.png")                                           #opens the image file
        OS_copy_of_image = OS_image.copy()                                                                #creates a copy of the image file
        OS_photo = ImageTk.PhotoImage(OS_image)
        OS_background = Label(root, image = OS_photo)                                                          #Assigns the image to the label
        OS_background.bind("<Configure>", scaler)                                                     #Configures the image to the screen
        OS_background.pack(fill=BOTH, expand = YES) 
        
        options_frame = customtkinter.CTkFrame(root, border_width=5, corner_radius=30, bg_color="#F1EDE3", fg_color="light grey", border_color="grey", width=200, height=200)
        options_frame.place(relx = 0.35, rely= 0.55, anchor = W)


        languages=googletrans.LANGUAGES                                                     #Obtains languages from google translate
        language_list=list(languages.values())



        original_combo=ttk.Combobox(options_frame,width=20,value=language_list)                    #Creating Comboboxes for languages
        original_combo.current(21)

        
        fullscreen_checkbox = customtkinter.CTkCheckBox(options_frame, text=text_file[5], command=switch_screen_toggle, hover_color="#D3D3D3",font=("Comic Sans MS Bold",30), text_color="#453735")
        fullscreen_checkbox.pack(padx=20 ,pady = 20,fill=BOTH, expand = YES)
        if fullscreen == True:
            fullscreen_checkbox.select()

        
        translated_combo=customtkinter.CTkComboBox(options_frame, values=language_list, font=("Comic Sans MS Bold",30), text_color="#453735", fg_color ="#D3D3D3", state= "readonly")
        translated_combo.set("english")                                                     #Setting default language to english
        translated_combo.pack(padx=20 ,fill=BOTH, expand = YES)
        

        back_button = Image.open("images\Back.png")
        back_button = back_button.resize((50,50))
        back_button_options_menu = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(back_button), command=menu_screen, text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)
        back_button_options_menu.place(relx=0.03, rely=0.95, anchor= CENTER)
        
        
        apply_button = customtkinter.CTkButton(options_frame,text=text_file[6], command= read_text, font=("Comic Sans MS Bold",30), text_color="#453735", corner_radius=60)
        apply_button.pack(padx=20, pady=20 ,fill=BOTH, expand = YES)
    
    def next(choice):
        global correct_counter, incorrect_counter, J, explanation
        if choice == correct_answer:
            next_button = Image.open("images\mext.png")
            next_button = next_button.resize((50,50))
            next_button = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(next_button), command=lambda:level_menu(L+1), text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)

            if L == 20:
                next_button.configure(command = level_selection)
            next_button.place(relx=0.97, rely=0.95, anchor= CENTER)
            correct_counter += 1
            answer1.configure(state= DISABLED)
            answer2.configure(state= DISABLED)
            answer3.configure(state= DISABLED)
            answer4.configure(state= DISABLED)

        else:
            if J != L:
                explanation = customtkinter.CTkLabel(master = root, text=text_file[14+7*(L-1)], text_color="Black", fg_color= "#F1EDE3", font=("Comic Sans MS Bold",25), wraplength = 870)
                explanation.place(relx = 0.5, rely = 0.85, anchor = CENTER)
                J = L
                incorrect_counter += 1
                try:
                    explanation.configure(font=("Comic Sans MS Bold",45*avg_multi), wraplength = 1305*newx_multi)
                except: pass

        if choice == 1:
            answer1.configure(state = DISABLED)
        if choice == 2:
            answer2.configure(state = DISABLED)
        if choice == 3:
            answer3.configure(state = DISABLED)
        if choice == 4:
            answer4.configure(state = DISABLED)
        

    def level_menu(lvl):
        global LM_background, level_selection_frame, LM_copy_of_image, level_menu_state, level_selection_state, question, answer4, answer1, answer2, answer3, L, correct_answer

        if level_selection_state == True:
            try:
                LS_background.destroy()
                level_selection_frame.destroy()
            except: pass

        if level_menu_state == True:
            try:
                LM_background.destroy()
                level_menu_frame.destroy()
            except: pass

        level_selection_state = False
        level_menu_state = True

        L = lvl

        LM_image = Image.open("images\level_menu.png")                                           #opens the image file
        LM_copy_of_image = LM_image.copy()                                                                #creates a copy of the image file
        LM_photo = ImageTk.PhotoImage(LM_image)
        LM_background = Label(root, image = LM_photo)                                                          #Assigns the image to the label
        LM_background.bind("<Configure>", scaler)                                                     #Configures the image to the screen
        LM_background.pack(fill=BOTH, expand = YES)                                                         #packs the label onto the GUI

        level_menu_frame = customtkinter.CTkFrame(master=root, border_width=5, corner_radius=30, bg_color="#F1EDE3", fg_color="light grey", border_color="grey")
        level_menu_frame.place(relx=0.5, rely = 0.55, anchor = CENTER)                                                      #Frame in the start_menu

        correct_answer = int(text_file[13+7*(lvl-1)])

        question = customtkinter.CTkLabel(master = root, text=text_file[8+7*(lvl-1)], font=("Comic Sans MS Bold",30), wraplength=855, text_color="black", fg_color= "white")
        question.place(relx = 0.5, rely = 0.185, anchor = CENTER)

        answer1 = customtkinter.CTkButton(master = level_menu_frame, text = text_file[9+7*(lvl-1)], text_color="white", fg_color= "grey", hover_color="blue", anchor=W, command= lambda:next(1))
        answer1.grid(padx = 20, pady = 20, row = 0, column = 0 )

        answer2 = customtkinter.CTkButton(master = level_menu_frame, text = text_file[10+7*(lvl-1)], text_color="white", fg_color= "grey", hover_color="blue", anchor=W, command= lambda:next(2))
        answer2.grid(padx = 20, pady = 20, row = 0, column = 1 )

        answer3 = customtkinter.CTkButton(master = level_menu_frame, text = text_file[11+7*(lvl-1)], text_color="white", fg_color= "grey", hover_color="blue", anchor=W, command= lambda:next(3))
        answer3.grid(padx = 20, pady = 20, row = 1, column = 0 )

        answer4 = customtkinter.CTkButton(master = level_menu_frame, text = text_file[12+7*(lvl-1)], text_color="white", fg_color= "grey", hover_color="blue", anchor=W, command= lambda:next(4))
        answer4.grid(padx = 20, pady = 20, row = 1, column = 1 )

        

        LM_icon = Image.open("images\maximise_nav.png")                                                    #Maximise/minimise icon
        LM_icon = LM_icon.resize((30,30))
        LM_icon_button = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(LM_icon), command=switch_screen_toggle, text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)
        LM_icon_button.place(x=5, y=5) 

        LM_back_button = Image.open("images\Back.png")
        LM_back_button = LM_back_button.resize((50,50))
        LM_back_button_options_menu = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(LM_back_button), command=level_selection, text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)
        LM_back_button_options_menu.place(relx=0.03, rely=0.95, anchor= CENTER)


     

    def level_selection():
        global LS_background, start_menu_frame, LS_copy_of_image, title3, level_selection_state, level_selection_frame, menu_screen_state, options_menu_state, LS_back_button_options_menu
        global lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10, lvl11, lvl12, lvl13, lvl14, lvl15, lvl16, lvl17, lvl18, lvl19, lvl20, incorrect_counter, correct_counter

        if menu_screen_state == True:
            try:
                MS_background.destroy()
                start_menu_frame.destroy()
            except: pass

        if level_menu_state == True:
            try:
                LM_background.destroy()
            except: pass

        menu_screen_state = False
        options_menu_state = False
        level_selection_state = True

        
        LS_image = Image.open("images\level_selection.png")                                           #opens the image file
        LS_copy_of_image = LS_image.copy()                                                                #creates a copy of the image file
        LS_photo = ImageTk.PhotoImage(LS_image)
        LS_background = Label(root, image = LS_photo)                                                          #Assigns the image to the label
        LS_background.bind("<Configure>", scaler)                                                     #Configures the image to the screen
        LS_background.pack(fill=BOTH, expand = YES)                                                         #packs the label onto the GUI

        level_selection_frame = customtkinter.CTkFrame(master=root, border_width=5, corner_radius=30, bg_color="#F1EDE3", fg_color="light grey", border_color="grey")
        level_selection_frame.place(relx=0.5, rely = 0.6, anchor = CENTER)                                                      #Frame in the start_menu

        title3 = customtkinter.CTkLabel(master = root, text = text_file[7], font=("Comic Sans MS Bold",120), text_color="#453735", fg_color="#F1EDE3")
        title3.place(relx = 0.5, rely = 0.12, anchor = CENTER)

        LS_back_button = Image.open("images\Back.png")
        LS_back_button = LS_back_button.resize((50,50))
        LS_back_button_options_menu = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(LS_back_button), command=menu_screen, text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)
        LS_back_button_options_menu.place(relx=0.03, rely=0.95, anchor= CENTER)

        lvl1 = customtkinter.CTkButton(master = level_selection_frame, text="1", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(1))
        lvl2 = customtkinter.CTkButton(master = level_selection_frame, text="2", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(2))
        lvl3 = customtkinter.CTkButton(master = level_selection_frame, text="3", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(3))
        lvl4 = customtkinter.CTkButton(master = level_selection_frame, text="4", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(4))
        lvl5 = customtkinter.CTkButton(master = level_selection_frame, text="5", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(5))

        lvl1.grid(row = 0, column = 0, padx = 30, pady = 30)
        lvl2.grid(row = 0, column = 1, padx = 0, pady = 30)
        lvl3.grid(row = 0, column = 2, padx = 30, pady = 30)
        lvl4.grid(row = 0, column = 3, padx = 0, pady = 30)
        lvl5.grid(row = 0, column = 4, padx = 30, pady = 30)

        lvl6 = customtkinter.CTkButton(master = level_selection_frame, text="6", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(6))
        lvl7 = customtkinter.CTkButton(master = level_selection_frame, text="7", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(7))
        lvl8 = customtkinter.CTkButton(master = level_selection_frame, text="8", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(8))
        lvl9 = customtkinter.CTkButton(master = level_selection_frame, text="9", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(9))
        lvl10 = customtkinter.CTkButton(master = level_selection_frame, text= "10", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(10))

        lvl6.grid(row = 1, column = 0, padx = 30, pady = 22)
        lvl7.grid(row = 1, column = 1, padx = 0, pady = 22)
        lvl8.grid(row = 1, column = 2, padx = 30, pady = 22)
        lvl9.grid(row = 1, column = 3, padx = 0, pady = 22)
        lvl10.grid(row = 1, column = 4, padx = 30, pady = 22)

        lvl11 = customtkinter.CTkButton(master = level_selection_frame, text="11", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(11))
        lvl12 = customtkinter.CTkButton(master = level_selection_frame, text="12", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(12))
        lvl13 = customtkinter.CTkButton(master = level_selection_frame, text="13", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(13))
        lvl14 = customtkinter.CTkButton(master = level_selection_frame, text="14", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(14))
        lvl15 = customtkinter.CTkButton(master = level_selection_frame, text="15", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(15))

        lvl11.grid(row = 2, column = 0, padx = 30, pady = 22)
        lvl12.grid(row = 2, column = 1, padx = 0, pady = 22)
        lvl13.grid(row = 2, column = 2, padx = 30, pady = 22)
        lvl14.grid(row = 2, column = 3, padx = 0, pady = 22)
        lvl15.grid(row = 2, column = 4, padx = 30, pady = 22)

        lvl16 = customtkinter.CTkButton(master = level_selection_frame, text="16", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(16))
        lvl17 = customtkinter.CTkButton(master = level_selection_frame, text="17", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(17))
        lvl18 = customtkinter.CTkButton(master = level_selection_frame, text="18", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(18))
        lvl19 = customtkinter.CTkButton(master = level_selection_frame, text="19", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(19))
        lvl20 = customtkinter.CTkButton(master = level_selection_frame, text="20", font=("Comic Sans MS Bold",50), hover_color="blue", fg_color="grey", command= lambda:level_menu(20))

        lvl16.grid(row = 3, column = 0, padx = 30, pady = 30)
        lvl17.grid(row = 3, column = 1, padx = 0, pady = 30)
        lvl18.grid(row = 3, column = 2, padx = 30, pady = 30)
        lvl19.grid(row = 3, column = 3, padx = 0, pady = 30)
        lvl20.grid(row = 3, column = 4, padx = 30, pady = 30)

        LS_icon = Image.open("images\maximise_nav.png")                                                    #Maximise/minimise icon
        LS_icon = LS_icon.resize((30,30))
        LS_icon_button = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(LS_icon), command=switch_screen_toggle, text="", width=0, fg_color="#F1EDE3", corner_radius=0, hover=DISABLED)
        LS_icon_button.place(x=5, y=5)                                                                 #Icon is an interactive toggle button

        if L == 20:
            stats = customtkinter.CTkToplevel(master = root, takefocus = True)
            stats.geometry('300x200')
            stats.grab_set()
            stats.title(text_file[151])
            correct_text = text_file[152]+" "+str(correct_counter)
            incorrect_text = text_file[153]+" "+str(incorrect_counter)
            correct = customtkinter.CTkLabel(master = stats, text = correct_text, font = (None, 25))
            incorrect = customtkinter.CTkLabel(master = stats, text = incorrect_text, font =  (None, 25))
            correct.pack()
            incorrect.pack()

            accuracy = "Your accuracy is "+str(float(correct_counter/(correct_counter + incorrect_counter))*100)+"%"
            accuracy_label = customtkinter.CTkLabel(master = stats, text = accuracy, font =  (None, 25))
            accuracy_label.pack()

            result = "Your result is "+str(float(correct_counter/20)*100)+"%"
            result_label = customtkinter.CTkLabel(master = stats, text = result, font =  (None, 25))
            result_label.pack()

            if correct_counter != 20:
                final_msg = text_file[149]
            else:
                final_msg = text_file[148]
            final_msg_label = customtkinter.CTkLabel(master = stats, text = final_msg, font =  (None, 25))
            final_msg_label.pack()

            incorrect_counter = 0
            correct_counter = 0


            

    def menu_screen():
        global MS_background, start_button, options_button, exit_button, start_menu_frame, MS_copy_of_image, icon, icon_button, menu_screen_state, options_menu_state, title1, title2, level_selection_state, level_menu_state


        if options_menu_state == True:
            try:
                OS_background.destroy()
                options_frame.destroy()                
            except: pass

        if level_selection_state == True:
            try:
                LS_background.destroy()
                LS_back_button_options_menu.destroy()
            except: pass

        menu_screen_state = True
        options_menu_state = False
        level_selection_state = False
        level_menu_state= False


        MS_image = Image.open("images\Learn_Arithmetic.png")                                           #opens the image file
        MS_copy_of_image = MS_image.copy()                                                                #creates a copy of the image file
        MS_photo = ImageTk.PhotoImage(MS_image)
        MS_background = Label(root, image = MS_photo)                                                          #Assigns the image to the label
        MS_background.bind("<Configure>", scaler)                                                     #Configures the image to the screen
        MS_background.pack(fill=BOTH, expand = YES)                                                         #packs the label onto the GUI

        start_menu_frame = customtkinter.CTkFrame(master=root, border_width=5, corner_radius=30, bg_color="white", fg_color="light grey", border_color="grey")
        start_menu_frame.place(relx=0.45, rely = 0.7, anchor = CENTER)                                                      #Frame in the start_menu


        title1 = customtkinter.CTkLabel(master = root, text = text_file[0], font=("Comic Sans MS Bold",140), text_color="#453735", fg_color="white")
        title2 = customtkinter.CTkLabel(master = root, text = text_file[1], font=("Comic Sans MS Bold",140), text_color="#453735", fg_color="white")
        title1.place(relx = 0.45, rely = 0.23, anchor = S)
        title2.place(relx = 0.45, rely = 0.27, anchor = N)

        start_button = customtkinter.CTkButton(start_menu_frame, text = text_file[2], font=("Comic Sans MS Bold",50), text_color="#453735", fg_color="#BDBDBD", corner_radius=25, hover_color="#E3E3E3", command = level_selection)
        start_button.pack(padx=20, pady = 20,fill=BOTH, expand = YES)

        options_button = customtkinter.CTkButton(start_menu_frame, text = text_file[3], font=("Comic Sans MS Bold",50), text_color="#453735", fg_color="#BDBDBD", corner_radius=25, hover_color="#E3E3E3", command=options_menu)
        options_button.pack(padx=20,fill=BOTH, expand = YES)

        exit_button = customtkinter.CTkButton(start_menu_frame, text = text_file[4], font=("Comic Sans MS Bold",50), text_color="#453735", fg_color="#BDBDBD", corner_radius=25, hover_color="#E3E3E3", command= close_app)
        exit_button.pack(padx=20, pady = 20,fill=BOTH, expand = YES)

        icon = Image.open("images\maximise.png")                                                    #Maximise/minimise icon
        icon = icon.resize((30,30))
        icon_button = customtkinter.CTkButton(root, image=ImageTk.PhotoImage(icon), command=switch_screen_toggle, text="", width=0, fg_color="#453735", corner_radius=0, hover=DISABLED)
        icon_button.place(x=5, y=5)                                                                 #Icon is an interactive toggle button

    menu_screen()

                                          


    root.mainloop()


#configurations of the program
fullscreen = False
language = "english"

menu_screen_state = False
options_menu_state = False
level_menu_state = False
level_selection_state = False
incorrect_counter = 0
correct_counter = 0
J = 0
L = False
Program()
