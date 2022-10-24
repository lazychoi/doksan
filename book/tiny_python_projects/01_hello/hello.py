#! /usr/bin/env python
# 셔뱅은 이 코드를 실행할 때 어떤 프로그램을 사용할지 os에게 알려줌
"""
Author: Ken Youens-Clark
Purpose: Say hello
"""

# 인수를 전달할 때 사용하는 모듈
import argparse


def get_args():
    """
    인수 전용 함수
    """
    # 이 parser가 모든 인수를 인지한다. description에 있는 내용이 도움말로 표시됨
    parser = argparse.ArgumentParser(description="Say hello")

    # 인사할 사람의 이름('name')을 인수로 전달한다고 파서에게 알려줌
    # parser.add_argument('name', help='Name to greet')

    # '-n'과 '--name'을 각각 축약형(short)과 일반형(long) 인수명으로 추가
    # 인수명을 추가하지 않을 경우 기본값인 'world'가 출력됨
    # 'metavar'는 인수명
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()

    # args.name 값을 사용해 인사 메시지 출력(metavar에 지정한 이름)
    print("Hello, " + args.name + "!")


# 모든 프로그램과 모듈은 __name__이라는 변수로 접근할 수 있는 이름을 갖고 있다.
# 프로그램이 실행될 때 __name__이 __main__이라는 값으로 설정된다.
if __name__ == "__main__":
    main()

# 실행 결과 ======================================
# $ ./hello.py => Hello, World!
# $ ./hello.py -n Jun => Hello, Jun!
# $ ./hello.py -h => 도움말 출력
# usage: hello.py [-h] [-n name]
#
# Say hello
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -n name, --name name  Name to greet
