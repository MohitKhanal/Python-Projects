# to make KBC game using only match case statement
cash=0
print("Let's play the game")
print("Who is the father of computer?")
print("a.Anne Marie\t b.Radhe Shyam\t  \nc.Hari Banjade\t  d.Charles Babbage")
life=input("Do you want to use lifeline?(Y/N)")
match life:
    case "Y":
        print("Which life life would you like to use?")
        print("a.50-50\t b.Double Dip\t")
        life1_op=input("Choose your lifeline option")
        match life1_op:
            case "a":
                print("Who is the father of computer?")
                print("\t\tb.Radhe Shyam\n\t\td.Charles Babbage")
                life1_ans=input("Enter the answer:\n")
                match life1_ans:
                    case "d":
                        cash+=1000
                        print("Right answer!.You win ${}".format(cash))
                        print("Its right answer.\nLet\'s move to next question")
                        print("What is the capital city of Portugal?")
                        print("Your Options are:\na.Moscow\t b.Lisbon\t c.Berlin\t d.Havanna")
                        life=input("Do you want to use lifeline?(Y/N)")
                        match life:
                            case "Y":
                               print("Which life line would you like to use?")
                               print("\t\t b.Double Dip")
                               life2_op=input("Choose your lifeline option")
                               match life2_op:
                                    case "b":
                                       print("Now you have two chances to select your answer.If one goes wrong you have to select another and if both goes wrong you lose!")
                                       print("What is the capital of Portugal?")
                                       print("Your Options are:\na.Moscow\t b.Lisbon\t c.Berlin\t d.Havanna")
                                       life2_ans=input("Enter your answer:")
                                       match life1_ans:
                                            case "b":
                                                cash+=10000
                                                print("Congratulations!!,You have won ${}".format(cash))
                                            case _:
                                               print("That's wrong answer.You have one more chance to prove yourself")
                                               life2_ans=input("What do you choose now?")
                                               match life2_ans:
                                                    case "b":
                                                        cash+=10000
                                                        print("That's right answer.You have won ${}".format(cash))
                                                    case _:
                                                       print("You are wrong again.So you go away with ${}".format(cash))
                            case _:
                                print("Fine!")        
                                ans=input("Enter the answer:\n")
                                match ans:
                                    case "d":
                                        cash+=10000
                                        print("Its right answer.You win ${}".format(cash))
                                    case _:
                                        print("Its wrong answer.You win a total of ${}".format(cash))

                    case _:
                        print("it's wrong answer you go away with ${}".format(cash))
            case "b":
                print("Now you have two chances to select your answer.If one goes wrong you have to select another and if both goes wrong you lose!")
                print("Who is the father of computer?")
                print("a.Anne Marie\t b.Radhe Shyam\t  \nc.Hari Banjade\t  d.Charles Babbage")
                life2_ans=input("Enter the answer:\n")
                match life2_ans:
                    case "d":
                        cash+=1000
                        print("Right answer!.You win {}".format(cash))
                        print("What is the capital city of Portugal?")
                        print("Your Options are:\na.Moscow\t b.Lisbon\t c.Berlin\t d.Havanna")
                        life=input("Do you want to use lifeline?(Y/N)")
                        match life:
                            case "Y":
                               print("You have only one lifeline left that is 50-50!Would you like to take it(Y/N)?")
                               conf=input("Type 'Y' if you want to use it")
                               match conf:
                                   case Y:
                                        print("What is the capital city of Portugal?")
                                        print("a.Moscow\t b.Lisbon")
                                        life1_ans=input("Enter your answer")
                                        match life1_ans:
                                            case "b":
                                                cash+=10000
                                                print("That's a right answer.You have won${}".format(cash))
                                            case _:
                                                print("Wrong answer!!.You go away with ${}".format(cash))
                    case _:
                        print("You are wrong and you have one more chance to prove youself")
                        life2_ans=input("Enter your next answer:\n")
                        match life2_ans:
                            case "d":
                                cash+=1000
                                print(f"Right answer!.You win ${cash}")
                                print("What is the capital city of Portugal?")
                                print("Your Options are:\na.Moscow\t b.Lisbon\t c.Berlin\t d.Havanna")
                                life=input("Do you want to use lifeline?(Y/N)")
                                match life:
                                    case "Y":
                                       print("You have only one lifeline left that is 50-50!Would you like to take it(Y/N)?")
                                       conf=input("Type 'Y' if you want to use it")
                                       match conf:
                                           case Y:
                                                print("What is the capital city of Portugal?")
                                                print("a.Moscow\t b.Lisbon")
                                                life1_ans=input("Enter your answer")
                                                match life1_ans:
                                                    case "b":
                                                        cash+=10000
                                                        print("That's a right answer.You have won${}".format(cash))
                                                    case _:
                                                        print("Wrong answer!!.You go away with ${}".format(cash))
                            case _:
                                print("it's wrong answer you go away with $0")
    case _:
        print("Ok,then you chosed not to use life line")        
        ans=input("Enter the answer:\n")
        match ans:
            case "d":
                cash+=1000
                print("Its right answer.You won ${}".format(cash))
                print("What is the capital city of Portugal?")
                print("Your Options are:\na.Moscow\t b.Lisbon\t c.Berlin\t d.Havanna")
                life=input("Do you want to use lifeline?(Y/N)")
                match life:
                   case "Y":
                       print("Which life life would you like to use?")
                       print("a.50-50\t b.Double Dip\t")
                       life2_op=input("Choose your lifeline option")
                       match life2_op:
                            case "a":
                               print("What is the capital city of Portugal?")
                               print("\t\tb.Lisbon\nc.Berlin")
                               life2_ans=input("Enter the answer:\n")
                               match life2_ans:
                                    case "b":
                                         cash+=10000
                                         print("Congratulations!!You have won${}".format(cash))
                                    case _:
                                       print("That's a wrong answer.You have won ${}".format(cash))
                            case "b":
                               print("Now you have two chances to select your answer.If one goes wrong you have to select another and if both goes wrong you lose!")
                               print("What is the capital of Portugal?")
                               print("Your Options are:\na.Moscow\t b.Lisbon\t c.Berlin\t d.Havanna")
                               life2_ans=input("Enter your answer:")
                               match life2_ans:
                                    case "b":
                                        cash+=10000
                                        print("Congratulations!!,You have won ${}".format(cash))
                                    case _:
                                       print("That's wrong answer.You have one more chance to prove yourself")
                                       life2_ans=input("What do you choose now?")
                                       match life2_ans:
                                            case "b":
                                                cash+=10000
                                                print("That's right answer.You have won ${}".format(cash))
                                            case _:
                                               print("You are wrong again.So you go away with ${}".format(cash))
            case _:
                print("That's wrong.Sorry you have won only ${}".format(cash))
                      
