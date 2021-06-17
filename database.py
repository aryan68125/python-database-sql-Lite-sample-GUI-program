#this program demonstrates how to use drop down boxes
from tkinter import *
#if you want to use sqlite3 database just import the database library
import sqlite3

#import scrollable textView
import tkinter.scrolledtext as scrolledtext

window = Tk()
window.title("Database program")
#setting up the window size to be 400x400 size
window.geometry("500x600")
#setting up the minimum size and maximum size for the application window
# set minimum window size value
window.minsize(500, 600)
 
# set maximum window size value
window.maxsize(500, 600)

#CREATING A FRAME THAT WILL CONTAIN ALL the wifgets related to input of the data
#frame is a widhet so it can be used like any other widget
#padx and pady here will pad the area inside the custom frame that the user has created
frame_input_field = LabelFrame(window,text="Input your details",padx=5,pady=5)
#putting our cutom frame in our application on pur screen
#padx and pady will pad the area outside the custome frame that the user has create
#padx=10,pady=10 will come outside the frame that we have created here
frame_input_field.grid(row=0,column=0,padx=10,pady=10)

#database SQL Lite
'''
this function will create a database
'''
def create_database():
    global database_connect
    global cursor_of_database
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()

    #create a table
    #address is the name of the table
    #column names first_name, last_name, address,city,state,zipcode
    #text is datatype , integer is a datatype specifying which data type each column of a table holds
    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database.execute("""
    CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
    """)


#create a function to delete a record from the database
def delete():
    global database_connect
    global cursor_of_database
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()
    
    #now we can perform delete operation on a record present in the database
    #after WHERE <enter the column of the table where you want to search and delete>
    '''
    oid is an integer in your sql Lite database and user_ID_input.get() returns a string 
    normally your would do str(user_ID_input.get()) to make it work but with tkinter you do't need to do that
    '''
    cursor_of_database.execute("DELETE FROM addresses WHERE oid="+user_ID_input.get())

    #now any time we make a change to our database we want to commit those changes to our database
    database_connect.commit()

    #now we need to close the connection to our database when the operation is complete
    database_connect.close()

'''
create a submit function for the button that will handle the background database operation
to save the data that has been entered by the user in the input fields (EditText) of the application
'''
def Save():
    global database_connect
    global cursor_of_database
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()

    #insert the data from the input fields into the table of the database
    '''
    VALUES(:dummy variable_1, :dummy variable_2, :dummy variable_3
         {
	          create a python dictionary that will have a key value pair
	          key = dummy variables
	          value = entry widgets (EditText) name
         }
    )
    '''
    cursor_of_database.execute("INSERT INTO addresses VALUES(:first_name,:last_name,:address,:city,:state,:zipcode)",{
                "first_name": first_name.get(), 
                "last_name":Last_name.get(), 
                "address":address_of_person.get(), 
                "city":city_name.get(), 
                "state":state_name.get(), 
                "zipcode":zipcode_number.get()

              })

    #now any time we make a change to our database we want to commit those changes to our database
    database_connect.commit()

    #now we need to close the connection to our database when the operation is complete
    database_connect.close()

    #delete all the entry done by the user in the input field
    first_name.delete(0,END)
    Last_name.delete(0,END)
    address_of_person.delete(0,END)
    city_name.delete(0,END)
    state_name.delete(0,END)
    zipcode_number.delete(0,END)

