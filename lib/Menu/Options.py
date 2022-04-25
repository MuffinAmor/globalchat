class Options:
    room_named = "Name des Chatraums"
    channel_name = "Textchannel der ab/angebunden werden soll."
    member = "Eine Person aus diesem Server"

    def __init__(self, room_name, channel_name, member):
        self.room_name = room_name
        self.channel_name = channel_name
        self.member = member


class HelpMenuContent:
    normal_desc = "Allgemeine Commands"
    setup_desc = "Commands zur Erstellung und Ersteinrichtung."
    admin_desc = "Optionen zur Administration von Chaträumen"
    mod_desc = "Möglichkeiten zur Verwaltung und Moderation"
    anime_desc = "Anime Gifs"

    def __init__(self, normal_desc, setup_desc, admin_desc, mod_desc, anime_desc):
        self.normal_desc = normal_desc
        self.setup_desc = setup_desc
        self.admin_desc = admin_desc
        self.mod_desc = mod_desc
        self.anime_desc = anime_desc
