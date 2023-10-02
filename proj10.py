
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
   
    deck = Deck()
    deck.shuffle()
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    column7 = []
    tableau = []
    foundation = [[],[],[],[]]
    waste = []
    
    
    for count in range (7):
        if count == 0:
            column1.append(deck.deal())
            column2.append(deck.deal())
            column3.append(deck.deal())
            column4.append(deck.deal())
            column5.append(deck.deal())
            column6.append(deck.deal())
            column7.append(deck.deal())
        if count == 1:
            column2.append(deck.deal())
            column3.append(deck.deal())
            column4.append(deck.deal())
            column5.append(deck.deal())
            column6.append(deck.deal())
            column7.append(deck.deal())
        if count == 2:
            column3.append(deck.deal())
            column4.append(deck.deal())
            column5.append(deck.deal())
            column6.append(deck.deal())
            column7.append(deck.deal())
        if count == 3:
            column4.append(deck.deal())
            column5.append(deck.deal())
            column6.append(deck.deal())
            column7.append(deck.deal())
        if count == 4:
            column5.append(deck.deal())
            column6.append(deck.deal())
            column7.append(deck.deal())
        if count == 5:
            column6.append(deck.deal())
            column7.append(deck.deal())
        if count == 6:
            column7.append(deck.deal())
    for card in range(len(column1)-1):
        column1[card].flip_card()
    for card in range(len(column2)-1):
        column2[card].flip_card()
    for card in range(len(column3)-1):
        column3[card].flip_card()
    for card in range(len(column4)-1):
        column4[card].flip_card()
    for card in range(len(column5)-1):
        column5[card].flip_card()
    for card in range(len(column6)-1):
        column6[card].flip_card()
    for card in range(len(column7)-1):
        column7[card].flip_card()
    
    tableau.append(column1)
    tableau.append(column2)
    tableau.append(column3)
    tableau.append(column4)
    tableau.append(column5)
    tableau.append(column6)
    tableau.append(column7)
    stock_deck = deck
    stock_list = []
    stock_list.append(stock_deck.deal())
    stock_list.reverse()
    waste_pop = stock_list.pop()
    waste.append(waste_pop)


    return tableau, stock_deck, foundation, waste
    
    
def display(tableau, stock, foundation, waste):

    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):

    if stock.is_empty() == False:
        stock = stock
        waste = waste
        stock_list = []
        stock_list.append(stock.deal())
        stock_list.reverse()
        waste_pop = stock_list.pop()
        waste.append(waste_pop)
        return True
    else:
        return False
    
       
def waste_to_tableau( waste, tableau, t_num ):

    t_num = int(t_num)
    waste_pop = waste.pop()
    if len(tableau[t_num]) == 0 and waste_pop.rank() != 13:
        waste.append(waste_pop)
        return False
    if len(tableau[t_num]) == 0 and waste_pop.rank() == 13:
        tableau[t_num].append(waste_pop)
        return True
    try:
        lastnum = tableau[t_num].pop()
        lastnumrank = lastnum.rank()-1
        lastnumsuit = lastnum.suit()
    except IndexError:
        tableau[t_num].append(lastnum)
        waste.append(waste_pop)
        return False
    if waste_pop.suit() == 1 or waste_pop.suit() == 4:
        if lastnumsuit == 2 or lastnumsuit == 3:
            if waste_pop.rank() == lastnumrank:
                tableau[t_num].append(lastnum)
                tableau[t_num].append(waste_pop)
                return True
            else:
                tableau[t_num].append(lastnum)
                waste.append(waste_pop)
                return False
        else:
            tableau[t_num].append(lastnum)
            waste.append(waste_pop)
            return False
        
    if waste_pop.suit() == 2 or waste_pop.suit() == 3:
            if lastnumsuit == 1 or lastnumsuit == 4:
                if waste_pop.rank() == lastnumrank:
                    tableau[t_num].append(lastnum)
                    tableau[t_num].append(waste_pop)
                    return True
                else:
                    tableau[t_num].append(lastnum)
                    waste.append(waste_pop)
                    return False
            else:
                tableau[t_num].append(lastnum)
                waste.append(waste_pop)
                return False
    

def waste_to_foundation( waste, foundation, f_num ):

    f_num = int(f_num)
    waste_pop = waste.pop()
        
    if len(foundation[f_num]) == 0 and waste_pop.rank() != 1:
        waste.append(waste_pop)
        return False
    if len(foundation[f_num]) == 0 and waste_pop.rank() == 1:
        foundation[f_num].append(waste_pop)
        return True
    try:
        lastnum = foundation[f_num].pop()
        lastnumrank = lastnum.rank()+1
        lastnumsuit = lastnum.suit()
    except IndexError:
        foundation[f_num].append(lastnum)
        waste.append(waste_pop)
        return False
    if waste_pop.suit() == lastnumsuit and waste_pop.rank() == lastnumrank:
        foundation[f_num].append(lastnum)
        foundation[f_num].append(waste_pop)
        return True
    else:
        foundation[f_num].append(lastnum)
        waste.append(waste_pop)
        return False
        
            

