import time

class Funnel():
    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity
        self.leaking_rate = leaking_rate
        self.left_quota = capacity
        self.leaking_ts = time.time()


    def make_space(self):
        new_ts = time.time()
        delta_ts = new_ts - self.leaking_ts
        delta_quota = delta_ts * self.leaking_rate
        if delta_quota < 1:
            return 

        self.left_quota = delta_quota
        self.leaking_ts = new_ts

        if self.left_quota > self.capacity:
            self.left_quota = self.capacity


    def watering(self, quota):
        self.make_space()
        if self.left_quota >= quota:
            self.left_quota -= quota
            return True

        return False


funnels = {}

def is_action_allowed(
        user_id, action_key, capacity, leaking_rate ):
    key = f"{user_id}:{action_key}"

    funnel = funnels.get(key)

    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel

    return funnel.watering(1)

for i in range(20):
    print(is_action_allowed('jack', 'post', 15, 0.5))
