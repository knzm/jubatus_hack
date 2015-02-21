# -*- coding: utf-8 -*-

from __future__ import print_function

from time import sleep

from jubatus.common import Datum
import jubatus.recommender.client


def read(f):
    col_names = (
        'pname', 'team', 'bave', 'games', 'pa', 'atbat', 'hit', 'homerun',
        'runsbat', 'stolen', 'bob', 'hbp', 'strikeout', 'sacrifice', 'dp',
        'slg', 'obp', 'ops', 'rc27', 'xr27',
        )
    for line in f:
        d = {}
        for key, val in zip(col_names, line[:-1].split(',')):
            if key in ('pname', 'team'):
                val = val.decode('utf-8')
            else:
                val = float(val)
            d[key] = val
        yield d


def main(host='localhost'):
    recommender = jubatus.recommender.client.Recommender(
        host, 9199, '', timeout=10)

    items = []
    with open('baseball.csv') as f:
        items = list(read(f))

    # print("sleeping")
    # sleep(60)

    print("updating")
    for item in items:
        d = Datum({
          u"チーム": item['team'],
          u"打率": item['bave'],
          u"試合数": item['games'],
          u"打席": item['pa'],
          u"打数": item['atbat'],
          u"安打": item['hit'],
          u"本塁打": item['homerun'],
          u"打点": item['runsbat'],
          u"盗塁": item['stolen'],
          u"四球": item['bob'],
          u"死球": item['hbp'],
          u"三振": item['strikeout'],
          u"犠打": item['sacrifice'],
          u"併殺打": item['dp'],
          u"長打率": item['slg'],
          u"出塁率": item['obp'],
          u"OPS": item['ops'],
          u"RC27": item['rc27'],
          u"XR27": item['xr27'],
          })
        recommender.update_row(item['pname'], d)

    print("sleeping")
    sleep(10)

    print("analyzing")
    for item in items:
        sr = recommender.similar_row_from_id(item['pname'] , 4)
        names = [row.id.decode('utf-8') for row in sr[1:]]
        print(u"player {0} is similar to : {1}".format(
                item['pname'], u", ".join(names)).encode('utf-8'))


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
