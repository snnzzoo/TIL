# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4373&sca=pyd0

import sys
sys.stdin = open('945_정올.txt')

manga = {
    'Pokemon': 'Pikachu',
    'Digimon': 'Agumon',
    'Yugioh': 'Balck Magician'
}

word = input()
print(manga.get(word, "I don't know"))
