# ------------------------
# Import Libraries
# ------------------------
import sys
import clr
import os
import codecs
import json
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

# ------------------------
# [Required] Script Information
# ------------------------
ScriptName = "LFG"
Website = "https://github.com/bap14/Streamlabs_LFG"
Description = "Adds !lfg command which populates an overlay for use on stream"
Creator = "BleepBlamBleep"
Version = "0.0.1"

# ------------------------
# Set Variables
# ------------------------
fileEncoding = 'utf-8-sig'
settingsFile = os.path.join(os.path.dirname(__file__), "settings", "settings.json")

class Settings:
    def __init__(self, settings_file=None):
        global fileEncoding, settingsFile
        self.config = self.getDefaultSettings()

        settings_dir = os.path.dirname(settingsFile)
        if settings_file is not None:
            settings_dir = os.path.dirname(settings_file)

        if not os.path.isdir(settings_dir):
            os.makedirs(settings_dir)

        if settings_file is not None and not os.path.isfile(settings_file):
            path_tuple = os.path.split(settings_file)
            settingsFilePath = path_tuple[0].split(os.sep)
            settingsFilePath.pop()
            old_settings_file = os.path.join(os.sep.join(settingsFilePath), path_tuple[1])
            if os.path.isfile(old_settings_file):
                os.rename(old_settings_file, settings_file)
            if os.path.isfile(old_settings_file.replace('json', 'js')):
                os.rename(old_settings_file.replace('json', 'js'), settings_file.replace('json', 'js'))

        if os.path.isfile(settings_file):
            with codecs.open(settings_file, encoding=fileEncoding, mode='r') as f:
                self.config.update(json.load(f, encoding=fileEncoding))
        return

    def __getattr__(self, item):
        retval = None
        if item in self.config:
            retval = self.config[item]
        return retval

    def ReloadSettings(self, data):
        global fileEncoding
        self.config = self.getDefaultSettings()
        self.config.update(json.loads(data, encoding=fileEncoding))
        Parent.BroadcastWsEvent("LFG_UPDATE_SETTINGS", json.dumps(self.config))
        return

    def SaveSettings(self, settings_file):
        global fileEncoding
        with codecs.open(settings_file, encoding=fileEncoding, mode='w+') as f:
            json.dump(self.config, f, encoding=fileEncoding, indent=4, sort_keys=True)
        with codecs.open(settings_file.replace('json', 'js'), encoding=fileEncoding, mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.config, encoding=fileEncoding, indent=4,
                                                            sort_keys=True)))
        return

    # ------------------------
    # Get a copy of the default settings JSON structure
    # ------------------------
    def getDefaultSettings(self):
        return {
            "Command": "!lfg",
            "Permission": "Everyone",
            "PermissionInfo": "",
            "ListAllCommand": "list",
            "ListAllCommandPermission": "Moderator",
            "ListAllCommandPermissionInfo": "",
            "HelpCommand": "help",

            "Message_LFG_Usage": "To add your group to our LFG list, type this in chat: {1} <console> <activity>",

            "Manage_ClearKeyword": "clear",
            "Manage_ClearPermission": "Moderator",
            "Manage_ClearPermissionInfo": ""
        }.copy()

# ------------------------
# [Required] Initialize Data (Only called on Load)
# ------------------------
def Init():
    global RaffleSettings, isRaffleActive, settingsFile
    isRaffleActive = False
    RaffleSettings = Settings(settingsFile)
    return

def ReloadSettings(jsonData):
    global RaffleSettings, settingsFile
    RaffleSettings.ReloadSettings(jsonData)
    return

# ------------------------
# [Required] Execute Data / Process Messages
# ------------------------
def Execute(data):
    if data.IsChatMesage():
        # TODO: Implement stuff!
    return
