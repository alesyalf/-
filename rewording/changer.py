import pymorphy2


def change(old, new):
    morph = pymorphy2.MorphAnalyzer()
    if len(new.split(' ')) == 1:
        old_parse = morph.parse(old)[0]
        new_parse = morph.parse(new)[0]
        if old_parse.tag.POS == 'NOUN' and new_parse.tag.POS == 'NOUN':
            pad = old_parse.tag.case
            new = new_parse.inflect({pad}).word
            return new
        if old_parse.tag.POS == 'INFN' and new_parse.tag.POS == 'INFN':
            return new
        if old_parse.tag.POS == 'INFN' and new_parse.tag.POS == 'VERB':
            return new_parse.normal_form
        if old_parse.tag.POS == 'VERB' and new_parse.tag.POS == 'INFN':
            time = old_parse.tag.tense
            number = old_parse.tag.number
            person = old_parse.tag.person
            if number == 'plur' and time == 'past':
                new = new_parse.inflect({time, number}).word
                return new
            if number == 'plur':
                new = new_parse.inflect({time, number, person}).word
                return new
            if (time == 'pres'):
                person = old_parse.tag.person
                new = new_parse.inflect({time, number, person}).word
                return new
            gender = old_parse.tag.gender
            new = new_parse.inflect({time, number, gender}).word
            return new
        if old_parse.tag.POS == 'VERB' and new_parse.tag.POS == 'VERB':
            time = old_parse.tag.tense
            number = old_parse.tag.number
            if number == 'plur':
                new = new_parse.inflect({time, number}).word
                return new
            person = old_parse.tag.person
            if time == 'past':
                gender = old_parse.tag.gender
                new = new_parse.inflect({time, number, gender, person}).word
                return new
            new = new_parse.inflect({time, number, person}).word
            return new
    else:
        old_parse = morph.parse(old.split(' ')[0])[0]
        if old_parse.tag.POS == 'VERB':
            verb_positions = []
            splitted = new.split(' ')
            for i, word in enumerate(splitted):
                word_parse = morph.parse(word)[0]
                if word_parse.tag.POS == 'VERB' or word_parse.tag.POS == 'INFN':
                    verb_positions.append(i)
            for k in verb_positions:
                new_parse = morph.parse(new.split(' ')[k])[0]
                time = old_parse.tag.tense
                number = old_parse.tag.number
                person = old_parse.tag.person
                if number == 'plur':
                    new_change_word = new_parse.inflect({time, number, person}).word
                    split_list = new.split(' ')
                    split_list[k] = new_change_word
                    new = ' '.join(split_list)
                    continue
                if time == 'past':
                    gender = old_parse.tag.gender
                    new_change_word = new_parse.inflect({time, number, gender}).word
                    split_list = new.split(' ')
                    split_list[k] = new_change_word
                    new = ' '.join(split_list)
                    continue
                person = old_parse.tag.person
                new_change_word = new_parse.inflect({time, number, person}).word
                split_list = new.split(' ')
                split_list[k] = new_change_word
                new = ' '.join(split_list)
            return new
        if old_parse.tag.POS == 'INFN':
            k = 0
            for i in range(len(new.split(' '))):
                word = new.split(' ')[i]
                word_parse = morph.parse(word)[0]
                if word_parse.tag.POS == 'INFN':
                    return new
                if word_parse.tag.POS == 'VERB':
                    k = i
                    break
            new_parse = morph.parse(new.split(' ')[k])[0]
            new_change_word = new_parse.normal_form
            split_list = new.split(' ')
            split_list[k] = new_change_word
            new = ' '.join(split_list)
            return new
        if old_parse.tag.POS == 'NOUN':
            noun_positions = []
            for i in range(len(new.split(' '))):
                word = new.split(' ')[i]
                word_parse = morph.parse(word)[0]
                if word_parse.tag.POS == 'NOUN':
                    noun_positions.append(i)
            if new.split(' ')[1] == 'и' or new.split(' ')[1] == 'или':
                for k in noun_positions:
                    pad = old_parse.tag.case
                    number = old_parse.tag.number
                    new_parse = morph.parse(new.split(' ')[k])[0]
                    new_change_word = new_parse.inflect({pad, number}).word
                    split_list = new.split(' ')
                    split_list[k] = new_change_word
                    new = ' '.join(split_list)
                return new
            else:
                pad = old_parse.tag.case
                number = old_parse.tag.number
                new_parse = morph.parse(new.split(' ')[0])[0]
                new_change_word = new_parse.inflect({pad, number}).word
                split_list = new.split(' ')
                split_list[0] = new_change_word
                new = ' '.join(split_list)
            return new