'''
the function show_saved_data will show the contents of the database that is already there
to the user in the outputfield textView
'''
def show_saved_data():
    #creating a new window
    window2 = Toplevel()
    window2.title("output window")
    #setting up the window2 size to be 400x400 size
    window2.geometry("1000x500")
    #setting up the minimum size and maximum size for the application window2
    # set minimum window2 size value
    window2.minsize(1000, 500)
    # set maximum window2 size value
    window2.maxsize(1000, 500)
    global database_connect
    global cursor_of_database
    global scroll
    global eula
    global Delete_button
    global user_ID_input
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()

    #to query the database
    #oid will give you primary key
    cursor_of_database.execute("SELECT *,oid FROM addresses ")
    read_data_list_of_tuples = cursor_of_database.fetchall()
    print(read_data_list_of_tuples)

    #the code below will deal how the data is extracted from the database 
    #since the data recieved from the database is a list of tuples that holds the data we can 
    #use for loop to loop through the list and get hold of the individual tuples inside the list
    Name=''
    add=''
    city=''
    state =''
    zip_code=''
    persons_info=''
    userID = ''
    for data_tuple in read_data_list_of_tuples:
        Name = str(data_tuple[0]) + " " +str(data_tuple[1])
        add = str(data_tuple[2])
        city = str(data_tuple[3])
        state = str(data_tuple[4])
        zip_code = str(data_tuple[5])
        userID = str(data_tuple[6])
        persons_info += "User ID = " +userID+"\n" + "Name = " +Name +"\n"+ "Address = " +add+ "\n" + "City = " +city+ "\n" + "State = " + state +"\n"+ "zip code = " + zip_code + "\n" + "\n"
        #the above for loop will allow us to get a single tuple 
    
    # Vertical (y) Scroll Bar
    scroll = Scrollbar(window2)
    scroll.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Text(window2, wrap=NONE, yscrollcommand=scroll.set)
    eula.delete(1.0,"end") #deleting the previous content present on the text View
    eula.insert("1.0", persons_info)
    eula.pack(side="left")

    # Configure the scrollbars
    scroll.config(command=eula.yview)

    #create an input field that will accept the unique user ID oid from the user
    #and the delete button will then use that user ID oid to search delete the record from the database
    user_ID_input= Entry(window2)
    user_ID_input.pack(side=TOP, fill=X,pady=20)

    #create a button for delete operation
    Delete_button = Button(window2,text = "Delete",command=delete)
    Delete_button.pack(side = BOTTOM, fill = X,pady=20)
    delete_lable =Label(window2,text="Enter the user ID",anchor='w')
    delete_lable.pack(side=TOP, fill=X)

    #query_label = Label(frame_output_field, text=persons_info,anchor="w")
    #query_label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    #now any time we make a change to our database we want to commit those changes to our database
    database_connect.commit()

    #now we need to close the connection to our database when the operation is complete
    database_connect.close()

'''
this function will handle the editing function of the existing record present in the database
'''
def edit_saved_data_window():
    #creating a new window3
    global window3
    window3 = Toplevel()
    window3.title("Select Window")
    #setting up the window2 size to be 400x400 size
    window3.geometry("640x500")
    #setting up the minimum size and maximum size for the application window2
    # set minimum window2 size value
    window3.minsize(640, 500)
    # set maximum window2 size value
    window3.maxsize(640, 500)

    global user_ID_input_edit_window
    global Save_changes_button
    global show_record_button
    global Select_Frame
    global update_button

    #create a frame that will contain all the widgets related to selecting a record from the database
    Select_Frame = LabelFrame(window3,text="Select Record",width=400, height=200,padx=5,pady=5)
    Select_Frame.grid(row=0,column=0,sticky='nsew')
    
    #create an input field that will accept the unique user ID oid from the user
    #and the delete button will then use that user ID oid to search delete the record from the database
    user_ID_input_edit_window= Entry(Select_Frame)
    user_ID_input_edit_window.grid(row=1,column=0,sticky='EW',padx=10,pady=10)

    ##
    
    #this button should show the selected record 
    show_selected_record_button = Button(Select_Frame,text = "select record",command=show_the_selected_record)
    show_selected_record_button.grid(row=3,column=0,sticky='EW',padx=10,pady=10)

    #create an update button
    update_button = Button(Select_Frame,text = "update the selected record",command=update_record_input)
    update_button.grid(row=4,column=0,sticky='EW',padx=10,pady=10)   
    update_button.config(state = DISABLED)

    Save_changes_lable =Label(Select_Frame,text="Enter the user ID",anchor='w')
    Save_changes_lable.grid(row=0,column=0,sticky='EW',padx=10,pady=10)

