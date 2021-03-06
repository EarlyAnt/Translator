from googletrans import Translator


def test():
    import googletrans
    print(googletrans.LANGUAGES)


def translate_one(content, src, dest):
    translator = Translator()
    result = translator.translate(text=content, src=src, dest=dest)

    print(result.src)
    print(result.dest)
    print(result.text)

    return {content: result.text}


def translate_multi(words, src, dest):
    translated = {}

    translator = Translator()
    results = translator.translate(words, src=src, dest=dest)

    for result in results:
        print("{}->{}".format(result.origin, result.text))
        translated[result.origin] = result.text
    return translated


if __name__ == "__main__":
    #  test()

    translate_one(content="相信一切都是最好的安排！", src="zh-cn", dest="en")

    # words = ['健康', '平安', '幸福', '快乐', '如意']
    # translate_multi(words=words, src='zh-cn', dest='en')
