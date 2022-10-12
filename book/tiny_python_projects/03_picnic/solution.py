#!/usr/bin/env python3
"""Picnic game"""

import argparse


# 파이썬에서는 함수 순서가 중요하지 않다. 단지 읽는 사람을 배려해서 가장 앞에 놓는다.
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',     # 하나 이상의 위치 인수(문자열)을 받는다
                        help='Item(s) to bring')

    parser.add_argument('-s',          # 옵션 인수(축약형) 
                        '--sorted',    # 옵션 인수
                        action='store_true',   # 옵션이 있으면 True
                        help='Sort the items')

    return parser.parse_args()


# 프로그램 시작 위치
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item   # args에 있는 item 변수를 items에 저장
    num = len(items)    # 리스트에 포함된 아이템 개수를 가져온다. nargs='+'를 사용했으므로 0개인 경우는 없다.

    if args.sorted:     # args.sorted가 True 이면
        items.sort()    # 아이템 정렬한다. 원본 변환. 반환값 없음

    bringing = ''       # 가져올 아이템을 저장한 변수를 빈 문자열로 초기화
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))


# --------------------------------------------------
if __name__ == '__main__': # 여기서 main 네임스페이스에 있는지 확인해서 main() 함수 실행.
    main()