'''
the function below handles the select record function of window3
'''
Selected_record_label = Label()
def show_the_selected_record():
    global database_connect
    global cursor_of_database
    global persons_info
    global Selected_record_label
    global Selected_Record_Frame
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()

    #to query the database
    #oid will give you primary key
    cursor_of_database.execute("SELECT *,oid FROM addresses ")
    read_data_list_of_tuples = cursor_of_database.fetchall()
    print(read_data_list_of_tuples)

    #the code below will deal how the data is extracted from the database 
    #since the data recieved from the database is a list of tuples that holds the data we can 
    #use for loop to loop through the list and get hold of the individual tuples inside the list
    Name=''
    add=''
    city=''
    state =''
    zip_code=''
    persons_info=''
    userID = ''
    compare_oid = ''
    index = int(user_ID_input_edit_window.get())
    flag = 0
    for data_tuple in read_data_list_of_tuples:
        compare_oid = str(data_tuple[6])
        if index == int(compare_oid):
            flag = 1
            Name = str(data_tuple[0]) + " " +str(data_tuple[1])
            add = str(data_tuple[2])
            city = str(data_tuple[3])
            state = str(data_tuple[4])
            zip_code = str(data_tuple[5])
            userID = str(data_tuple[6])
            persons_info += "User ID = " +userID+"\n" + "Name = " +Name +"\n"+ "Address = " +add+ "\n" + "City = " +city+ "\n" + "State = " + state +"\n"+ "zip code = " + zip_code + "\n" + "\n"
            #the above for loop will allow us to get a single tuple 
        
    if flag==0:
        persons_info = "User ID not Found"
        update_button.config(state = DISABLED)
    elif flag==1:
        update_button.config(state = NORMAL)

    # create a Selected_Record_Frame here
    Selected_Record_Frame = LabelFrame(window3,text="Selected Record",width=400, height=200,padx=5,pady=5)
    Selected_Record_Frame.grid(row=0,column=1,sticky='nsew',padx=5,pady=5)
    Selected_Record_Frame.grid_rowconfigure(0, weight=1)
    Selected_Record_Frame.grid_columnconfigure(0, weight=1)
    Selected_Record_Frame.grid_propagate(False)

    #delete the previous text of the label
    Selected_record_label.config(text="")
    Selected_record_label = Label(Selected_Record_Frame,text=persons_info,anchor='w')
    Selected_record_label.grid(row=0,column=0,sticky='W')

    #now any time we make a change to our database we want to commit those changes to our database
    database_connect.commit()

    #now we need to close the connection to our database when the operation is complete
    database_connect.close()

