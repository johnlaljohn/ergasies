import tweepy
from tweepy import OAuthHandler

consumer_key = 'pxlybvSXTYFyM7hzrQjxugo9d'
consumer_secret = 'TRuvKjAsm3m6zxSRjZDPuxex3YzMDVdHkNFFE6yHkB3leRo0Ks'
access_token = 'hkrYh0q9NzrKIm0ehU1jgOLEQRr9PXk'
access_secret = 'OxGIRTskcgBnPeSLgZGcllLrbr5k67Z35HLRFaJikeOZD'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user1=raw_input('dwse prwto xrhsth')
lis1=[ ]
user_timeline = api.user_timeline(screen_name=user1,count=11)
for tweet in user_timeline:
    t1 = tweet.text
    utf8_1 = t1.encode("utf-8")
    lis1.append(utf8_1)

user2=raw_input('dwse deytero xrhsth')
lis2=[ ]
user_timeline = api.user_timeline(screen_name=user2,count=11)
for tweet in user_timeline:
    t2 = tweet.text
    utf8_2 = t2.encode("utf-8")
    lis2.append(utf8_2)

new1 = []
new2 = []
for item in lis1:
    new1.extend(lis1.split())

for item in lis2:
    new2.extend(lis2.split())

prwto=len(new1)
deytero=len(new2)

if (prwto > deytero):
    print user1
elif (prwto < deytero):
    print user2
else:
    print "oi dyo xrhstes exoyn ton idio arithmo leksewn sta tweets toys"
