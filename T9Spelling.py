alphas = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_pattern(test_str):
    key_pad = dict()
    ite_alpha = 0 #iterates over all alphabets
    digits = 2    #digits varialble takes values from 2-9
    ntimes = 1    #number of time you need to print a particular alphabet. Eg. to print 'b' print '2' twice

    #Make a Dictionary of all patterns and store it in 'key_pad'.
    #Eg: key_pad['b'] = '22'

    while ite_alpha < 26:
        if digits == 7 or digits == 9:
            times_limit = 4
        else:
            times_limit = 3
        ntimes = 1
        while ntimes <= times_limit and ite_alpha < 26:

            key_pad[alphas[ite_alpha]] = str(digits) * ntimes
            ntimes = ntimes + 1
            ite_alpha = ite_alpha + 1
        digits = digits + 1

    key_pad[' '] = '0'
    previous_key = -1
    answer = ''

    #for every character in the input string, just retrieve its corresponding pattern from dictionary.
    for alpha in test_str:
        present_key = int(key_pad[alpha][0])

        #if present key was same as previous, add space
        if present_key == previous_key:
            answer = answer + ' '

        answer = answer + str(key_pad[alpha])
        previous_key = present_key

    return answer

def main():
    ifile = open('input.txt', 'r')
    ofile = open('output.txt', 'w')
    ite = 0
    for line in ifile:
        #To remove the first line, '100'
        if ite == 0:
            ite = ite + 1
            continue

        #strip newline
        line = line[:-1]
        answer = get_pattern(line)
        ofile.write('Case #' + str(ite) + ': ' + answer + '\n')
        ite = ite + 1

if __name__ == '__main__':
    main();

