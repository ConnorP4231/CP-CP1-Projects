top_row = ' , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12'
ones_row = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12'
twos_row = '2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24'
threes_row = '3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36'
fours_row = '4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48'
fives_row = '5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60'
sixs_row = '6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72'
sevens_row = '7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84'
eights_row = '8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96'
nines_row = '9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108'
tens_row = '10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120'
elevens_row = '11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132'
twelves_row = '12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144'
all_rows = (top_row, ones_row, twos_row, threes_row, fours_row, fives_row, sixs_row, sevens_row, eights_row, nines_row, tens_row, elevens_row, twelves_row)

print(top_row)

for rows in all_rows:
    print(rows)