def update_record_input():
    #creating a new window3
    global window4
    window4 = Toplevel()
    window4.title("Edit Window")
    #setting up the window2 size to be 400x400 size
    window4.geometry("400x500")
    #setting up the minimum size and maximum size for the application window2
    # set minimum window2 size value
    window4.minsize(400, 500)
    # set maximum window2 size value
    window4.maxsize(400, 500)

    global database_connect
    global cursor_of_database
    global persons_info
    global Selected_record_label
    global Selected_Record_Frame

    #create global variables for editText of edit Window
    global first_name_edit_record_frame
    global Last_name_edit_record_frame
    global address_of_person_edit_record_frame
    global city_name_edit_record_frame
    global state_name_edit_record_frame
    global zipcode_number_edit_record_frame
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()

    #to query the database
    #oid will give you primary key
    cursor_of_database.execute("SELECT * FROM addresses WHERE oid="+user_ID_input_edit_window.get())
    read_data_list_of_tuples = cursor_of_database.fetchall()
    print("\n"+ str(read_data_list_of_tuples))

    #editText 
    first_name_edit_record_frame = Entry(window4 ,width=30)
    first_name_edit_record_frame.grid(row=0,column=1,padx=10,pady=10)

    Last_name_edit_record_frame = Entry(window4 ,width=30)
    Last_name_edit_record_frame.grid(row=1,column=1,padx=10,pady=10)

    address_of_person_edit_record_frame = Entry(window4 , width=30)
    address_of_person_edit_record_frame.grid(row=2,column=1,padx=10,pady=10)

    city_name_edit_record_frame = Entry(window4 , width=30)
    city_name_edit_record_frame.grid(row=3,column=1,padx=10,pady=10)

    state_name_edit_record_frame = Entry(window4 , width=30)
    state_name_edit_record_frame.grid(row=4,column=1,padx=10,pady=10)

    zipcode_number_edit_record_frame = Entry(window4 , width=30)
    zipcode_number_edit_record_frame.grid(row=5,column=1,padx=10,pady=10)

    #the code below will deal how the data is extracted from the database 
    #since the data recieved from the database is a list of tuples that holds the data we can 
    #use for loop to loop through the list and get hold of the individual tuples inside the list
    First_Name=''
    Last_name=''
    add=''
    city=''
    state =''
    zip_code=''
    persons_info=''
    for data_tuple in read_data_list_of_tuples:
        first_name_edit_record_frame.insert(0,data_tuple[0])
        Last_name_edit_record_frame.insert(0,data_tuple[1])
        address_of_person_edit_record_frame.insert(0,data_tuple[2])
        city_name_edit_record_frame.insert(0,data_tuple[3])
        state_name_edit_record_frame.insert(0,data_tuple[4])
        zipcode_number_edit_record_frame.insert(0,data_tuple[5])

    #textView
    Lable_first_name_edit_record_frame = Label(window4 , text="First Name",anchor='w')
    Lable_first_name_edit_record_frame.grid(row=0,column=0,padx=10,pady=10)

    Lable_last_name_edit_record_frame= Label(window4 , text="Last Name", anchor='w')
    Lable_last_name_edit_record_frame.grid(row=1,column=0,padx=10,pady=10)

    Lable_address_of_person_edit_record_frame= Label(window4 , text="Address", anchor='w')
    Lable_address_of_person_edit_record_frame.grid(row=2,column=0,padx=10,pady=10)

    Lable_city_name_edit_record_frame= Label(window4 , text="City", anchor='w')
    Lable_city_name_edit_record_frame.grid(row=3,column=0,padx=10,pady=10)

    Lable_state_name_edit_record_frame= Label(window4, text="State", anchor='w')
    Lable_state_name_edit_record_frame.grid(row=4,column=0,padx=10,pady=10)

    Lable_zipcode_number_edit_record_frame= Label(window4 , text="Zip Code",anchor='w')
    Lable_zipcode_number_edit_record_frame.grid(row=5,column=0,padx=10,pady=10)

    #create a button for edit operation should open a new window
    Save_changes_button = Button(window4, text="Save Changes",command=update_the_selected_record_in_Edit_window)
    Save_changes_button.grid(row=6,column=0,sticky='EW',padx=10,pady=10)

    #now any time we make a change to our database we want to commit those changes to our database
    database_connect.commit()

    #now we need to close the connection to our database when the operation is complete
    database_connect.close()

