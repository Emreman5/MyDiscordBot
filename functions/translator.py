import googletrans
from googletrans import Translator
import pandas as pd# Desteklenen dil sayısı
def get_translate(string):
    translator = Translator()
    return translator.translate(string, dest = "tr").text