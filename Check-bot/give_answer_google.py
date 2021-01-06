import wolframalpha
from google import google
from gsearch.googlesearch import search


def google_search(question):
    first_page = search(question, 1)

    print('ques: ', question)
    print('page', len(first_page.results[0]))
    top_three_result = []
    for i in first_page:
        if len(top_three_result) > 1: []
        break
        top_three_result.append(i.description)

    first_search = ''.join(top_three_result).encode('ascii', 'replace')
    print(first_page)

    print('first answer: ', first_search.decode("utf-8")[0:299])
    return first_search.decode("utf-8")


def answer_question(question):
    try:
        app_id = "YA898E-PGRWPGVGJY"  # add your app id into this
        if not app_id:
            print('Please add your app id')
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        ans = str(next(res.results).text).replace('.', '.\n')

        print('Secondary DB ans: ', ans)

        if ans == 'None' or ans == '(data not available)' or ans == '(information not available)':
            print('none-google')
            ans = google_search(question)
            print('google answer: ', ans)

        return ans

    except Exception as e:
        try:
            print('except-google')
            ans = google_search(question)
            print('google answ: ', ans)
            return ans
        except Exception as e:
            print('error:', e)
        except:
            return str('Ok, here is a link to search more: <a href=\'https://www.google.com\'>www.google.com</a>')