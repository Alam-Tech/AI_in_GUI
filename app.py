class AppType:
    """
    This class is used as an enum class to uniquely identify different categories of apps
    """
    INTERNET_BROWSER = 0
    ANTIVIRUS = 1
    FOLDER = 2
    MEDIA_VIDEO = 3
    MEDIA_AUDIO_ONLY = 4
    GAMES = 5
    DOCUMENT = 6
    UTILITY = 7
    
class App():
    """
    This class is used to respresent the basic details of an app
    present in the app list of the computer
    """
    def __init__(self,name,size,app_type):
        self.app_name = name
        self.app_size = size
        self.app_type = app_type