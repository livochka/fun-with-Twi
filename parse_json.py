# Created to parsing json files from TwitterAPI
# Creates list with information for each user
# You will get information about users friends in form of list with tuples



def parse_file(file, parameters):
    '''
    (json, list) -> list
    file: json file from Twitter
    parameters: list with all parameters you need
    return: list with tuples for each user
    '''
    users = []

    def parse(par, d):
        '''
        Recursive function to access to the deepest parts of dictionary
        par: route to value
        d: dictionary
        In result save information in the form (route to value, value) in
        current list
        '''
        if d and type(d) == list:
            d = d[0]
        if type(d) != dict:
            current.append(tuple(par + [d]))
            return par + [d]
        else:
            return list(parse(par + [key], d[key]) for key in d)

    for user in range(len(file)):
        current = []
        for param in parameters:
                # We add ti current user tuple with parameter on the first
                # position, info on the second

                # We have deep dictionary in case of 'status' parameter and
                # 'entities' parameter, so I have to handle them separately

            if param == 'status':
                parse([param], file[user]['status'])

            elif param == 'entities':
                parse([param], file[user]['entities'])
            else:
                try:
                    current.append((param, file[user][param]))
                except KeyError:
                    # If the param unavailable, we skip it
                    continue

            users.append(current)
    write_to_file(users)
    return users


def write_to_file(info):
    '''
    Writes o file
    :param info:
    :return:
    '''
    with open('results_of_008_hacker_attack', 'w', encoding='utf-8') as f:
        for user in info:
            for i in user:
                answer = str(i[-1]) if i[-1] and i[-1] != ' ' else 'Nothing ' \
                                                                   'found'
                for x in range(len(i) - 2):
                    f.write(str(i[x]) + ': \t')
                f.write(str(i[-2]) + ': ' + answer + '\n')
            f.write('\n\n')
