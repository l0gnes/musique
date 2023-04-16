from os import PathLike
import os.path
import eyed3

class Song(object):

    name : str
    artist : str
    album : str

    song_path : PathLike

    def __init__(
        self,
        name : str | None,
        path : PathLike,
        *,
        artist : str = None,
        album : str = None
    ) -> None:

        self.song_path = path

        self.name = name if name else self.get_default_title_name()

        self.artist = artist
        self.album = album

    @classmethod
    async def from_file(cls, file_path : PathLike, 
                        *, existence_check : bool = True) -> "Song":
        
        if existence_check and not os.path.exists(file_path):
            raise FileNotFoundError("No file with that path exists. Could not create song object!")
        
        eyed3_obj = eyed3.load(file_path)

        return cls(
            eyed3_obj.tag.title,
            file_path,
            artist = eyed3_obj.tag.artist,
            album = eyed3_obj.tag.album
        )

    @property
    def slug(self) -> str:
        return self.name.lower().replace('_', ' ')
    
    def get_default_title_name(self) -> str:
        return os.path.basename(os.path.splitext(self.song_path)[0])

    def is_file_mp3(self) -> bool:
        return os.path.splitext(self.song_path)[1] == '.mp3'