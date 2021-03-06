from pandas import *

rng = DateRange('1/3/2011', '11/30/2011', offset=datetools.Minute())
rng5 = DateRange('1/3/2011', '11/30/2011', offset=datetools.Minute(5))

df = DataFrame(np.random.randn(len(rng), 5), index=rng,
               columns=list('OHLCV'))

gp = rng5.asof

grouped = df.groupby(gp)

def get1(dt):
    k = gp(dt)
    return grouped.get_group(k)

def get2(dt):
    k = gp(dt)
    return df.ix[grouped.groups[k]]

def f():
    for i, date in enumerate(df.index):
        if i % 10000 == 0:
            print i
        get1(date)

def g():
    for i, date in enumerate(df.index):
        if i % 10000 == 0:
            print i
        get2(date)

