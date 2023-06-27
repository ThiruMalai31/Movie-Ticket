list=["","Leo","Demon Slayer-Kimetsu No Yaiba: To the Swordsmith Village","Pathu thala","Viduthalai","Jailer"]
def makepayment(Amount):
    print("\n\t\t\t\tSelect Bank Account")
    print("\n\t\t\t\t1.SBI   2.Indian   3.Karur   4.IOB   5.UPI\t\n\n")
    bank=int(input("\t\t\t\tEnter any bank\t"))
    if bank==1:
                            print("\n\t\t\t\tPay Amount ",Amount," from your SBI\n")
                            card=input("\t\t\t\tEnter Account Number\t")
                            while(len(card)!=16):
                                        print("\n\t\t\t\tInvalid Card Number\n")
                                        card=input("\t\t\t\tEnter Account Number\t")       
                            print("\n\t\t...............................Transaction Succesfull...................................")
    elif bank==2:
                            print("\n\t\t\t\tPay Amount ",Amount," from your Indian\n")
                            card=input("\t\t\t\tEnter Account Number\t")
                            while(len(card)!=16):
                                        print("\n\t\t\t\tInvalid Card Number\n")
                                        card=input("\t\t\t\tEnter Account Number\t")
                            print("\n\t\t...............................Transaction Succesfull...................................")
    elif bank==3:
                            print("\n\t\t\t\tPay Amount ",Amount," from your Karur\n")
                            card=input("\t\t\t\tEnter Account Number\t")
                            while(len(card)!=16):
                                        print("\n\t\t\t\tInvalid Card Number\n")
                                        card=input("\t\t\t\tEnter Account Number\t")
                            print("\n\t\t......................Transaction Succesfull...................................")
    elif bank==4:
                            print("\n\t\t\t\tPay Amount ",Amount," from your IOB\n")
                            card=input("\t\t\t\tEnter Account Number\t")
                            while(len(card)!=16):
                                        print("\n\t\t\t\tInvalid Card Number\n")
                                        card=input("\t\t\t\tEnter Account Number\t")
                            print("\n\t\t......................Transaction Succesfull...................................")
    elif bank==5:
                            print("\n\t\t\t\tPay Amount ",Amount," from your UPI\n")
                            card=input("\t\t\t\tEnter UPI Number\t")
                            print("\n\t\t......................Transaction Succesfull...................................")



def info(select,theatre_names,time,Movie_Name):
    name=input("\t\t\t\tEnter Your Name\t")
    with open("History.txt",'a') as f:
            f.write("Name:")
            f.write(name)
            f.write("\n")
    ph_no=input("\n\t\t\t\tEnter Your Phone_Number\t")
    while len(ph_no)!=10:
        print("\n\t\t\t\tInvalid Phone Number...")
        print("\nEnter Valid Phone number\t")
        ph_no=input("\n\t\t\t\tEnter Your Phone_Number\t")
    with open("History.txt",'a') as f:
            f.write("Phone_Number:")
            f.write(ph_no)
            f.write("\n")
    No_tickets=input("\n\t\t\t\tEnter No of Tickets\t")
    with open("History.txt",'a') as f:
            f.write("No of Tickets:")
            f.write(No_tickets)
            f.write("\n")
    print("\n\n\t\t\t\tEnter type of Seating\n\t\t\t\t1.Normal_Seat Rs.120\t\t2.Platinum Seat Rs.200\n\n\t\t\t\t")
    Seat_Type=input("Select Seat Type\t\t")
    with open("History.txt",'a') as f:
            f.write("Seat_Type")
            f.write(Seat_Type)
            f.write("\n")
    print("\n\n\n\t\t\t\tYour Details\n")
    print("\t\t\t\tName:",name)
    print("\t\t\t\tPh_no:",ph_no)
    print("\t\t\t\tMovie_Name:",list[Movie_Name])
    with open("History.txt",'a') as f:
            f.write("Movie_Name")
            f.write(list[Movie_Name])
            f.write("\n")
    print("\t\t\t\tTheatre_Name:",theatre_names[select])
    with open("History.txt",'a') as f:
            f.write("Theatre_Name:")
            f.write(theatre_names[select])
            f.write("\n")
    print("\t\t\t\tTime:",time[select])
    with open("History.txt",'a') as f:
            f.write("Time:")
            f.write(time[select])
            f.write("\n")
    print("\t\t\t\tNo_of_Tickets:",No_tickets)
    print("\n\t\t\t\tSeat_Type:",Seat_Type)
    Amountt=0
    if(Seat_Type=="1"):
        Amountt=str(120*int(No_tickets))
    elif(Seat_Type=="2"):
        Amountt=str(200*int(No_tickets))
    print("\n\t\t\t\tTotal Amount:",Amountt)
    with open("History.txt",'a') as f:
            f.write("Total Amount:")
            f.write(Amountt)
            f.write("\n\n")
    nxt=input("\n\t\t\t\tPress y Key To Make Payment\t")
    if(nxt=='y'):
        makepayment(Amountt)






