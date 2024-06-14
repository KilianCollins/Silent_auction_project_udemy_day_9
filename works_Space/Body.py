#
#
# # make a empty dic
#
# end_loop = False
# master_dictionary = {}
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
#         print(f"the highest bid goes to {corrosponding_key}")
#
#         end_loop = True
#
#
