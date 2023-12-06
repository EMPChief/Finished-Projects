name = ['Frida', 'Hilda', 'Mathilda', 'Robin']
age = [18, 27, 24, 22]
password = ('AliceWonderland12', 'HildaTheKiller', 'ShutThatFace', 'KidYouNot')
words = ['Frida the Master', 'Hilda the assassin',
         'Mathilda the Succubus', 'Robin the clown']

puttogheter = dict(zip(name, zip(age, password, words)))

for key, value in puttogheter.items():
    print(key + " : " + str(value))

for i in puttogheter.items():
    print(i)
