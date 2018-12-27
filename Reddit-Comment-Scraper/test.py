import praw
import matplotlib.pyplot as plt
from collections import Counter

#top secret data 
reddit = praw.Reddit(client_id='id', \
                     client_secret='secret', \
                     user_agent='Scraper', \
                     username='username', \
                     password='password')

subredditname = "politics"

subreddit = reddit.subreddit(subredditname)

top_subbreddit = subreddit.top()
count = 0
max = 10000
print('success')
words = []
wordCount = {}
commonWords = {'that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we',
'all','when','had','see','his','him','who','by','her','she','our','thing','-',
'now','what','going','been','we',"I'm",'than','any','because','We','even',
'said','only','want','other','into','He','what','i','That','thought',
'think',"that's",'Is','much','too','still','got','its','theres','Cant','Lmao',
'My','these','those','[deleted]','if','It',"It's","I've"}

for submission in subreddit.top(limit=500):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        tempWords = top_level_comment.body.split(' ')
        filter(str.isalpha, words)
        words += [word for word in tempWords if word not in commonWords]
    if(count == max):
            break

word_count = Counter(words)

top_words = word_count.most_common(10)

topWords = [word[0] for word in top_words]
topWordsCount = [value[1] for value in top_words]

plt.title('Top comments for: r/' + subredditname)
plt.pie(topWordsCount, labels=topWords,autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
