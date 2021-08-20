import argparse

from classes import CupTree



def get_cup_amount(i,j,k):
    cp = CupTree()
    cp.pour(k)
    return cp.get_cup_amount(i,j)

    
if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('ijk', help="Comma seperated Cup placement (i,j) and litres poured (k) in the form: i,j,k", default="") # defaults to stdin
    arguments = parser.parse_args()
    robot_obj = CupTree()
    if not arguments.ijk: 
        raise Exception('Please Enter valid values in the form i,j,k where i and j is coord of cup and k is litres poured')

    i, j, k = arguments.ijk.split(',')
    i = int(i.strip())
    j = int(j.strip())
    k = float(k.strip())

    print('{} L (4 d.p)'.format(get_cup_amount(i,j,k)))





