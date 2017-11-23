def lambda_handler(event, context):
    ''' KMP string matching '''

    def compute_prefix_function(P, len_P):
        s = [0] * len_P
        border = 0
        for i in range(1, len_P):
            while border > 0 and P[i] != P[border]:
                border = s[border - 1]
            if P[i] == P[border]:
                border += 1
            else:
                border = 0
            s[i] = border
        return s

    def find_pattern(P, T):
        '''
        Find all the occurrences of the pattern in the text
        and return a list of all positions in the text
        where the pattern starts in the text.
        '''
        S = P + '%' + T
        # we use lengths of pattern and text in a few places
        len_P = len(P)
        len_T = len(T)
        len_S = len_P + len_T + 1
        # compute prefix function for S
        s = compute_prefix_function(S, len_S)
        result = list()
        for i in range(len_P + 1, len_S):
            # if the prefix function matches the length of the pattern
            # we have a match!
            # aka a place in T which formed a border 
            # with the entirety P inside S
            if s[i] == len_P:
                result.append( i - (2 * len_P) )
        return result

    # get events
    P = event.get('P','ab')
    T = event.get('T','abcdabcd') 

    result = find_pattern(P, T)

    return {
        "pattern": P,
        "text": T,
        "matches": result
    }
    
