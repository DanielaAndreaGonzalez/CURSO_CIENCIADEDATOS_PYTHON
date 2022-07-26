from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator
from pandas import json_normalize,DataFrame
from ibm_watson import language_translator_v3



url_s2t= ""
iam_apikey_s2t = ""

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

filename = 'C:\\Users\\danie\\Downloads\\ingles.mp3'

with open(filename, mode = "rb") as wav:
    response = s2t.recognize(method='POST',audio=wav,content_type='audio/mp3')



json_normalize(response.result['results'],"alternatives")

recognized_text = response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)

url_lt=''
apikey_lt=''

version_lt='2018-05-01'



