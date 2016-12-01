def format_duration(seconds):
    if seconds == 0:
        return 'now'
    # s = str(seconds % 60)
    # m = str((seconds / 60) % 60)
    # h = str((seconds / (60 * 60)) % 24)
    # d = str((seconds / (60 * 60 * 24)) % 365)
    # y = str((seconds / (60 * 60 * 24 * 365)))

    s = seconds % 60
    m = (seconds / 60) % 60
    h = (seconds / (60 * 60)) % 24
    d = (seconds / (60 * 60 * 24)) % 365
    y = (seconds / (60 * 60 * 24 * 365))

    # vals = {'year' : y, 'day' : d, 'hour' : h, 'minute' : m, 'second' : s}
    names = {y : 'year', d : 'day', h : 'hour', m : 'minute', s : 'second'}

    final_str = ''
    final_str += '{}{}'.format(str(y) + ' year' if y > 0 else '', 's' if y > 1 else '')
    final_str += '{}{}{}'.format(", " if len(final_str) > 0 and d > 0 else '', str(d) + ' day' if d > 0 else '', 's' if d > 1 else '')
    final_str += '{}{}{}'.format(", " if len(final_str) > 0 and h > 0 else '', str(h) + ' hour' if h > 0 else '', 's' if h > 1 else '')
    final_str += '{}{}{}'.format(", " if len(final_str) > 0 and m > 0 else '', str(m) + ' minute' if m > 0 else '', 's' if m > 1 else '')
    final_str += '{}{}{}'.format(", " if len(final_str) > 0 and s > 0 else '', str(s) + ' second' if s > 0 else '', 's' if s > 1 else '')

    # for t in ['year', 'day', 'hour', 'minute', 'second']:
    #     final_str += '{}{}{}'.format(", " if len(final_str) > 0 and vals.get(t) > 0 else '', str(vals.get(t)) + ' ' + t)

    # indices max duplicate!
    # for val in [y, d, h, m, s]:
    #     final_str += '{}{}{}'.format(", " if len(final_str) > 0 and val > 0 else '',
    #                                  str(val) + ' ' + names.get(val) if val > 0 else '',
    #                                  's' if val > 1 else '')

            ### add element number of times depending on value of a given variable


    # replace last comma by ' and'
    idx = final_str.rfind(',')
    if idx != -1:
        final_str =  final_str[:idx] + ' and' + final_str[idx + 1 :]

    return final_str

# print (format_duration(36629999941))
# print (format_duration(0))
# print (format_duration(1))
# print format_duration(120)
print format_duration(3662)