PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def check_brackets(line):
    stack = []
    for index in range(len(line)):
        ch = line[index]
        if ch in PAIRS:
            stack.append((ch, index))
        elif ch in PAIRS.values():
            if not stack:
                return index, ch
            open_bracket, unused = stack.pop()
            if PAIRS[open_bracket] != ch:
                return index, ch

    if stack:
        return stack[-1][1], stack[-1][0]

    return None


def print_bracket_check(line):
    result = check_brackets(line)

    if result is None:
        print('Balanced')
        return

    position, bracket = result
    print(f'Problem at position {position}: {bracket}')
    print(line)
    print(' ' * position + '^')


if __name__ == '__main__':
    text = input('Enter a line of code: ')
    print_bracket_check(text)