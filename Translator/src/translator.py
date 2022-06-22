from googletrans import Translator
# import googletrans

# print (googletrans.LANGUAGES)

translator = Translator()
# result = translator.translate('相信一切都是最好的安排！', src='zh-cn', dest='en')
result = translator.translate('相信一切都是最好的安排！', dest='en')

print(result.src)
print(result.dest)
print(result.text)



