from grin.parsing import parse
from grin.token import GrinTokenKind, GrinToken


ASSIGN = dict()
LABELS = dict()
CALLSTACKS = []


def _generate_label(code: str):
    for i in range(len(code)):
        parsed = list(parse([code[i]]))

        if not parsed:
            continue

        command = parsed[0][0].kind
        if command == GrinTokenKind.IDENTIFIER:
            label = parsed[0][0].value
            LABELS[label] = i


def get_token_value(token: GrinToken):
    if token.kind == GrinTokenKind.IDENTIFIER:
        return ASSIGN[token.value]
    return token.value


def excute(code):

    _generate_label(code)

    index = 0
    while index < len(code):
        parsed = list(parse([code[index]]))

        # Dealing with dot
        if not parsed:
            return

        command = parsed[0][0].kind

        # Handling Labels
        if command == GrinTokenKind.IDENTIFIER:
            parsed[0].pop(0)
            parsed[0].pop(0)
            command = parsed[0][0].kind

        if command == GrinTokenKind.LET:
            vars = parsed[0][1].value
            ASSIGN[vars] = get_token_value(parsed[0][2])

        elif command == GrinTokenKind.PRINT:
            kind = parsed[0][1].kind
            value = parsed[0][1].value
            if kind == GrinTokenKind.IDENTIFIER:
                if value not in ASSIGN.keys():
                    print(0)
                else:
                    print(ASSIGN[value])
            elif kind == GrinTokenKind.LITERAL_STRING:
                print(value)

        elif command == GrinTokenKind.INNUM:
            inp = input()
            value = parsed[0][1].value
            ASSIGN[value] = int(inp)

        elif command == GrinTokenKind.INSTR:
            inp = input()
            value = parsed[0][1].value
            ASSIGN[value] = inp

        elif command == GrinTokenKind.ADD:
            v1 = parsed[0][1].value
            v2 = get_token_value(parsed[0][2])
            ASSIGN[v1] += v2

        elif command == GrinTokenKind.SUB:
            v1 = parsed[0][1].value
            v2 = get_token_value(parsed[0][2])
            ASSIGN[v1] -= v2

        elif command == GrinTokenKind.MULT:
            v1 = parsed[0][1].value
            v2 = get_token_value(parsed[0][2])
            if isinstance(ASSIGN[v1], int) and isinstance(v2, int):
                ASSIGN[v1] = int(ASSIGN[v1] * v2)
            else:
                ASSIGN[v1] = ASSIGN[v1] * v2

        elif command == GrinTokenKind.DIV:
            v1 = parsed[0][1].value
            v2 = get_token_value(parsed[0][2])
            if isinstance(ASSIGN[v1], int) and isinstance(v2, int):
                ASSIGN[v1] = int(ASSIGN[v1] / v2)
            else:
                ASSIGN[v1] = ASSIGN[v1] / v2

        elif command in [GrinTokenKind.GOTO, GrinTokenKind.GOSUB]:
            if command == GrinTokenKind.GOSUB:
                CALLSTACKS.append(index)

            goto_kind = parsed[0][1].kind
            if goto_kind == GrinTokenKind.IDENTIFIER:
                if isinstance(ASSIGN[parsed[0][1].value], int):
                    index += ASSIGN[parsed[0][1].value]
                elif isinstance(ASSIGN[parsed[0][1].value], str):
                    index = LABELS[ASSIGN[parsed[0][1].value]]
                continue

            if goto_kind == GrinTokenKind.LITERAL_INTEGER:
                index += parsed[0][1].value
                continue

            elif goto_kind == GrinTokenKind.LITERAL_STRING:
                label = parsed[0][1].value
                index = LABELS[label]
                continue

            else:
                print('Not dealt with goto_kind:', goto_kind)

        elif command == GrinTokenKind.RETURN:
            index = CALLSTACKS.pop() + 1
            continue

        elif command == GrinTokenKind.END:
            return

        else:
            print('The command was not processed:', command, parsed)


        index += 1
