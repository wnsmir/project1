import random

def determine_winner(user, computer):
    if user == computer:
        return "무승부!"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "사용자 승리!"
    else:
        return "컴퓨터 승리!"