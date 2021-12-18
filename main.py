# I read the handout
import csv
import operator
from typing import Coroutine, OrderedDict


def list_between(input_list, lower_cutoff, upper_cutoff):
    cut_off_list = []
    if len(input_list) == 0:
        print("Input list is empty")
    else:
        for num in input_list:
            if num > lower_cutoff and num < upper_cutoff:
                cut_off_list.append(num)

    return cut_off_list


def list_top_three(input_list):

    length = len(input_list)

    if length == 0:
        message = "None"
        return message

    elif length > 0 and length < 3:
        message = "Input list has less than three values."
        return message

    else:
        make_set = set(input_list)
        make_list = list(make_set)
        reverse_sorted_list = sorted(make_list, reverse=True)
        message = []

        for num in reverse_sorted_list:
            if len(message) < 3:
                message.append(num)
            else:
                break
        return message

def dict_between(input_dict, lower_cutoff, upper_cutoff):
    cut_off_dict = {}
    if len(input_dict) == 0:
        print("Input dictionary is empty")
    else:
        
        for key in input_dict:
            if input_dict[key] > lower_cutoff and input_dict[key] < upper_cutoff:
                cut_off_dict[key] = input_dict[key]

    return cut_off_dict

def dict_top_three(input_dict):

    if len(input_dict) == 0:
        message3 = "None"
        return message3
    else:
        from typing import OrderedDict
        top_three_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
        # Will contain MAX values to MIN values
        top_three_dict = OrderedDict(reversed(list(top_three_dict.items())))

        message3 = {}
        message3["Gold"] = []
        message3["Silver"] = []
        message3["Bronze"] = []

        make_set = set(input_dict.values())
        make_list = list(make_set)
        reverse_sorted_list = sorted(make_list, reverse=True)

        gold = -1
        silver = -1
        bronze = -1

        if len(reverse_sorted_list) > 0:
            gold = reverse_sorted_list[0]
        if len(reverse_sorted_list) > 1:
            silver = reverse_sorted_list[1]
        if len(reverse_sorted_list) > 2:
            bronze = reverse_sorted_list[2]
       
        lst = []
        if gold != -1:
            for key in input_dict:
                if input_dict[key] == gold:
                    lst.append(key)
            message3["Gold"] = lst

        lst = []
        if silver != -1:
            for key in input_dict:
                if input_dict[key] == silver:
                    lst.append(key)
            message3["Silver"] = lst

        lst = []
        if bronze != -1:
            for key in input_dict:
                if input_dict[key] == bronze:
                    lst.append(key)
            message3["Bronze"] = lst

        return message3

def csv_between(input_handle, output_handle, lower_cutoff, upper_cutoff):
    current_dict = {}
    cnt = 0
    with input_handle as file_open:
        for line in file_open:
            if cnt > 0:
                line = line.split(',')
                key = line[0]
                val = int(line[1])
                current_dict[key] = val
            cnt += 1
    
    with output_handle as file_write:
        file_write.write("Player Name,Points\n")
        for key in current_dict:
            if current_dict[key] > lower_cutoff and current_dict[key] < upper_cutoff:
                s = str(key) + "," + str(current_dict[key]) + str("\n")
                file_write.write(s)


def csv_top_three(input_handle, output_handle):

    current_dict = {}
    cnt = 0
    with input_handle as file_open:
        for line in file_open:
            if cnt > 0:
                line = line.split(',')
                key = line[0]
                val = int(line[1])
                current_dict[key] = val
            cnt += 1
    top_three_winners = dict_top_three(current_dict)
    # print("Ready to print", top_three_winners)

    with output_handle as file_write:
        lst = top_three_winners["Gold"]
        for name in lst:
            file_write.write(str(name) + " wins Gold\n")
        
        lst = top_three_winners["Silver"]
        for name in lst:
            file_write.write(str(name) + " wins Silver\n")

        lst = top_three_winners["Bronze"]
        for name in lst:
            file_write.write(str(name) + " wins Bronze\n")


