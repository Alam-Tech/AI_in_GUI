from app import AppType,App
from ucb_agent import Agent

#Initialising the app_tray dictionary with empty list for all categories:
app_dict = {}

app_dict[AppType.INTERNET_BROWSER] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(1)
}
app_dict[AppType.ANTIVIRUS] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(1)
}
app_dict[AppType.FOLDER] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(3)
}
app_dict[AppType.MEDIA_VIDEO] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(1)
}
app_dict[AppType.MEDIA_AUDIO_ONLY] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(1)
}
app_dict[AppType.GAMES] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(2)
}
app_dict[AppType.DOCUMENT] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(3)
}
app_dict[AppType.UTILITY] = {
   'full_list':[],
   'display_list':[],
    'agent':Agent(5)
}

#Initialising the app list:
app_list = [
    App('Microsoft Edge',34,AppType.INTERNET_BROWSER),
    App('Firefox',34,AppType.INTERNET_BROWSER),
    App('Google Chrome',34,AppType.INTERNET_BROWSER),
    App('Opera mini',34,AppType.INTERNET_BROWSER),
    App('Windows Firewall',34,AppType.ANTIVIRUS),
    App('Avast Antivirus',34,AppType.ANTIVIRUS),
    App('Call of Duty',34,AppType.GAMES),
    App('Raw vs Smackdown',34,AppType.GAMES),
    App('Need for Speed',34,AppType.GAMES),
    App('Uncharted',34,AppType.GAMES),
    App('MX Player',34,AppType.MEDIA_VIDEO),
    App('VLC',34,AppType.MEDIA_VIDEO),
    App('Windows Media Player',34,AppType.MEDIA_VIDEO),
    App('Flash Player',34,AppType.MEDIA_VIDEO),
]

for app in app_list:
    app_dict[app.app_type]['full_list'].append(app.app_name)
    app_dict[app.app_type]['display_list'].append(app.app_name)
    app_dict[app.app_type]['agent'].add_app()

def get_target_list(target_key,app_name,action):
    """
    This function is to get the display list of apps that are to be displayed on the
    desktop based on the output of the UCB agents of different app categories.
    Codes of different actions:
    0 -->  app is selected.
    1 -->  app is deleted.
    2 -->  app is added.
    """
    result = []
    global app_dict
    
    for key in app_dict.keys():
        if key == target_key:
            if action == 2:
                app_dict[key]['full_list'].append(app_name)
                app_dict[key]['agent'].add_app()
            else:
                index = app_dict[key]['full_list'].index(app_name)
                if action == 1:
                    app_dict[key]['agent'].delete_app(index)
                elif action == 0:
                    app_dict[key]['agent'].update(index)
            target_list = app_dict[key]['agent'].get_priority_list()
            app_dict[key]['display_list'] = [app_dict[key]['full_list'][i] for i in target_list]
        result += app_dict[key]['display_list']
    
    return result    
        
choice = 'yes'
app_choice = 'No app'
app_dict_key = -1
app_action = -1

while choice.lower() == 'yes':
    target_list = get_target_list(app_dict_key,app_choice,app_action)
    print("Select an app: ")
    for app in target_list:
        print(app)
    
    app_choice = input('Enter the app\'s name(Enter "add" or "delete" to perform corresponding actions): ')
    
    lower_app_choice = app_choice.lower()
    if lower_app_choice == 'add':
        app_action = 2
        app_choice = input("Enter the name of the App/Folder to be added: ")
    elif lower_app_choice == 'delete':
        app_action = 1
        app_choice = input("Enter the name of the App/Folder to be deleted: ")
    else:
        app_action = 0
        for app in app_list:
            if app.app_name == app_choice:
                app_dict_key = app.app_type
                break
        else:
            print("App not found!")
            app_dict_key = -1
    
    choice = input('Do you wanna continue? ')

print('Thank you!')