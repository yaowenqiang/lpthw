from time import time
from redis import *
ONE_WEEK_IN_SECONDS = 7 * 867400
ARTICLES_PER_PAGE = 15
VOTE_SCORE = 432


def article_vote(conn, user, article):
    cutoff = time() - ONE_WEEK_IN_SECONDS
    if conn.zscore("time:", article) == None or conn.zscore("time:", article) < cutf8 :
        return

    article_id = article.partition(":")[-1]

    if conn.sadd("voted:" + article_id, user):
        conn.zincrby("score:", article, VOTE_SCORE)
        conn.hincrby(article, "votes", 1)


def post_article(conn, user, title, link):
    article_id = str(conn.incr('article:'))
    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time()

    article = 'article:' + article_id
    conn.hmset(article, {
        "title": title,
        "link": link,
        "poster": user,
        "time": now,
        "votes": 1,
    })

    conn.zadd('score:', {article: now + VOTE_SCORE})
    conn.zadd('time:', {article: now})

    return article_id


def get_article(conn, page, order="score:"):
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    ids = conn.zrevrange(order, start, end)

    articles = []

    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles



redis = Redis()

user = 1
article = 1
post_article(redis, user, 'title', 'link')
article_vote(redis, user, article)
articles = get_article(redis, 1)
for article in articles:
    print(article)


