from googletrans import Translator

def test():
    import googletrans
    print (googletrans.LANGUAGES)

def translate_one():
    translator = Translator()
    result = translator.translate('相信一切都是最好的安排！', src='zh-cn', dest='en')

    print(result.src)
    print(result.dest)
    print(result.text)

def translate_multi():
    words = ['健康', '平安', '幸福', '快乐', '如意']
    
    translator = Translator()
    results = translator.translate(words, src='zh-cn', dest='en')
    for result in results:
        print("{}->{}".format(result.origin, result.text))


if __name__ == "__main__":
    #  test()
    #  translate_one()
     translate_multi()
    
