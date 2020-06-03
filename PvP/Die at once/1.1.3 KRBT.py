print("                     Welcome to VAN (PvP) by Richard.")
print("                                                        1.2.3")

input("     WE HAVE THREE HEROS:(press enter to continue)")
print("     YOU CAN USE 3 AFTER THE 4TH ROUND AND 4ROUNDS AFTER.")
print("     BRUCE : |HP=150|a_10|1_强化a或2|2_+20HP   |3_   +50HP  |")
print("               THE HIGHEST HP IS 150")
print("   RICHARD : |HP=150|a_15|1_+10HP   |2_  30    |3_  ANI'HP/2|")
print("             生命值小于等于三十，a=20,2=40")
print("      KATE : |HP=250|a_10|1_+30HP   |2_100HP   |3_伤害(250-HP)/2|")
print("              THE HIGHEST HP IS 250")
print("  TONY : |HP=150|a=10|1_三回合持续伤害，每回合10.|2_+20HP|3_伤害自己10HP，抉择：敌方HP-45 or 三回合持续攻击15/round|")
print("         |4.消灭TONY并以LUIS大王代替之。LUIS：HP=100 a=20 1_ 30  2_+20HP   3_ 持续三回合攻击15/round|")

PLAYER1=input("Now , player1 choose the hero:")

while PLAYER1 != "BRUCE" and PLAYER1 != "RICHARD" and PLAYER1 != "KATE" and PLAYER1 != "TONY":
    PLAYER1=input("Now , player1 choose the hero:")
    
if PLAYER1=="BRUCE":
    HPI=150
    NI=150
if PLAYER1=="RICHARD":
    HPI=150
    NI=150
if PLAYER1=="KATE":
    HPI=250
    NI=250
if PLAYER1=="TONY":
    HPI=150
    NI=150

    
PLAYER2=input("Now , player2 choose the hero:")

while PLAYER2 != "BRUCE" and PLAYER2 != "RICHARD" and PLAYER2 != "KATE" and PLAYER2 != "TONY":
    PLAYER2=input("Now , player2 choose the hero:")
    
if PLAYER2=="BRUCE":
    HPII=150
    NII=150
if PLAYER2=="RICHARD":
    HPII=150
    NII=150
if PLAYER2=="KATE":
    HPII=250
    NII=250
if PLAYER2=="TONY":
    HPII=150
    NII=150

input("(press enter to continue)")

MODE=input("CHOOSE YOUR GAME MODE: 1-血战到底 2-打死你.")

