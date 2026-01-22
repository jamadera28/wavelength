import random



prompter = ' \u23CE'


def control_text(*msg):
    print(*msg, sep='', end=prompter)
    input()


def control_reply(msg):
    data = -1
    while True:
        try:
            data = int(input(msg))
            break
        except ValueError:
            print("Invalid input")
    return data


def get_spikes():
    spike = random.choice(range(1,101))
    spikes = []
    if spike == 1:
        spikes.append(spike)
        spikes.append(spike + 1)
        spikes.append(spike + 2)
    elif spike == 100:
        spikes.append(spike - 2)
        spikes.append(spike - 1)
        spikes.append(spike)
    elif spike == 2:
        spikes.append(spike - 1)
        spikes.append(spike)
        spikes.append(spike + 1)
        spikes.append(spike + 2)
    elif spike == 99:
        spikes.append(spike - 2)
        spikes.append(spike - 1)
        spikes.append(spike)
        spikes.append(spike + 1)
    else:
        spikes.append(spike - 2)
        spikes.append(spike - 1)
        spikes.append(spike)
        spikes.append(spike + 1)
        spikes.append(spike + 2)
    return spikes


def show_spikes(spikes, prompt):
    line = '|'+('-'*100)+'|'
    
    if len(spikes) == 2:
        if spikes[0] == 1:
            line = '|$++' + ('-'*97) + '|'
        if spikes[0] == 2:
            line = '|+$++' + ('-'*96) + '|'
        if spikes[0] == 99:
            line = line[:1+97] + '++$|'
        if spikes[0] == 98:
            line = line[:1+96] + '++$+|'
    else:
        line = line[:spikes[0]] + '++$++' + line[spikes[4]+1:]
        
    assert(len(line) == (100 + 2))
    a, b = prompt.split('vs.')
    diff_len = 49 - len(a)
    diff_len2 = 49 - len(b)
    top = '|' + a + (' '*diff_len) + '50' + (' '*diff_len2) + b + '|'
    print(top)
    print(line) 


def main():
    prompts = set()
    with open('prompts.txt', 'r') as fp:
        prompts = set(fp.readlines()) 
        
    try:
        while True:
            control_text('Hello and welcome to CLI fan-made, not real WAVELENGTH!\nPress ^C at any time to stop playing')
            control_text('PLAYER 1: please CHOOSE a PROMPT from the pile (just press',prompter,')')
            prompt = random.choice(list(prompts))
            prompts.remove(prompt)
            prompt = prompt.replace('\n','')
            control_text('Your prompt is... ', prompt)
            control_text('PLAYER 1: close your eyes!')
            control_text('PLAYER 2: please SPIN the WHEEL (again just press', prompter,')')
            spikes = get_spikes()
            control_text('The wheel says...')
            show_spikes(spikes, prompt)
            print()
            control_text('PLAYER 2: think of a word on the  ',prompt,' spectrum. Then, tell PLAYER 1 the word!')
            control_text('When you are ready, PLAYER 2, press \u23CE to clear the screen for PLAYER 1')
            print("\n" * 100)
            a, b = prompt.split('vs.')
            diff_len = 49 - len(a)
            diff_len2 = 49 - len(b)
            top = '|' + a + (' '*diff_len) + '50' + (' '*diff_len2) + b + '|'
            print(top)
            print('|'+('-'*100)+'|')
            print()
            print('PLAYER 1: open your eyes and make your guess now!')
            guess = control_reply('Enter your guess: ')
            control_text('Are you ready to see the wheel?')
            show_spikes(spikes, prompt)
            print(' '+(' '*(guess-1))+'^'+(' '*(100-guess))+' ')
            print()
            print()
            print()
            
    except KeyboardInterrupt:
        print('\n\nAll done!')   


if __name__ == "__main__":
    main()