def tableau_to_foundation( tableau, foundation, t_num, f_num ):

    t_num = int(t_num)
    f_num = int(f_num)
    lastnumt = tableau[t_num].pop()
    if len(foundation[f_num]) == 0 and lastnumt.rank() == 1:
        foundation[f_num].append(lastnumt)
        for column in tableau:
            try:
                lastcard = column.pop()
            except IndexError:
                continue
            if lastcard.is_face_up() == False:
                lastcard.flip_card()
                column.append(lastcard)
            else:
                column.append(lastcard)
        return True
    if len(foundation[f_num]) == 0 and lastnumt.rank() != 0:
        tableau[t_num].append(lastnumt)
        return False
        
    
    try:
        lastnumf = foundation[f_num].pop()
    
    except IndexError:
        foundation[f_num].append(lastnumf)
        return False
    
    if lastnumt.rank() == lastnumf.rank()+1 and lastnumt.suit()==lastnumf.suit():
        foundation[f_num].append(lastnumf)
        foundation[f_num].append(lastnumt)
        for column in tableau:
            try:
             lastcard = column.pop()
            except IndexError:
                continue
            if lastcard.is_face_up() == False:
                lastcard.flip_card()
                column.append(lastcard)
            else:
                column.append(lastcard)
        return True
    else:
        foundation[f_num].append(lastnumf)
        tableau[t_num].append(lastnumt)
        return False


def tableau_to_tableau( tableau, t_num1, t_num2 ):

    t_num1 = int(t_num1)
    t_num2 = int(t_num2)
    lastnumt1 =  tableau[t_num1].pop()
    if len(tableau[t_num2]) == 0 and lastnumt1.rank() == 13:
        tableau[t_num2].append(lastnumt1)
        for column in tableau:
            try:
                lastcard = column.pop()
            except IndexError:
                continue
            if lastcard.is_face_up() == False:
                lastcard.flip_card()
                column.append(lastcard)
            else:
                column.append(lastcard)
        return True
    if len(tableau[t_num2]) == 0 and lastnumt1.rank() != 13:
        tableau[t_num1].append(lastnumt1)
        return False
    lastnumt2 = tableau[t_num2].pop()
    
    if lastnumt1.suit() == 1 or lastnumt1.suit() == 4:
        if lastnumt2.suit() == 2 or lastnumt2.suit() == 3:
            if lastnumt1.rank() == lastnumt2.rank()-1:
                tableau[t_num2].append(lastnumt2)
                tableau[t_num2].append(lastnumt1)
                for column in tableau:
                    try:
                        lastcard = column.pop()
                    except IndexError:
                        continue
                    if lastcard.is_face_up() == False:
                        lastcard.flip_card()
                        column.append(lastcard)
                    else:
                        column.append(lastcard)
                return True
            else:
                tableau[t_num2].append(lastnumt2)
                tableau[t_num1].append(lastnumt1)
                return False
        else:
            tableau[t_num2].append(lastnumt2)
            tableau[t_num1].append(lastnumt1)
            return False
    if lastnumt1.suit() == 2 or lastnumt1.suit() == 3:
        if lastnumt2.suit() == 1 or lastnumt2.suit() == 4:
            if lastnumt1.rank() == lastnumt2.rank()-1:
                tableau[t_num2].append(lastnumt2)
                tableau[t_num2].append(lastnumt1)
                for column in tableau:

                    lastcard = column.pop()
        
                    if lastcard.is_face_up() == False:
                        lastcard.flip_card()
                        column.append(lastcard)
                    else:
                        column.append(lastcard)
                return True
            else:
                tableau[t_num2].append(lastnumt2)
                tableau[t_num1].append(lastnumt1)
                return False
        else:
            tableau[t_num2].append(lastnumt2)
            tableau[t_num1].append(lastnumt1)
            return False
                
    
    
    
def check_win (stock, waste, foundation, tableau):

    if len(stock)==0:
        if len(waste)==0:
            for column in tableau:
                if len(column)==0:
                    continue
                else:
                    return False
            return True
        else:
            return False
    else:
        return False
    

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    tableau, stock, foundation, waste = initialize()
    print(MENU)
    display(tableau, stock, foundation, waste)
    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
    listuser = parse_option(userchoice)
    while listuser[0] != 'Q':
        if listuser == None:
            display(tableau, stock, foundation, waste)
            userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
            listuser = parse_option(userchoice)
        if listuser[0] == "TT":
            result = tableau_to_tableau(tableau,listuser[1]-1,listuser[2]-1)
            if result == True:
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
            if result == False:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
        if listuser[0] == 'TF':
            result = tableau_to_foundation(tableau,foundation,listuser[1]-1,listuser[2]-1)
            if result == True:
                win = check_win (stock, waste, foundation, tableau)
                if win == True:
                    print('You Won!')
                    display(tableau, stock, foundation, waste)
                    break
                if win == False:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
                    while listuser ==  None:
                        display(tableau, stock, foundation, waste)
                        userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                        listuser = parse_option(userchoice)
            if result == False:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
        if listuser[0] == 'WT':
            result = waste_to_tableau( waste, tableau, listuser[1]-1 )
            if result == True:
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
            if result == False:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
        if listuser[0] == 'WF':
            result = waste_to_foundation( waste, foundation, listuser[1]-1 )
            if result == True:
                win = check_win (stock, waste, foundation, tableau)
                if win == True:
                    print('You Won!')
                    display(tableau, stock, foundation, waste)
                    break
                if win == False:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
                    while listuser ==  None:
                        display(tableau, stock, foundation, waste)
                        userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                        listuser = parse_option(userchoice)
            if result == False:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
        if listuser[0] == 'SW':
            result = stock_to_waste( stock, waste )
            if result == True:
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
            if result == False:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
                while listuser ==  None:
                    display(tableau, stock, foundation, waste)
                    userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                    listuser = parse_option(userchoice)
        if listuser[0] == 'R':
            tableau, stock, foundation, waste = initialize()
            print(MENU)
            display(tableau, stock, foundation, waste)
            userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
            listuser = parse_option(userchoice)
            while listuser ==  None:
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
        if listuser[0] == 'H':
            print(MENU)
            userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
            listuser = parse_option(userchoice)
            while listuser ==  None:
                display(tableau, stock, foundation, waste)
                userchoice = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                listuser = parse_option(userchoice)
        if listuser[0] == 'Q':
            break

if __name__ == '__main__':
     main()
