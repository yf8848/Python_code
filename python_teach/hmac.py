import hmac

message=b'Hello world!'
key=b'secret'
h=hmac.new(key,message,digestmod='md5')
print(h.hexdigest())