print("               AND NOW THE GAME BEGINS")
print("               IF YOU DIED IN 1-19 ROUND ")
print("               YOU ARE NOT THE LOSER")
print("               YOU CAN STILL ADD HP!!!!!")
print("               NEVER GIVE UP!")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while HPI>0 and HPII>0: 
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    PL1=input("            NOW , PLAYER 1 CHOOSE WHAT TO DO.")
    if PLAYER1=="BRUCE":
        if PL1=="a":
            HPII=HPII-10
        if PL1=="1":
            BNM1=input("a or 2")
            if BNM1=="a":
                if HPI<=140:
                    HPI=HPI+10
                else:
                    HPI=150
                HPII=HPII-10
            if BNM1=="2":
                if HPI<=130:
                    HPI=HPI+20
                else:
                    HPI=150
                HPII=HPII-5
        if PL1=="2":
            if HPI<=130:
                HPI=HPI+20
            else:
                HPI=150
        if PL1=="3":
            if HPI<=100:
                HPI=HPI+50
            else:
                HPI=150
    if PLAYER1=="RICHARD":
        if PL1=="a":
            if HPI>30:
                HPII=HPII-15
            else:
                HPII=HPII-20
        if PL1=="1":
            if HPI<=140:
                HPI=HPI+10
            else:
                HPI=150
        if PL1=="2":
            if HPI>30:
                HPII=HPII-30
            else:
                HPII=HPII-40
        if PL1=="3":
            HPII=HPII/2
    if PLAYER1=="KATE":
        if PL1=="a":
            HPII=HPII-10
        if PL1=="1":
            if HPI<=220:
                HPI=HPI+30
            else:
                HPI=250
        if PL1=="2":
            HPI=100
        if PL1=="3":
            HPII=HPII-(250-HPI)/2
    if PLAYER1=="TONY":
        TO1=0
        TOTO1=0
        MNMNMN1=1
        if PL1=="a":
            HPII=HPII-10
        if PL1=="1":
            TO1=4
        if PL1=="2":
            if HPI>=130:
                HPI=150
            if HPI<130:
                HPI=HPI+20
        if PL1=="3":
            HPI=HPI-10
            CHOOSE=input("choose 1 or 2:1-敌方HP-30 or 2-三回合持续攻击10/round")
            if CHOOSE=="1":
                HPII=HPII-45
            if CHOOSE=="2":
                TOTO1=4
        if PL1=="4":
            PLAYER1="LUIS"
            print("You are Luis The King now!")
            print(" ")
            print("LUIS：HP=100 a=20 1_ 30  2_+20HP   3_ 持续三回合攻击15/round")
            print(" ")
            print("WRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!!!")
            print(" ")
            HPI=100
            NI=100
        TO1=TO1-1
        if TO1<=0:
            TO1=0
        if TO1==1 or TO1==2 or TO1==3:
            HPII=HPII-10
        TOTO1=TOTO1-1
        if TOTO1<=0:
            TOTO1=0
        if TOTO1==1 or TOTO1==2 or TOTO1==3:
            HPII=HPII-15
            
    if PLAYER1=="LUIS":
        LUISGOOD1=0
        if PL1=="a":
            HPII=HPII-20
        if PL1=="1":
            HPII=HPII-30
        if PL1=="2":
            if HPI>=80:
                HPI=100
            if HPI<80:
                HPI=HPI+20
        if PL1=="3":
            LUISGOOD1=4
        
        LUISGOOD1=LUISGOOD1-1
        if LUISGOOD1<=0:
            LUISGOOD1=0
        if LUISGOOD1==1 or LUISGOOD1==2 or LUISGOOD1==3:
            HPII=HPII-15
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    PL2=input("            NOW , PLAYER 2 CHOOSE WHAT TO DO.")
    if PLAYER2=="BRUCE":
        if PL2=="a":
            HPI=HPI-10
        if PL2=="1":
            BNM2=input("a or 2")
            if BNM2=="a":
                if HPII<=140:
                    HPII=HPII+10
                else:
                    HPII=150
                HPI=HPI-10
            if BNM2=="2":
                if HPII<=130:
                    HPII=HPII+20
                else:
                    HPII=150
                HPI=HPI-5
        if PL2=="2":
            if HPII<=130:
                HPII=HPII+20
            else:
                HPII=150
        if PL2=="3":
            if HPII<=100:
                HPII=HPII+50
            else:
                HPII=150
    if PLAYER2=="RICHARD":
        if PL2=="a":
            if HPII>30:
                HPI=HPI-15
            else:
                HPI=HPI-20
        if PL2=="1":
            if HPII<=140:
                HPII=HPII+10
            else:
                HPII=150
        if PL2=="2":
            if HPII>30:
                HPI=HPI-30
            else:
                HPI=HPI-40
        if PL2=="3":
            HPI=HPI/2
    if PLAYER2=="KATE":
        if PL2=="a":
            HPI=HPI-10
        if PL2=="1":
            if HPII<=220:
                HPII=HPII+30
            else:
                HPII=250
        if PL2=="2":
            HPII=100
        if PL2=="3":
            HPI=HPI-(250-HPII)/2
 
    if PLAYER2=="TONY":
        TO2=0
        TOTO2=0
        MNMNMN2=1
        if PL2=="a":
            HPI=HPI-10
        if PL2=="1":
            TO2=4
        if PL2=="2":
            if HPII>=130:
                HPII=150
            if HPII<130:
                HPII=HPII+20
        if PL2=="3":
            HPII=HPII-10
            CHOOSE=input("choose 1 or 2:1-敌方HP-30 or 2-三回合持续攻击10/round")
            if CHOOSE=="1":
                HPI=HPI-45
            if CHOOSE=="2":
                TOTO2=4
        if PL2=="4":
            PLAYER2="LUIS"
            print("You are Luis The King now!")
            print(" ")
            print("LUIS：HP=100 a=20 1_ 30  2_+20HP   3_ 持续三回合攻击15/round")
            print(" ")
            print("WRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!!!")
            print(" ")
            HPII=100
            NII=100
        TO2=TO2-1
        if TO2<=0:
            TO2=0
        if TO2==1 or TO2==2 or TO2==3:
            HPI=HPI-10
        TOTO2=TOTO2-1
        if TOTO2<=0:
            TOTO2=0
        if TOTO2==1 or TOTO2==2 or TOTO2==3:
            HPI=HPI-15
            
    if PLAYER2=="LUIS":
        LUISGOOD2=0
        if PL2=="a":
            HPI=HPI-20
        if PL2=="1":
            HPI=HPI-30
        if PL2=="2":
            if HPII>=80:
                HPII=100
            if HPII<80:
                HPII=HPII+20
        if PL2=="3":
            LUISGOOD2=4
        
        LUISGOOD2=LUISGOOD2-1
        if LUISGOOD2<=0:
            LUISGOOD2=0
        if LUISGOOD2==1 or LUISGOOD2==2 or LUISGOOD2==3:
            HPI=HPI-15
 
    print("PLAYER ONE HP:",HPI,"/",NI)
    print("PLAYER TWO HP:",HPII,"/",NII)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if HPI==0:
    print("PLAYER TWO IS THE WINNER !")
