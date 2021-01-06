import sys

chatbot_enabled = False


# PreProcessor
def unescape(bot, statement):
    if sys.version_info[0] < 3:
        from HTMLParser import HTMLParser
        html = HTMLParser()
    else:
        import html
        statement.text = html.unescape(statement.text)
        return statement


def remove_breakline(text):
    return text.replace('\n', '<br>')
