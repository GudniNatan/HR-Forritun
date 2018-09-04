secs_str = int(input("Input seconds: ")) # do not change this line
hours = secs_str // (60 * 60 )
secs_str -= hours * 60 * 60
minutes = secs_str // 60
secs_str -= minutes * 60
seconds = secs_str
print(hours,":",minutes,":",seconds) # do not change this line