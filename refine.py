focus_costs = (
    (0),
    (0),
    #2
    (10),
    #3
    (24),
    #4
    (48, 89, 143, 239),
    #5
    (89, 160, 269, 461),
    #6
    (160, 284, 487, 844),
    #7
    (284, 500, 866, 1508),
    #8
    (500, 877, 1527, 2666)
)

#change these
tier = 5.3
level = 41
amount = 999
focus = 20000
#royal city with bonus  : 53.9
#royal city             : 43.5
#royal island with bonus: 49.7
#royal island           : 37.1
#blackzone hideout      : 46
rrr = 46

#tells you how much focus you need to refine a certain amount of materials
#note: this counts in "crafts" so 1 amount isnt one flax but 2 flax and 1 simple cloth

def calc_focus(tier, level, amount):
    fef = level*250
    halve = 0
    while fef > 10000:
        fef -= 10000
        halve += 1
    if type(tier) == int:
        focus = focus_costs[tier][0] * amount
    if type(tier) == float:
        tiersplit = str(tier).split('.')
        focus = focus_costs[int(tiersplit[0])][int(tiersplit[1])] * amount
    while halve > 0:
        focus /= 2
        halve -= 1
    return focus

#tells you how many resources it will yeild using a certain amount of focus
def calc_out(tier, level, focus, rrr):
    fef = level*250
    halve = 0
    while fef > 10000:
        fef -= 10000
        halve += 1
    if type(tier) == int:
        focus_cost = focus_costs[tier][0]
    if type(tier) == float:
        tiersplit = str(tier).split('.')
        focus_cost = focus_costs[int(tiersplit[0])][int(tiersplit[1])]
    while halve > 0:
        focus_cost /= 2
        halve -= 1
    output = focus / focus_cost
    rrd = rrr / 100
    rrd += 1
    output *= rrd
    return output



print(calc_focus(tier,level,amount))
#print(calc_out(tier,level,focus,rrr))