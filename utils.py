def http_request(url):    
    if url == "https://www.example.com":
        print("hello world!")
        return "Hello, world!"
    raise ValueError("Bad url")

def string_reverse(string=""):
    rts = "".join(list(reversed(string)))
    print('reversed string', rts)
    return rts

def string_length(string=""):
  return len(string)

def save_file(filename="", contents=""):
    print("Got filename", filename)
    print("Got contents", contents)