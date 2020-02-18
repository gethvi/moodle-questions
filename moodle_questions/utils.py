def cdata_str(text):
    if text == None:
        return ""
    return f"<![CDATA[{text}]]>"

def estr(text):
    if text == None:
        return ""
    else:
        return str(text)