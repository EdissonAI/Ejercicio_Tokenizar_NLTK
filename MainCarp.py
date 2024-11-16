# Analisis de frecuencias de palabras NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import Counter

texto = """A medida que la IA tiene una presencia cada vez más común en nuestras vidas, 
también nos enfrentamos a una serie de desafíos y preocupaciones los cuales debemos 
abordar con urgencia. De este modo, se confirma que la inteligencia artificial tiene 
consecuencias negativas también. La ciberseguridad se torna en una de las principales 
preocupaciones, ya que los sistemas impulsados ​​por inteligencia artificial pueden ser 
objetivos de ciberataques sofisticados con consecuencias potencialmente devastadoras."""

# Tokenizamos(dividimos) el texto
palabras = word_tokenize(texto, language="spanish")
# print(palabras)

# Eliminamos los conectores con StopWords
stop_words = set(stopwords.words("spanish"))

# Filtramos las palabras que no estan en la lista de StopWords

palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words and palabra.isalpha()]
print(palabras_filtradas) # Genera la lista de palabras filtradas

# Analisis de frecuencia de palabras
frecuencia_palabras = FreqDist(palabras_filtradas)
print(frecuencia_palabras.most_common(10))