import sqlite3
import sys



class atm():


    def is_prime(n):

        if (n % 2) == 0:#here we use this logic when the amount of 50$ notes is bigger than the amount we have
            return (n - 1) # we take one less 50$ note , so the number is prime and the rest of the mony will be in notes of 20$
        else:
            return (n)
                            
    def checkatmdb(): # a function to report after every succesful transcaction the amount of money remaining , the 20$ and 50$ notes.
        try:
            conn = sqlite3.connect('atm.db')
            cur=conn.execute("SELECT  START_MONEY,COMB_OF20,COMB_OF50 FROM atminit")
            for r in cur.fetchall():  
                smoney,twedol,fifdol = r
        except sqlite3.Error as e1:
            raise e1
        conn.close()
        print('The remaining amount is'+'       '+str(smoney)+'$')
        print('The remaining 20$ notes are'+'   '+str(twedol))
        print('The remaining 50$ notes are'+'   '+str(fifdol))

      

    def moneytrans(comb20,comb50,money): # a function to update the table with the available money and the rest of the the notes.
        try:
            conn = sqlite3.connect('atm.db')
            cur=conn.execute("UPDATE atminit SET START_MONEY=?,COMB_OF20=?,COMB_OF50=?",(smoney-money,twedol-comb20,fifdol-comb50))
            conn.commit()
        except sqlite3.Error as e1:
            raise e1
        conn.close()

    #Each we start the app we connect to the db to get the the money avalable and the notes of 20$ and 50$ dollars
    # smoney = START_MONEY from table atminit
    # twedol = COMB_OF20 the remaining number of 20$ dollar notes .
    # fifdol = COMB_OF50 the remaining number of 50$ dollar notes .
    # setting them as global to use them in the fucntion moneytrans for the update of the table atminit

    global smoney,twedol,fifdol
    
    try:
        conn = sqlite3.connect('atm.db')
        cur=conn.execute("SELECT START_MONEY,COMB_OF20,COMB_OF50 FROM atminit")      
        for r in cur.fetchall():  
            smoney,twedol,fifdol = r
    except sqlite3.Error as e1:
        raise e1
    conn.close()

    #Asking the user for the amount he wishes to withdraw
    user_in = int(input('Please enter the money you wish to withdraw?\n'))

    if user_in > smoney :
        print('not enough money to withdraw from the ATM , please try gain later!\n')
        open_cmd = input('Press enter to Finish\n')
        sys.exit() # if the customer asks for more money than the available , stopping the programm

    if user_in > 50 :
        ftcomb = user_in / 50 #  the number that if multiplied by 50 will give the uamount the user asked
        int_part,dec_part = divmod(ftcomb,1) # getting the Integer part of that number
        if int_part > fifdol : # if we need more 50$ dollars notes than we cuurently have
            int_part = is_prime(fifdol) # the combination of 50$ for the above statement
            rem_money = user_in - (int_part*50)
        else:    
            rem_money = user_in - (int_part*50)  # by  subtracting the amount of  int_part*50 from user_in we get an amount smaller than 50
        if (rem_money % 20)==0: # if the statement is true , that means rem_money can be calculated to combinations of 20$
            twcomb = rem_money / 20
            if (twcomb > twedol) or (int_part > fifdol):# if we need more 20$ or 50$ dollar notes than we cuurently have
                print('The combinations of 50$ and 20$ notes cannot fulfill your request, please try another amount')
                open_cmd = input('Press enter to Finish\n')
                sys.exit()
            moneytrans(twcomb,int_part,user_in)
            print('Thanks for your transcaction')
        elif (user_in % 20)==0:
            twcomb = user_in / 20
            if twcomb > twedol :# if we need more 20$ dollar notes than we cuurently have
                print('We are out of 20$ dollar notes , please try another amount')
                open_cmd = input('Press enter to Finish\n')
                sys.exit()
            moneytrans(twcomb,0,user_in)
            print('Thanks for your transcaction')    
        else:
            print('The combinations of 20 and 50 dollars notes cannot  fulfil your request')
            open_cmd = input('Press enter to Finish\n')
            sys.exit()
    elif user_in < 50:
        if (user_in % 20)==0: # for amounts smaller than 50$ we only check if there combinations of 20$
            twcomb = user_in / 20
            if twcomb > twedol :# if we need more 20$ dollar notes than we cuurently have
                print('We are out of 20$ dollar notes , please try another amount')
                open_cmd = input('Press enter to Finish\n')
                sys.exit()
            moneytrans(twcomb,0,user_in)
            print('Thanks for your transcaction')
        else:
            print('The combinations of 20 and 50 dollars notes cannot  fulfil your request')
            open_cmd = input('Press enter to Finish\n')
            sys.exit()              
    else:  #that means the user asked for a note of 50$
        if (fifdol > 1):
            moneytrans(0,1,user_in)
            print('Thanks for your transcaction')
        else:
            print('The are no more  50 dollar notes , please try another amount')
            open_cmd = input('Press enter to Finish\n')
            sys.exit()

    #Calling the function after the succesful transcaction for the report
    checkatmdb()
    #keeping the command line open!
    open_cmd = input('Press enter to Finish\n')
    
            
        

        
           
        

        

        

    
        



          



      
    
