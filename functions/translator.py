import googletrans
from googletrans import Translator
import pandas as pd
def get_translate(string):
    translator = Translator()
    return translator.translate(string, dest = "tr").text