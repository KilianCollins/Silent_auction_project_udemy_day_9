from Art import logo


bids = {}
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
bidding_fineshed = False

def max_bid_finer(biding_record):
    highest_bid = 0
    winner =" "
    for bidder in biding_record:
        bid_amaount = biding_record[bidder]
        if bid_amaount > highest_bid:
            highest_bid = bid_amaount
            winner = bidder
    print(f"the winner is {winner} with the amount of {highest_bid}")




while not bidding_fineshed:
    print(logo)
    print("Hello welcome to the silent blind auction")
    name = input("name: ")
    price =int(input("bid: "))
    bids[name] = price
    should_continue = input("are there any other bidders: y/n")
    if should_continue == "n":
        max_bid_finer(biding_record=bids)
        bidding_fineshed = True


    elif should_continue =="y":
        print(CLEAR)
        print(CLEAR_AND_RETURN)



























# make a empty dic
# CLEAR_TERMINAL = "\033[H\033[2J"
#
# end_loop = False
# master_dictionary = {}
#
# acution_in_progress = True
# print(CLEAR_TERMINAL)
# welcome_sequence = "Hello welcome to the silent blind auction"
# # name = input("name: ")
# # bid = input("bid: ")
# winner = ""
# max_bid = 0
# def silent_Auction(name_input,bid_input):
#     master_dictionary[name_input] = bid_input
#     max_bid = max(master_dictionary.values())
#
#     for person in master_dictionary:
#         if master_dictionary[person] == max_bid:
#             winner = master_dictionary[person]
#
# while acution_in_progress: #true
#     print(CLEAR_TERMINAL)
#     new_memeber = input("is there a bidder? : (y/n): ").lower().strip(" ")
#     if new_memeber == "n":
#         print(f"the winner is {winner} whose bid is {max_bid}")
#         acution_in_progress = False
#     if new_memeber =="y":
#         new_memeber = input("is there a bidder? : (y/n): ").lower().strip(" ")
#         name = input("name: ")
#         bid = int(input("bid: "))
#         silent_Auction(name_input=name,bid_input=bid)
#         print(CLEAR_TERMINAL)
#
#






















#
#
# print(master_dictionary)
#
# while end_loop == False:
#     should_continue = input("are there any bidders?: (yes/no): \n").lower().strip()
#     if should_continue == "yes":
#         dict_entry_key = input("whats your name:\n")
#         # will equal key
#         dict_entry_value = int(input(f"Hello {dict_entry_key} enter your bid below: \n"))
#         # dict value
#         master_dictionary[dict_entry_key] = dict_entry_value
#     elif should_continue == "no":
#         max_val = max(master_dictionary.values())
#         # print(master_dictionary, max_val)
#         # print(f"the highest bid goes to {corrosponding_key}")
#
#         end_loop = True
#
#
