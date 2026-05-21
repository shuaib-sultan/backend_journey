from datetime import datetime ,timedelta ,timezone
class Ratelimiter:
  def __init__(self, limit , window ) :
    self.limit= limit
    self.window= window
    self.storage={}
  def is_allowed(self,key): # key can be [ip ,id , api key] it's gernal 
    now=datetime.now(timezone.utc)
    self.storage = { k:v for k ,v in self.storage.items() if now <=(self.storage[k]["start_time"] + timedelta(seconds=self.window))  }

    if key not in self.storage:
      self.storage[key]={
        "count":1,
        "start_time": now
      }
    else :
      self.storage[key]["count"]+=1
      if self.storage[key]["count"] > self.limit:
        return False
    return True