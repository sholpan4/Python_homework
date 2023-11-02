def get_diag_words(matrix):
    main_diag = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
    anti_diag = [matrix[i][len(matrix) - i - 1] for i in range(min(len(matrix), len(matrix[0])))]

    main_word = ''.join(main_diag)
    anti_word = ''.join(anti_diag)

    return f"{main_word} {anti_word}"

def test_get_diag_words():
    input1 = [['ж', 'ф', 'л'],
              ['р', 'и', 'а'],
              ['с', 'з', 'л']]
    expect1 = "жил лис"
    assert get_diag_words(input1) == expect1

    input2 = [['б', 'ф', 'л', 'т', ']', 'в'],
              ['р', 'е', 'а', 'о', 'о', 'щ'],
              ['е', 'и', 'л', 'р', 'э', 'к'],
              ['г', 'ы', 'о', 'а', 'ф', 'о'],
              ['н', 'н', 'а', 'а', 'я', 'ч'],
              ['а', 'з', 'л', 'ц', 'в', ' ']]
    expect2 = "белая  ворона"
    assert get_diag_words(input2) == expect2

    input3 = []
    expect3 = ""
    assert get_diag_words(input3) == expect3

test_get_diag_words()