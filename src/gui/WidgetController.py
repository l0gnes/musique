from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .classes.frames.MusicControl import MusicControl
    from .classes.frames.MusicProgress import MusicProgress
    from .classes.frames.MusicSelection import MusicSelection
    from .classes.frames.SongView import SongView
    from .ApplicationConfig import ApplicationConfig

from .PlaylistHandler import PlaylistHandler
from ttkbootstrap import Window

class WidgetController(object):

    music_control : "MusicControl"
    music_progress : "MusicProgress"
    music_selection : "MusicSelection"
    song_view : "SongView"

    application_config : "ApplicationConfig"
    playlist_handler : "PlaylistHandler"

    root : Window

    is_music_paused : bool = False

    def __init__(
        self,
        root : Window,
        application_config : "ApplicationConfig"
    ) -> None:
        
        self.root = root
        self.application_config = application_config
        self.playlist_handler = PlaylistHandler( self.application_config.get_playlists_directory() )

    def pause_music(self):
        self.is_music_paused = not self.is_music_paused
        self.music_progress.set_paused_state(self.is_music_paused)