def theatre(movie):
    
    if movie==1:
        print("\t\t\t\tList Of Theatres\n")
        print("\t\t\t\tVetri Cinemas\n")
        print("\t\t\t\t1.Vetri Time-10:00 AM      2.Lakshan Time-10:00 AM      3.Laksha  Time-10:00  AM\n\n")
        print("\t\t\t\tShunmuga theatre\n")
        print("\t\t\t\t4.Screen 1  Time-2:30 PM      5.Screen 2  Time-5:30 PM\n\n") 
        print("\t\t\t\t6.Solavandhan Time - 7:30 PM\n\n")
        print("\t\t\t\tTamil Jeya Theatre\n")
        print("\t\t\t\t7.screen 1 Time-7:30 PM      8.screen   Time-10:30 PM 2\n\n")
        theatre_names=["","vetri","Lakshan","Laksha","Shunmuga_Screen_1","Shunmuga_Screen_2","Solavandhan","Tamil_Jeya_Screen_1","Tamil_Jeya_screen_2"]
        time=["","10:00 AM","10:00 AM","10:00 AM","2:30 PM","02:30 PM","07:30 PM","07:30 PM","10:00 PM"]
        select=int(input("\t\t\t\tSelect Any Show and Time\t "))
        info(select,theatre_names,time,movie)
    elif movie==2:
        print("\t\t\t\tList Of Theatres\n")
        print("\t\t\t\tGuru Cinemas\n")
        print("\t\t\t\t1.Guru Time-2:30 PM      2.Jeyam Time-4:30 PM      3.Multiplex  Time-7:00  PM\n\n")
        print("\t\t\t\Midland theatre\n")
        print("\t\t\t\t4.Screen 1  Time-3:30 PM      5.Screen 2  Time-5:30 PM\n\n") 
        print("\t\t\t\t6.Ambiga Time - 7:30 PM\n\n")
        print("\t\t\t\tJazzs Theatre\n")
        print("\t\t\t\t7.screen 1 Time-10:00 AM      8.screen 2  Time-7:30 PM \n\n")
        theatre_names=["","Guru","Jeyam","Multiplex","Midland_Screen_1","Midland_Screen_2","Ambiga","Jazzs_Screen_1","Jazzs_screen_2"]
        time=["","2:30 PM","4:30 PM","7:30 PM","3:30 PM","5:30 PM","07:30 PM","10:00 AM","7:30 PM"]
        select=int(input("\t\t\t\tSelect Any Show and Time\t "))
        info(select,theatre_names,time,movie)
    elif movie==3:
        print("\t\t\t\tList Of Theatres\n")
        print("\t\t\t\tVetri Cinemas\n")
        print("\t\t\t\t1.Vetri  Time - 12:30 PM      2.Lakshan Time - 12:30 PM      3.Laksha  Time-12:30 PM\n\n")
        print("\t\t\t\tMidland theatre\n")  
        print("\t\t\t\t4.Screen 1  Time - 7:30 PM      5.Screen 2  Time - 10:30 PM  \n\n")  
        print("\t\t\t\t6.Ambiga  Time - 2:30 PM \n")
        print("\t\t\t\tJazzs theatre\n")
        print("\t\t\t\t7.screen 1  Time - 4:30 PM      8.screen 2  Time - 12:30 PM")
        theatre_names=["","Vetri","Lakshan","Laksha","Midland_Screen_1","Midland_Screen_2","Ambiga","Jazzs_Screen_1","Jazzs_Jeya_screen_2"]
        time=["","12:30 PM","12:30 PM","12:30 PM","7:30 PM","10:30 PM","02:30 PM","04:30 AM","12:30 PM"]
        select=int(input("Select Any Show and Time\t "))
        info(select,theatre_names,time,movie)
    elif movie==4:
        print("\t\t\t\tList Of Theatres\n")
        print("\t\t\t\tGuru Cinemas\n")
        print("\t\t\t\t1.Guru  Time -5:30 PM      2.Jeyam Time 6:30 PM      3.Multiplex  Time- 8:30 PM\n\n")
        print("\t\t\t\tMidland theatre\n")
        print("\t\t\t\t4.Screen 1 Time - 1:30 PM      5.Screen 2  Time- 2:30 PM  \n\n") 
        print("\t\t\t\t6.Ambiga  Time - 9:30 PM")
        print("\t\t\t\tJazzs theatre\n")
        print("\t\t\t\t7.screen 1  Time - 11:00 AM      8.screen 2  Time:4:30 PM")
        theatre_names=["","Guru","Jeyam","Multiplex","Midland_Screen_1","Midland_Screen_2","Ambiga","Jazzs_Screen_1","Jazzs_Jeya_screen_2"]
        time=["","05:30 PM","06:30 PM","08:30 PM","1:30 PM","02:30 PM","09:30 PM","11:00 AM","04:30 PM"]
        select=int(input("Select Any Show and Time\t "))
        info(select,theatre_names,time,movie)
    elif movie==5:
        print("\t\t\t\tList Of Theatres\n")
        print("\t\t\t\tVetri Cinemas\n")
        print("\t\t\t\t1.Vetri  Time - 02:30 PM      2.Lakshan Time - 11:30 PM      3.Laksha  Time-01:30 PM")
        print("\t\t\t\tMidland theatre\n")
        print("\t\t\t\t4.Screen 1  Time - 9:30 PM      5.Screen 2  Time - 11:30 PM  \n\n")  
        print("\t\t\t\t6.Ambiga  Time - 3:30 PM \n")
        print("\t\t\t\tJazzs theatre\n")
        print("\t\t\t\t7.screen 1  Time - 5:30 PM      8.screen 2  Time - 07:30 PM")
        theatre_names=["","Vetri","Lakshan","Laksha","Midland_Screen_1","Midland_Screen_2","Ambiga","Jazzs_Screen_1","Jazzs_Jeya_screen_2"]
        time=["","02:30 PM","11:30 PM","01:30 PM","09:30 PM","11:30 PM","03:30 PM","05:30 AM","07:30 PM"]
        select=int(input("Select Any Show and Time\t "))
        info(select,theatre_names,time,movie)
            




