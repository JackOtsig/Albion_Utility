2550449
#[0] = nutrition
#[1] = market value
#[2] = food
#[3] = building
values = [
    (252, 1642, 'wheat soup', 'smelter'),
    (77, 380, 'carrot soup', 'lumbermill'),
    (243, 1459, 'mutton sandwich', 'mage tower'),
    (272, 1996, 'mutton stew', 'warrior forge'),
    (756, 4577, 'potato salad', 'hunter lodge'),
    (77, 469, 'chicken omelette', 'weaver'),
    (78, 1000, 'chicken pie', 'tanner'), #rare
    (266, 1563, 'goose pie', 'cook'),
    (756, 4190, 'cabbage soup', 'butcher'),
    (252, 2003, 'turnip salad', 'toolmaker'),
    (77, 513, 'bean salad', 'stonemason')
]

def main():
    t = 0
    pt = 0
    for value in values:
        nutrition = value[0] * 2
        cost = value[1]
        silver_per_nut_lol = cost / nutrition
        cost100 = silver_per_nut_lol * 100
        cost1000 = silver_per_nut_lol * 1000
        cost100 = round(cost100, 1)
        cost1000 = round(cost1000, 1)
        silver_per_nut_lol = round(silver_per_nut_lol, 1)
        to_full = 795000 / nutrition
        price_to_full = to_full * cost
        tf50 = to_full*0.5
        ptf50 = price_to_full*0.5
        tf25 = to_full*0.25
        ptf25 = price_to_full*0.25
        tf10 = to_full*0.1
        ptf10 = price_to_full*0.1
        t += round(to_full, 1)
        pt += round(price_to_full, 1)
        print(value[2], 'at', value[3], 'for',  silver_per_nut_lol, 'per')
        print('to fill:', round(to_full, 1), 'for', round(price_to_full, 1))
        print('50% :', round(tf50, 1), 'for', round(ptf50, 1))
        print('25% :', round(tf25, 1), 'for', round(ptf25, 1))
        print('10% :', round(tf10, 1), 'for', round(ptf10, 1))
        print(cost100, 'per 100 \n', cost1000, 'payback')
    print('total to all full:', t, 'for', pt)
    t50 = t * 0.5
    t25 = t * 0.25
    t10 = t * 0.1
    pt50 = pt * 0.5
    pt25 = pt * 0.25
    pt10 = pt * 0.1
    print('50%:', round(t50, 1), 'for', round(pt50, 1))
    print('25%:', round(t25, 1), 'for', round(pt25, 1))
    print('10%:', round(t10, 1), 'for', round(pt10, 1))
if __name__ == '__main__':
    main()