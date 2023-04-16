from .data.Playlist import Playlist
from typing import List
from os import PathLike
import os.path
from glob import glob
from json import load

class PlaylistHandler(object):

    playlist_dir : PathLike
    playlists : List[Playlist]

    def __init__(
            self,
            playlist_dir : PathLike) -> None:
        
        self.playlist_dir = playlist_dir

        self.playlists = []
        self.load_playlists_from_directory()

    def load_playlists_from_directory(self) -> None:
        
        # Returns a list of all of the playlist files
        playlist_files = glob(
            os.path.join(self.playlist_dir, '/*.json')
        )

        print("Found %d playlist(s)" % (len(playlist_files)))

        for pl in playlist_files:

            self.playlists.append(
                Playlist.load_from_file(pl)
            )
            
    def get_playlists(self) -> List[Playlist]:
        return self.playlists