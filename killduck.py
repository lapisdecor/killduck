__module_name__ = "killduck"
__module_version__ = "1.0"
__module_description__ = "Kill a duck instantly"

import hexchat

def duck_talks(word, word_eol, userdata):
    if word[0] == "chat":
        if word[1] == "\\_o< quack!":
            hexchat.command("say +bang")
    return None

hexchat.hook_print("Channel Message", duck_talks)
