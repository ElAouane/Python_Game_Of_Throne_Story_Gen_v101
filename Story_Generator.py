import time
#####################################################################
#DEFINE ALL DICTIONARIES AND VARIABLE AS GENERAL APPLICATION SETTING
#####################################################################

#########################
#DEFINE ALL DICTIONARIES
#########################
#TODO change date format
month_dict = {'01' : 'I drank with',
              '02' : 'I illed',
              '03' : 'I married',
              '04' : 'I kissed',
              '05' : 'I poisoned',
              '06': 'I slapped',
              '07' : 'I ate with',
              '08' : 'I stabbed',
              '09' : 'I ******',
              '10' : 'I burned',
              '11' : 'I beheaded',
              '12' : 'I fight with'
              }
day_dict = {'01' : 'Jorah Mormont',
            '02' : 'The Hound',
            '03' : 'Sansa Stark',
            '04' : 'The Night King',
            '05' : 'Podrick',
            '06' : 'Daenerys',
            '07' : 'Samwel Tarly',
            '08' : 'Bran Stark',
            '09' : 'Lyanna Mormont',
            '10' : 'Ser Devos',
            '11' : 'Cersei Lannister',
            '12' : 'Missandei',
            '13' : 'Brienne of Tarth',
            '14' : 'Joffrey',
            '15' : 'Theon Greyjoy',
            '16' : 'Ramsey Bolton',
            '17' : 'Arya Stark',
            '18' : 'Tormund',
            '19' : 'Jon Snow',
            '20' : 'Lysa Arryn',
            '21' : 'Tyron Lannister',
            '22' : 'Ned Stark',
            '23' : 'Gendry',
            '24' : 'Grey Worm',
            '25' : 'Melisandre',
            '26' : 'Varys',
            '27' : 'Gilly',
            '28' : 'Jaime Lannister',
            '29' : 'Peter Baelish',
            '30' : 'Robb Stark',
            '31' : 'Robin Arryn'
            }
name_first_letter = {'A' : 'and I\'m proud of it',
                     'B' : 'While riding a horse',
                     'C' : 'In front of the crowd',
                     'D' : 'And it was f***** crazy',
                     'E' : 'For good luck',
                     'F' : 'While yelling so loudly',
                     'G' : 'Because my mother told me so',
                     'H' : 'In my dream',
                     'I' : 'On my bed',
                     'J' : 'While singing my favorite song',
                     'K' : 'And I want to do it again',
                     'L' : 'Outside the wall',
                     'M' : 'Inside the box',
                     'N' : 'Because i loved it',
                     'O' : 'In the Crypt',
                     'P' : 'and I expect it will happen',
                     'Q' : 'In the Red Keep',
                     'R' : 'While my eyes were closed',
                     'S' : 'Because I Wanted it so badly',
                     'T' : 'In a tent',
                     'U' : 'Because it\'s my hobby',
                     'V' : 'In the kitchen',
                     'W' : 'Because I\'ve been waiting this for a long time',
                     'X' : 'On a boat',
                     'Y' : 'And it was amazing',
                     'Z' : 'While taking a bath'
                     }

#############################
#DEFINE USER GEN INFO AS DICT
#############################
general_info = {'Name' : '',
                'Surname' : '',
                'DOB' : ''}

date_of_birth = {'Day' : '',
                 'Month' : '',
                 'Year' : ''
                 }

story_dict = {'hero': '',
              'beginning': '',
              'middle': '',
              'end': ''}
###################################
#Gather General info about the user
###################################
general_info['Name'] = input("Hello, may i have your name please?: ")
general_info['Surname'] = input(f"Oh, as we have another persone named {general_info['Name']}, may i have your Surname please?")
#Feed the general info['name']['surname'] to story_dict[hero]
story_dict['hero'] = general_info['Name'] + ' ' +general_info['Surname']
print(f"Perfect, thank very much {general_info['Name']} {general_info['Surname']}")
#print(general_info['Name'][0])
#############################
#Store user date of birth
#############################
general_info['DOB'] = input('One last thing, can I have you date of birth please?')

########################################
#Split date of birth from general_info
#And feed every index to date_of_birth dict
###########################################
date_split = general_info['DOB'].split('/')
date_of_birth['Day'] = date_split[0]
date_of_birth['Month'] = date_split[1]
date_of_birth['Year'] = date_split[2]
#print(date_of_birth)


#########################
#CORE APPLICATION CODE
#########################
print("Here is our story. It\'s and we get tired and bored.\n So we will make a story based on you general info")
print("Thinking......")
time.sleep(5)
for key, value in month_dict.items():
    if date_of_birth['Month'] == key:
        story_dict['beginning'] = value
for key, value in day_dict.items():
    if date_of_birth['Day'] == key:
        story_dict['middle'] = value
for key, value in name_first_letter.items():
    if general_info['Name'][0] == key:
        story_dict['end'] = value

print(f"Your story is:\n  {story_dict['beginning']} {story_dict['middle']} {story_dict['end']}")
print(story_dict)