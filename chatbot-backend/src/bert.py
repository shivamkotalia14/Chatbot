import neuspell
from neuspell import BertChecker


from src.store import Store

class Bert:

    checker = BertChecker()
    checker.from_pretrained()

    @classmethod
    def fix(cls):

        print("WEE WOO WEE WOO")

        Store.raw_word = ""

        raw_transcription = " ".join(Store.raw_transcription).lower()
        print(raw_transcription)

        corrected = cls.checker.correct(raw_transcription).strip()
        print(corrected)

        Store.corrected_transcription = corrected.upper().split()
        
