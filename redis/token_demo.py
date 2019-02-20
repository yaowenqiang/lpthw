import time

QUIT = False
LIMIT = 100


def check_token(conn, token):
    return conn.hget('login:', token)


def update_token(conn, token, user, item=None):
    timestamp = time.time()

    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)

    if item:
        conn.zadd("viewed:" + token, item, timestamp)
        conn.zremrangebyrank("viewed:" + token, 0, -26)


def clear_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')

        if size <= LIMIT:
            time.sleep(1)

            continue

        end_index = max(size - LIMIT, 100)

        tokens = conn.zrange('recent:', 0, end_index - 1)

        session_keys = []

        for token in tokens:
            session_keys.append("viewed:" + token)

        conn.delete(*session_keys)
        conn.hdel('login:', *tokens)
        conn.zrem('recent:', *tokens)





