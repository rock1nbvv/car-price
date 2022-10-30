age = ['bad', 'mediocre', 'average', 'normal', 'good']
mileage = ['bad', 'mediocre', 'average', 'normal', 'good']
repairments = ['bad', 'mediocre', 'average', 'normal', 'good']

output = ['terrible', 'very bad', 'bad', 'normal', 'good', 'very good', 'perfect']


def trapezoid(x, a, b, c, d):
    return max(min((x - a) / (b - a), 1, (d - x) / (d - c)), 0)


def triangular(x, a, b, c):
    return max(min((x - a) / (b - a), (c - x) / (c - b)), 0)


def terrible(x, a=0, b=1, c=3, d=12):
    return trapezoid(x, a, b, c, d)


def veryBad(x, a=6, b=12, c=18, d=24):
    return trapezoid(x, a, b, c, d)


def bad(x, a=18, b=24, c=30):
    return triangular(x, a, b, c)


def normal(x, a=24, b=30, c=36, d=42):
    return trapezoid(x, a, b, c, d)


def good(x, a=36, b=42, c=48):
    return triangular(x, a, b, c)


def veryGood(x, a=42, b=48, c=54):
    return triangular(x, a, b, c)


def perfect(x, a=51, b=54, c=59, d=60):
    return trapezoid(x, a, b, c, d)


for age_count, age_item in enumerate(age):
    for mileage_count, mileage_item in enumerate(mileage):
        for repairments_count, repairments_item in enumerate(repairments):
            current = age_count * 5 + mileage_count * 5 + repairments_count * 5
            values = [terrible(current), veryBad(current), bad(current), normal(current), good(current),
                      veryGood(current), perfect(current)]
            print('((\''+age_item + '\', \'' + mileage_item + '\', \'' + repairments_item + '\'), \'' + output[values.index(max(values))]+'\'),')
