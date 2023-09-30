from EllieXMusic.core.bot import ALPHA
from EllieXMusic.core.dir import dirr
from EllieXMusic.core.git import git
from EllieXMusic.core.userbot import Userbot
from EllieXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ALPHA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