def championship(input_handles):
    if len(input_handles) < 3:
        print("Please provide all 3 input handles for championship output")
        return

    team_player_handle = input_handles[0]  # team_player.csv', 'r'
    team_wins_handle = input_handles[1]  # 'team_wins.csv', 'r'
    player_points_handle = input_handles[2]  # 'player_score.csv', 'r'

    #1. Top three teams by wins
    current_dict = {}
    cnt = 0
    with team_wins_handle as file_open:
        for line in file_open:
            if cnt > 0:
                line = line.split(',')
                key = line[0]
                val = int(line[1])
                current_dict[key] = val
            cnt += 1
    current_dict = dict(
        sorted(current_dict.items(), key=operator.itemgetter(1), reverse=True))
    if len(current_dict) < 3:
        print("There are only ", str(len(current_dict)) , "teams in the given input")
        print("The top", str(len(current_dict)), "teams by win are:", current_dict) 
        for team in current_dict:
            print(team)
    else:
        print("The top three",  "teams by wins are:")
        for team in current_dict:
            print(team)

    #3. Top three players by points scored
    player_score_dict = {}
    cnt = 0
    with player_points_handle as file_open:
        for line in file_open:
            if cnt > 0:
                line = line.split(',')
                key = line[0]
                val = int(line[1])
                player_score_dict[key] = val
            cnt += 1
    player_score_dict = dict(
        sorted(player_score_dict.items(), key=operator.itemgetter(1), reverse=True))
    

    if len(player_score_dict) < 3:
        print("There are only ", str(len(player_score_dict)),
              "players in the given input")
        print("The top", str(len(player_score_dict)),
              "players by points are:", player_score_dict)
        for player in player_score_dict:
            print(player)
    else:
        print("The top three players by points are:")
        cnt = 0
        for player in player_score_dict:
            print(player)
            cnt += 1
            if cnt >= 3:
                break
    
    #2. Top three teams by points scored
    team_player_dict = {}
    cnt = 0
    with team_player_handle as file_open:
        for line in file_open:
            if cnt > 0:
                line = line.split(',')
                key = line[0]
                val = line[1][:-1]
                if key not in team_player_dict.keys():
                    team_player_dict[key] = []
                    team_player_dict[key].append(val)
                else:
                    team_player_dict[key].append(val)
            cnt += 1


    team_player_dict = dict(
        sorted(team_player_dict.items(), key=operator.itemgetter(1), reverse=True))

    team_total_points = {}
    for team in team_player_dict:
        team_point = 0
        lst_players = team_player_dict[team]
        for name in lst_players:
            team_point += player_score_dict[name]
        team_total_points[team] = team_point
    team_total_points = dict(
        sorted(team_total_points.items(), key=operator.itemgetter(1), reverse=True))
    
    if len(team_total_points) < 3:
        print("The top", len(team_total_points), "teams by points are listed below:")
        for team in team_total_points:
            print(team, "->", team_total_points[team])
    else:
        print("The top three teams by points are listed below:")
        my_set = set()
        for team in team_total_points:
            my_set.add(team_total_points[team])
            if len(my_set) > 3:
                break
            print(team, team_total_points[team])
    
    #4. Top scoring player on each team
    for team in team_player_dict:
        print("The top players of", team, "are listed below:")
        lst_players = team_player_dict[team]
        top_scorer = {}
        for player in lst_players:
            top_scorer[player] = player_score_dict[player]
        top_scorer = dict(
            sorted(top_scorer.items(), key=operator.itemgetter(1), reverse=True))
        
        #------------------Print the top player of each team-------------------------------
        my_set = set()
        for player in top_scorer:
            my_set.add(top_scorer[player])
            if len(my_set) > 1:
                break 
            print(player, top_scorer[player])


my_list = [7, 7, 8]
cutoff_list = list_between(my_list, 5, 9)
top_three_list = list_top_three(my_list)

#Output of "cutoff_list" function
print("My input list is: " + str(my_list))
if len(cutoff_list) == 0:
    print("None")
else:
    print("My list with only values between 5 and 9 is: " + str(cutoff_list))  # <-- this should print [8, 6, 7]

#Output of "top_three_list" function
print("The top three elements are: " + str(top_three_list)) #<---- this should print[9, 8, 7]

my_dict = {'Alice': 7, 'Bob': 7, 'Carol': 7, 'Dave': 7, 'Edith': 7, 'Frank': 7, 'Gertrude': 7, 'Helen': 7}
cutoff_dict = dict_between(my_dict, 5, 9)
top_three_dict = dict_top_three(my_dict)

#Output of "dict_between" function
print("My starting dictionary is: " + str(my_dict))
print("My dictionary with only values above 5 is: " + str(cutoff_dict)) # <-- Dave, Edith and Helen should be in this dictionary

#Output of "top_three_dict" function
print("My dictionary winners are: " + str(top_three_dict)) #<-- should be something like: {'Gold': 'Gertrude', 'Silver': 'Dave', 'Bronze:' 'Alice'}


input_file = open('player_score.csv', 'r')
output_file = open('csv_top5.csv', 'w')
csv_between(input_file, output_file, 5, 9)
# <-- this should be the same format as the input file
# print("My csv file with only scores above 5 can be found at csv_top5.csv")
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

team_player_handle = open('team_player.csv', 'r')
team_wins_handle = open('team_wins.csv', 'r')
player_points_handle = open('player_score.csv', 'r')
input_files = [team_player_handle, team_wins_handle, player_points_handle]
print("Now let's award trophies!")
championship(input_files)  # <-- this should print lots of cool information


team_player_handle.close()
team_wins_handle.close()
player_points_handle.close()
