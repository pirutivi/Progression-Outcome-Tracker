from graphics import*

outer_loop_flag=True
Progress=0
Trailer=0
Retriever=0
Exclude=0

def barchart():
    labels=['Progress','Trailer','Retriever','Exclude']
    colors=["pink","lightblue","violet","lightgreen"]
    total=Progress+Trailer+Retriever+Exclude

    win=GraphWin("Histogram",700,600)
    data=[Progress,Trailer,Retriever,Exclude]

    total_text=Text(Point(550,80),str(total)+"outcomes in total")
    total_text.setStyle('bold italic')
    total_text.draw(win)
    bar_width=50
    bar_spacing=20
    maximum_data_value=max(data)

    for i,value in enumerate(data):
        bar_height=(value/maximum_data_value)*200

        #Calculate coordinates for the bar
        x1=50+i*(bar_width+bar_spacing)
        y1=250-bar_height
        x2=x1+bar_width
        y2=250

        #Create and draw the rectangle of the bar
        bar=Rectangle(Point(x1,y1),Point(x2,y2))
        bar.setFill(colors[i])
        bar.draw(win)

        #Create and draw the value above the bar
        value_label=Text(Point((x1+x2)/2,y1-10),f"{value}")
        value_label.draw(win)

        #Create and draw the label under the bar
        label=Text(Point((x1+x2)/2,y2+10),f"{labels[i]}")
        label.draw(win)
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        pass

Progress=0
Trailer=0
Retriever=0
Exclude=0
number_of_outcomes=0

list_pass=[]
list_defer=[]
list_fail=[]

list_a=[120,0,0]
list_b=[100,20,0],[100,0,20]
list_c=[80,40,0],[80,20,20],[80,0,40],[60,60,0],[60,40,20],[60,20,40],[60,0,60],[40,80,0],[40,60,20],[40,40,40],[40,20,60],[20,100,0],[20,80,20],[20,60,40],[20,40,60],[0,120,0],[0,100,20],[0,80,40],[0,60,60]
list_d=[40,0,80],[20,20,80],[20,0,100],[0,0,120],[0,40,80],[0,20,100]
list_e=[0,20,40,60,80,100,120]

while outer_loop_flag:
    while True:
        try:
            pass_credit = int(input("Please enter your credits at pass:"))
            defer_credit = int(input("Please enter your credits at defer:"))
            fail_credit = int(input("Please enter your credits at fail:"))
            break
        except ValueError:
            print("Integer required")

    if pass_credit in list_e and defer_credit in list_e and fail_credit in list_e:
        if pass_credit+defer_credit+fail_credit==120:
            credits=[pass_credit,defer_credit,fail_credit]

            if pass_credit==120 and defer_credit==0 and fail_credit==0:
                print("Progress")
                result='Progress'
            elif credits in list_b:
                print("Progress(module trailer)")
                result='Trailer'
            elif credits in list_c:
                print("Do not progress(module retriever)")
                result='Retriever'
            else:
                print("Exclude")
                result='Exclude'
            if result=='Progress':
                Progress+=1
            elif result=='Trailer':
                Trailer+=1
            elif result=='Retriever':
                Retriever+=1
            else:
                Exclude+=1
                
            number_of_outcomes += 1

            list_pass.append(pass_credit)
            list_defer.append(defer_credit)
            list_fail.append(fail_credit)

            while True:
                Repeat = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                Repeat = Repeat.lower()
                print('')
            
                if Repeat == 'y':
                  break  
                elif Repeat == 'q':
                     outer_loop_flag=False
                     barchart()
                continue
        else:
            print("Total incorrect")
    else:
        print("Out of range")


    
