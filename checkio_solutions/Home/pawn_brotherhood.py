#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

# 
# END_DESC

def safe_pawns(pawns: set) -> int:
    protectedTiles = set()
    count = 0
    
    for x in pawns:
        pRow = str(int(x[1]) + 1)
        if x[0] != "h":
            pCol = chr(ord(x[0]) + 1)
            protectedTiles.add(pCol + pRow)
        if x[0] != "a":
            pCol = chr(ord(x[0]) - 1)
            protectedTiles.add(pCol + pRow)
    for x in pawns:
        for tiles in protectedTiles:
            if x == tiles:
                count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")