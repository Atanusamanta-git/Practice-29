def conv_sec(second):
    days, second=divmod(second, 86400)
    hours, second=divmod(second,3600)
    minuit, second=divmod(second, 60)
    return f"{days}d {hours}h {minuit}m {second}s"

total_sec=1183755
print(conv_sec(total_sec))