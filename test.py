<<<<<<< HEAD
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
=======
def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요 (종료하려면 '끝'을 입력하세요): ")
        if user_choice in ["가위", "바위", "보"]:
            return user_choice
        elif user_choice == '끝':
            return '끝'
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
>>>>>>> branch_ec
def play_game():
    print("가위 바위 보 게임을 시작합니다!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"사용자 선택: {user_choice}")
    print(f"컴퓨터 선택: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
