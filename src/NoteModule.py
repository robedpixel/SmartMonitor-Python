import PIL.Image

class NoteModule:
    def __init__(self):
        pass

    def read_notes_from_file(self, url: str) -> [str]:
        raise NotImplementedError()


class ExifNoteModule(NoteModule):
    def read_notes_from_file(self, url: str) -> [str]:
        img = PIL.Image.open(url)
        exif_data = img.getexif()
        if exif_data:
            print(str(exif_data))
        pass


class AppendedDataNoteModule(NoteModule):
    def read_notes_from_file(self, url: str) -> [str]:
        pass
