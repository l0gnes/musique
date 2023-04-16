from os import PathLike
import os.path
from typing import List, TYPE_CHECKING
from .Song import Song
import json

if TYPE_CHECKING:
    from ..PlaylistHandler import PlaylistHandler

class Playlist(object):

    name : str
    playlist_file : PathLike

    songs : List[Song]

    def __init__(
        self, 
        name : str,
        directory : PathLike) -> None:

        self.name = name
        self.directory = directory
        self.songs = []

    @property
    def slug(self) -> str:
        return self.name.lower().replace(' ', '_')
    

    @classmethod
    def load_from_file(
        cls, file_path : PathLike
    ) -> "Playlist":
        
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        cls(
            data['playlist_info']['name'],
            file_path
        ).fill_songs_from_json(
            data['songs']
        )

    def dump_to_file(
        self        
    ) -> None:
        
        data_to_dump = {
            "playlist_info" : { "name" : self.name },
            "songs" : [s.song_path for s in self.songs]
        }

        with open(self.file_path, 'w+') as json_file:
            json.dump(data_to_dump, json_file)
    
    def fill_songs_from_json(self, songs : List[str]) -> None:

        for s in songs:

            if os.path.exists(s):

                self.songs.append(
                    Song.from_file(s, existence_check = False)
                )

    @classmethod
    def create_new_playlist(cls, playlist_handler : "PlaylistHandler", name : str) -> "Playlist":
        
        new_playlist = cls(
            name = name,
            directory = os.path.join(playlist_handler.playlist_dir, "%s.json" % (name))
        )

        return new_playlist