def update_the_selected_record_in_Edit_window():
    global database_connect
    global cursor_of_database
    global persons_info
    global Selected_record_label
    global Selected_Record_Frame
    #create a database or connect to a already existing database
    #sqlite3.connect("name of the database that we want to connect to")
    #if the dabase doesn't already exist then this command will create the database named address_book.db for us and it will save it in whatever directory we are currently in
    database_connect = sqlite3.connect("address_book.db")

    #now we need to create a cursor
    #cursor is responsible for getting and setting data to the database
    cursor_of_database = database_connect.cursor()
    record_id = user_ID_input_edit_window.get()
    cursor_of_database.execute("""
             UPDATE addresses SET 
             first_name = :first,
             last_name = :last,
             address = :address,
             city = :city,
             state = :state,
             zipcode = :zipcode
             WHERE oid = :oid""", 
             {
             "first" : first_name_edit_record_frame.get(),
             "last" : Last_name_edit_record_frame.get(),
             "address" : address_of_person_edit_record_frame.get(),
             "city" : city_name_edit_record_frame.get(),
             "state" : state_name_edit_record_frame.get(),
             "zipcode" : zipcode_number_edit_record_frame.get(),

             "oid" : record_id
             }
             )

    #to query the database
    #oid will give you primary key
    cursor_of_database.execute("SELECT * FROM addresses WHERE oid="+user_ID_input_edit_window.get())
    read_data_list_of_tuples = cursor_of_database.fetchall()
    print("\n"+ str(read_data_list_of_tuples))

    #now any time we make a change to our database we want to commit those changes to our database
    database_connect.commit()

    #now we need to close the connection to our database when the operation is complete
    database_connect.close()


    #now here we can close the edit window after completing the update record process
    window4.destroy()

#editText
first_name = Entry(frame_input_field, width=30)
first_name.grid(row=0,column=1,padx=10,pady=10)

Last_name = Entry(frame_input_field, width=30)
Last_name.grid(row=1,column=1,padx=10,pady=10)

address_of_person = Entry(frame_input_field, width=30)
address_of_person.grid(row=2,column=1,padx=10,pady=10)

city_name = Entry(frame_input_field, width=30)
city_name.grid(row=3,column=1,padx=10,pady=10)

state_name = Entry(frame_input_field, width=30)
state_name.grid(row=4,column=1,padx=10,pady=10)

zipcode_number = Entry(frame_input_field, width=30)
zipcode_number.grid(row=5,column=1,padx=10,pady=10)

#textView
Lable_first_name = Label(frame_input_field, text="First Name = ", anchor='w')
Lable_first_name.grid(row=0,column=0,padx=10,pady=10)

Lable_last_name = Label(frame_input_field, text="Last Name = ", anchor='w')
Lable_last_name.grid(row=1,column=0,padx=10,pady=10)

Lable_address_of_person = Label(frame_input_field, text="address = ", anchor='w')
Lable_address_of_person.grid(row=2,column=0,padx=10,pady=10)

Lable_city_name = Label(frame_input_field, text="city= ", anchor='w')
Lable_city_name.grid(row=3,column=0,padx=10,pady=10)

Lable_state_name = Label(frame_input_field, text="state = ", anchor='w')
Lable_state_name.grid(row=4,column=0,padx=10,pady=10)

Lable_zipcode_number = Label(frame_input_field, text="zip code= ",anchor='w')
Lable_zipcode_number.grid(row=5,column=0,padx=10,pady=10)

#now create a submit button
save_button = Button(frame_input_field,text = "save info",command=Save,width = 50,anchor='w')
save_button.grid(row=6,column=0,padx=10,pady=10, columnspan=2)

#now we will create a query button
show_saved_data_button = Button(frame_input_field,text = "show saved data" , command=show_saved_data,width = 50,anchor='w')
show_saved_data_button.grid(row=7,column=0,padx=10,pady=10,columnspan=2)

#now we will create a edit button
edit_saved_data_button = Button(frame_input_field,text = "edit saved data" , command=edit_saved_data_window,width = 50,anchor='w')
edit_saved_data_button.grid(row=8,column=0,padx=10,pady=10,columnspan=2)

#create a button to create a database
#now we will create a query button
create_database_button = Button(frame_input_field,text = "press the button to create a database" , command=create_database,width = 50,anchor='w')
create_database_button.grid(row=9,column=0,padx=10,pady=10,columnspan=2)

window.mainloop()