from ttkbootstrap import Treeview
from typing import List

from PIL import ImageTk, Image

class PlaylistTreeConsumer(object):

    @staticmethod
    def buildTree(tree : Treeview, playlists : List) -> None:

        test_image = ImageTk.PhotoImage(Image.open('./assets/fugue/icons/guitar.png'))

        for index, playlist, in enumerate(playlists):
            tree.insert('', 'end', playlist.slug, text=playlist.name)

            for song in playlist.songs:
                tree.insert(playlist.slug, 'end', song.slug + str(index), text=song.name, values=[song.artist])