if HPII==0:
    print("PLAYER ONE IS THE WINNER !")
#============================================ENDING==================================
ENDINGCHOICE=input("You can end this program by pressing enter . Or you can enter 'ending' to see the ending .")
if ENDINGCHOICE=="ending" or ENDINGCHOICE=="ENDING":
    print("THIS GAME IS PRESENTED BY =BRICONIS= .")
    input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WE WILL KEEP UPDATING THIS GAME UNTIL IT IS COMPLETELY COMPLETED .")
    input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("FOR TEAM BRICONIS , WE HAVE BRUCE , RICHARD , TONY AND LUIS .")
    input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("AND WE ARE ALL EXPECTING YOU TO HAVE A GOOD LIFE .")
    input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                                                ___________                        ")
    print("                                                                || BRUCE ||                        ")
    print("                                                                ||RICHARD||                        ")
    print("                                                                || TONY  ||                        ")
    print("                                                                || LUIS  ||                        ")
    print("                                                                ||<<<|>>>||                        ")
    print("                                                                ||THANKS ||                        ")
    print("                                                                ||  FOR  ||                        ")
    print("                                                                ||PLAYING||                        ")
    print("                    ++++++++++++++++++++++++++++++++++++++++++++~~~~~~~~~~+++++++                  ")
    print("              =========================================================================            ")
    print("        =====================================================================================      ")
    print("  =================================================================================================")
    print("  |||                                                                                           |||")
    print("  |||     ____________________________________________________________________________          |||")
    print("  |||     {YOU DON'T HAVE TO LOOK AT THIS ENDING EVERY TIME AFTER YOU PLAY THIS GAME.}          |||")
    print("  |||     {THIS ENDING IS FOR THOSE PEOPLE WHO IS THE FIRST TIME PLAYING THIS GAME  .}          |||")
    print("  |||     {WE MADE THIS GAME FOR YOU GUYS TO RELAX AND TO HAVE A LITTLE COMPETITION .}          |||")
    print("  |||     {              AND WE WILL BE VERY GLAD IF YOU GUYS LIKE IT               .}          |||")
    print("  |||     {I HAVE A LOT OF THINGS TO SAY , BUT I'M AFRAID OF THIS HOUSE WOULD BE TOO }          |||")
    print("  |||     {                                    HIGH                                 .}          |||")
    print("  |||     {WELL , I SUDDENLY REALIZED THAT IT IS NON OF MY BUSINESS HOW HIGH THIS    }          |||")
    print("  |||     {                              HOUSE WILL BE                              .}          |||")
    print("  |||     {HOWEVER , DO YOU THINK THIS IS A GOOD EXPERIENCE of.......................}          |||")
    print("  |||     {..........................................................TALKING WITH ME?}          |||")
    print("  |||     {WISH YOU HAVE A GOOD TIME DURING ENJOYING YOUR LIFE                      !}          |||")
    print("  |||     {IF YOU THINK YOUR LIFE IS UNLUCKY.........................................}          |||")
    print("  |||     {                         WISH YOU WILL BE  LUCKY TOMORROW                .}          |||")
    print("  |||     {                                                 SEE YOU NEXT TIME!!!!!!!!}          |||")
    print("  |||     ----------------------------------------------------------------------------          |||")
    print("  |||                                                                                           |||")
    print("  |||                                                                                           |||")
    print("  |||                                                                                           |||")
    print("  |||                                                             ____________                  |||")
    print("  |||                                                             |          |                  |||")
    print("  |||                                                             |          |                  |||")
    print("  |||                                                             |          |                  |||")
    print("  |||                                                             |       @  |                  |||")
    print("  |||                                                             |          |                  |||")
    print("  |||                                                             |          |                  |||")
    print("  |||                                                             |          |                  |||")
    print("  #################################################################################################")
    print("  #################################################################################################")
    print("  #################################################################################################")
    print("\n")
    input("                                     press enter to open the door......                            ")
    input("                    AND...............................it is locked.  Press enter again please.     ")
    print("             THERE IS NOTHING IN HERE , DUDE ! WHY DID YOU BELIEVE IN RICHARD'S LIE!!!!!!!!!!!!!!!!")
    input("=============================================THANKS FOR PLAYING!=============================================")
    print("                                                                                 (and being an ideat.hahaha!)")
else:
    print("=============================================THANKS FOR PLAYING!=============================================")