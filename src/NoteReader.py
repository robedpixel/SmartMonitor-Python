import PIL.Image

class NoteReader:
    def __init__(self):
        pass

    def read_notes_from_file(self, url: str) -> [str]:
        raise NotImplementedError()


class ExifNoteReader(NoteReader):
    def read_notes_from_file(self, url: str) -> [str]:
        img = PIL.Image.open(url)
        exif_data = img.getexif()
        print(str(exif_data))
        pass


class AppendedDataNoteReader(NoteReader):
    def read_notes_from_file(self, url: str) -> [str]:
        pass