def details(movie):
        if movie==1:
                        print(" Leo is an upcoming Indian Tamil-language action film directed by Lokesh Kanagaraj who co-wrote the script with Rathna Kumar and Deeraj Vaidy.it is produced by S. S. Lalit Kumar, under Seven Screen Studio , co-produced by Jagadish Palanisamy")
                        print("Produced by: S. S. Lalit Kumar, Jagadish Palanisamy\nDirected by: Lokesh Kanagaraj\nCinematography: Manoj Paramahamsa\nStarring: Vijay ")
                        print("\n\nBook TicKets")
                        print("Press y To Continue")
                        c=input()
                        if c=="y":
                                    theatre(movie)
        elif movie==2:
            print("Genre: Fantasy, Adventure, Action, Anime Original Language: Japanese Director: Haruo Sotozaki Writer: Koyoharu Gotoge Release Date (Theaters): Mar 3, 2023 wide Runtime: 1h 50m Distributor")
            print("\n\nBook TicKets")
            print("Press y To Continue")
            a=input()
            if(a=='y'):
                theatre(movie)
        elif movie==3:
            print("Pathu Thala ( transl. Ten-Headed) is a 2023 Indian Tamil -language neo-noir action thriller film directed by Obeli N.")
            print("\n\nBook TicKets")
            print("Press y To Continue")
            b=input()
            if b=='y':
                theatre(movie)
        elif movie==4:
            print("Viduthalai Part 1 (transl. Liberation) is a 2023 Indian Tamil-language period crime thriller film written and directed by Vetrimaaran.[5][6] Produced by Elred Kumar under the banners of RS Infotainment.[7] It is adapted from the short story Thunaivan (transl. Companion) written by B. Jeyamohan.The film stars Soori and Vijay Sethupathi. It was presented by RS Infotainment.")
            print("\n\nBook TicKets")
            print("Press y To Continue")
            d=input()
            if(d=='y'):
                theatre(movie);
        elif movie==5:
            print("Jailer is an upcoming Indian Tamil-language action comedy film written and directed by Nelson and produced by Kalanithi Maran of Sun Pictures. It stars Rajinikanth, Shiva Rajkumar, Tamannaah and Ramya...")

            print("Director: Nelson\nProducer: Kalanithi Maran\nWriter: Nelson (director)\nMusic: Anirudh Ravichander\nStudio: Sun Pictures\n\n")
            print("\n\nBook TicKets\n")
            print("Press y To Continue\t")
            e=input()
            if(e=='y'):
                theatre(movie)





print("\t\t\t\t--------------------")
print("\t\t\t\tMovie Ticket Booking")
print("\t\t\t\t--------------------")
print("\t\t\t\t1.Movie Tickets")
print("\t\t\t\t2.Booked Movies History")
print("\t\t\t\t3.Upcoming Movies")
print("\t\t\t\t4.Exit")

enter=int(input("\n\n\n\t\t\t\tEnter Any Number\t"))
while enter>5:
    print("Enter Valid Number")
    enter=int(input("\n\n\n\t\t\t\tEnter Any Number\t"))


if enter==1:
        print("\t\t\t\t1.Leo")
        print("\t\t\t\t2.Demon Slayer-Kimetsu No Yaiba: To the Swordsmith Village")
        print("\t\t\t\t3.Pathu Thala")
        print("\t\t\t\t4.Viduthalai")
        print("\t\t\t\t5.Jailer\t")
        movie=int(input("\n\n\n\t\t\t\tSelect Any Movie\t"))
        
        while(movie>5):
                    print("\n\t\t\t\tInvalid Option")
                    movie=int(input("\n\n\n\t\t\t\tSelect Any Movie\t"))
        details(movie)
elif enter==2:
        with open("History.txt") as f:
            for read in f:
                print(read, end = '')
elif enter==3:
        print("\t\t\t\t1.Ponniyin Selvan\n")
        print("\t\t\t\t2.Indian 2\n")
        print("\t\t\t\t3.Kanguva\n")
        print("\t\t\t\t4.Japan\n")
        print("\t\t\t\t5.Ayalaan\n")
elif enter==4:
        print("\t\t\t\t.....Thank You.....")
elif enter>4:
        print("\t\t\t\tInvalid Option\n")
