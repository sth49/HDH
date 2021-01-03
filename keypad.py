def solution(numbers, hand):
    answer = ''
    left_hand = {1,4,7}
    right_hand = {3,6,9}
    hands = ['*','#']
    keypad = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
        '*': (3,0), 0: (3,1), '#': (3,2),
    }
    for num in numbers:
        if num in left_hand:
            hands[0]=num
            answer += 'L'
        elif num in right_hand:
            hands[1]=num
            answer += 'R'
        else:
            l_dist = abs(keypad[hands[0]][0] - keypad[num][0]) + abs(keypad[hands[0]][1] - keypad[num][1])
            r_dist = abs(keypad[hands[1]][0] - keypad[num][0]) + abs(keypad[hands[1]][1] - keypad[num][1])
            if l_dist>r_dist:
                hands[1]=num
                answer += 'R'
            elif l_dist<r_dist:
                hands[0] = num
                answer += 'L'
            else:
                if hand == 'right':
                    hands[1] = num
                    answer += 'R'
                else:
                    hands[0] = num
                    answer += 'L'
    return answer