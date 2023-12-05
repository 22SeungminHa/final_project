from pico2d import *
from enum import Enum

import game_world

clear = []

# 리스트를 파일에 쓰기 예제
def write_2d_list_to_file(file_path):
    with open(file_path, 'w') as file:
        for row in clear:
            # 각 행의 요소를 문자열로 변환하여 파일에 쓰기
            row_str = ' '.join(map(str, row))
            file.write(row_str + '\n')

def read_2d_list_from_file(file_path):
    global clear

    with open(file_path, 'r') as file:
        for line in file:
            # 각 줄을 공백을 기준으로 나누어 정수로 변환하여 리스트에 추가
            row = list(map(int, line.strip().split()))
            clear.append(row)

def init_state(thema=-1):
    if thema == -1:
        for i in range(5):
            for j in range(8):
                clear[i][j] = 0
    else:
        for j in range(8):
            clear[thema][j] = 0
    write_2d_list_to_file('stage.json')
