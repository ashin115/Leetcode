def romanToInt( s: str) -> int:
    map ={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000

        }
    ans= 0
    for i in s:
        ans+=map[i]
    if "IV" in s:
        ans -= 2
    if "IX" in s:
        ans -= 2
    if "XL" in s:
        ans -= 20
    if "XC" in s:
        ans -= 20
    if "CD" in s:
        ans -= 200
    if "CM" in s:
        ans -= 200
    return ans


print(romanToInt(input()))