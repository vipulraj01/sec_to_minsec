seconds = int(input())
minutes, seconds = divmod(seconds, 60)
print("%d M : %0d S"%(minutes,seconds))