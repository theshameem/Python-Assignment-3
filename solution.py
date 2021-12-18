# I read the handout
def list_between(input_list, lower_cutoff, upper_cutoff):
    """
    """
    ansList = []
    for num in input_list:
        if num > lower_cutoff and num < upper_cutoff:
            ansList.append(num)
    
    print(ansList)
    return ansList



def list_top_three(input_list):
    """
    """


def dict_between(input_dict, lower_cutoff, upper_cutoff):
    """
    """


def dict_top_three(input_dict):
    """
    """


def csv_between(input_handle, output_handle, lower_cutoff, upper_cutoff):
    """
    """


def csv_top_three(input_handle, output_handle):
    """
    """


def championship(input_handles):
    """
    """


###MAIN CODE STARTS HERE###
"""
This code is designed to test the very basic functionality of your code, it does not fully test your code.
You will want to add additional testing yourself 
"""

my_list = [1, 4, 5, 3,  8,6, 2, 9, 7]
cutoff_list = list_between(my_list, 5, 9)
# top_three_list = list_top_three(my_list)

print("My input list is: " + str(my_list))
print("My list with only values between 5 and 9 is: " + str(cutoff_list))  # <-- this should print [8, 6, 7]
# <-- this should print [9, 8, 7]
print("The top three elements are: " + str(top_three_list))


#-------------------------------------------------------------------------------------------------------------------#
my_dict = {'Alice': 1, 'Bob': 4, 'Carol': 5, 'Dave': 8, 'Edith': 6, 'Frank': 2, 'Gertrude': 9, 'Helen': 7}
cutoff_dict = dict_between(my_dict, 5, 9)
top_three_dict = dict_top_three(my_dict)

print("My starting dictionary is: " + str(my_dict))
# <-- Dave, Edith and Helen should be in this dictionary
print("My dictionary with only values above 5 is: " + str(cutoff_dict))
# <-- should be something like: {'Gold':'Gertrude', 'Silver':'Dave', 'Bronze'}
print("My dictionary winners are: " + str(top_three_dict))

input_file = open('player_score.csv', 'r')
output_file = open('csv_top5.csv', 'w')
csv_between(input_file, output_file, 5, 9)
# <-- this should be the same format as the input file
print("My csv file with only scores above 5 can be found at csv_top5.csv")
#but with only Dave, Edith and Helen's data
output_file.close()
input_file.close()

input_file = open('player_score.csv', 'r')
output_file = open('csv_results.txt', 'w')
csv_top_three(input_file, output_file)
# <-- this file should have 3 lines with the text
print("My csv file winners can be foudn at csv_results.txt")
#Gertrude wins Gold
#Dave wins Silver
#Helen wins Bronze
input_file.close()
output_file.close()


# team_player_handle = open('team_player.csv', 'r')
# team_wins_handle = open('team_wins.csv', 'r')
# player_points_handle = open('player_score.csv', 'r')
# input_files = [team_player_handle, team_wins_handle, player_points_handle]
# print("Now let's award trophies!")
# championship(input_files)  # <-- this should print lots of cool information


# team_player_handle.close()
# team_wins_handle.close()
# player_points_handle.close()
#-------------------------------------------------------------------------------------------------------------------#

#########################Output#############################################################
# My input list is: [1, 4, 5, 3, 8, 6, 2, 9, 7]
# My list with only values between 5 and 9 is: None
# The top three elements are: None
# My starting dictionary is: {'Alice': 1, 'Bob': 4, 'Carol': 5, 'Dave': 8, 'Edith': 6, 'Frank': 2, 'Gertrude': 9, 'Helen': 7}
# My dictionary with only values above 5 is: None
# My dictionary winners are: None
# My csv file with only scores above 5 can be found at csv_top5.csv
# My csv file winners can be foudn at csv_results.txt
# Now let's award trophies!
