# Converts seconds to seconds.
seconds = int(input())
# Converts minutes and seconds to seconds.
minutes, seconds = divmod(seconds, 60)
# Prints a human - readable representation of a time.
print("%d M : %0d S"%(minutes,seconds))
