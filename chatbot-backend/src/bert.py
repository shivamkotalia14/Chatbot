

from src.store import Store

class Bert:

    @classmethod
    def fix(cls):

        print("WEE WOO WEE WOO")

        Store.raw_word = ""

        raw_transcription = " ".join(Store.raw_transcription).lower()
        print(raw_transcription)

        Store.corrected_transcription = raw_transcription
