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

python_list = ["Python", "파이썬", "python", "PYTHON"]
java_list = ["Java", "자바", "JAVA", "java"]
c_list = [
    "C언어",
    "c언어",
    "C#",
    "C\+\+",
    "c\+\+",
    "c#",
    "c언어",
    "c 언어",
    "C 언어",
    "C 프로그래밍",
    "c 프로그래밍",
    "c프로그래밍",
    "C프로그래밍",
]

filter_all(file_list, python_list, java_list, c_list)
filter_etc(file_list, python_list, java_list, c_list)
filter_site(file_list, python_list, java_list, c_list)

