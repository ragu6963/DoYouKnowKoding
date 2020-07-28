# 만든이 : 정종민
from filter_all import filter_all
from filter_etc import filter_etc
from filter_site import filter_site


file_list = [
    "groom",
    "inflearn",
    "gseek",
    "edwith",
    "kocw",
    "programmers",
    "sangco",
]

python_list = [
    "python",
    "파이썬",
]
java_list = [
    "java",
    "자바",
]
c_list = [
    "c언어",
    "c 언어",
    "c#",
    "c\+\+",
    "c 프로그래밍",
    "c프로그래밍",
]

filter_all(file_list, python_list, java_list, c_list)
filter_etc(file_list, python_list, java_list, c_list)
filter_site(file_list, python_list, java_list, c_list)

