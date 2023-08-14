import PySimpleGUI as sg

def main():

    PLAYER_ONE = "X"
    PLAYER_TWO = "O"
    current_player = PLAYER_ONE

    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

    winner_plays = [[0,1,2], [3, 4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    button_size = (10, 5)
    layout = [[sg.Button("", key="-0-", size=button_size),
               sg.Button("", key="-1-", size=button_size),
               sg.Button("", key="-2-", size=button_size)],

              [sg.Button("", key="-3-", size=button_size),
               sg.Button("", key="-4-", size=button_size),
               sg.Button("", key="-5-", size=button_size)],

              [sg.Button("", key="-6-", size=button_size),
               sg.Button("", key="-7-", size=button_size),
               sg.Button("", key="-8-", size=button_size)],

              [sg.Button("OK", key="-OK-")]]

    window = sg.Window("Ta Te Ti", layout)
    game_end = False

    while True:
        event, _ = window.read()

        if event == sg.WINDOW_CLOSED or event == "-OK-":
            break

        if window[event].GetText() == "" and not game_end:
            index = int(event.replace("-", ""))
            if deck[index] == 0:
                deck[index] = current_player
                window[event].update(text=current_player)

                for winner_play in winner_plays:
                    if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                        if deck[winner_play[0]] == PLAYER_ONE:
                            sg.popup("¡Ganó Jugador 1!")
                        else:
                            sg.popup("¡Ganó Jugador 2!")
                        game_end = True


                if 0 not in deck:
                    sg.popup("¡Juego Terminado!")
                    game_end = True

                current_player = PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE

    window.close()

if __name__ == '__main__':
    main()
