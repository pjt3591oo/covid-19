def pad (string, length=10, char=" "):
    string = str(string)

    if len(string) > length or len(char) > 1:
        return string

    strlen = len(string)
    padlen = abs(length - strlen)
    string = string + (char * padlen)
    return string

def print_table(lines, header=None, totalwidth=80, mincol=4, splitter=("|", "-", "+")):
    splitter, horiz, cross = splitter

    if splitter == "":
        splitter = " "
    if horiz == "":
        horiz = " "
    if cross == "":
        cross = " "

    width = {}
    total = {}
    average = {}
    fair_average = {}

    if header:
        col = 0
        for each in header:
            width[col] = len(each)
            col += 1

    num_lines = 0
    for line in lines:
        col = 0
        num_lines += 1
        for each in line:
            try:
                if len(each) > width[col]:
                    width[col] = len(each)
            except:
                width[col] = len(each)

            try:
                total[col] += len(each)
            except:
                total[col] = len(each)

            col += 1
    num_columns = col

    total_of_averages = 0
    for x in range(0,num_columns):
        average[x] = int( total[x]/num_lines )
        total_of_averages += average[x]

    total_of_widths = 0
    for x in range(0, num_columns):
        total_of_widths += width[x]

    amount_of_padding = (num_columns * len(splitter)) + len(splitter)

    if total_of_widths + amount_of_padding > totalwidth:

        for x in width:
            percent = float(average[x])/(total_of_averages)
            fair_average[x] = int((totalwidth - amount_of_padding) * percent)

        total_diff = 0
        for x in fair_average:
            if fair_average[x] < mincol:
                difference = mincol - fair_average[x]
                total_diff += difference
                fair_average[x] = mincol

        if total_diff > 0:
            while total_diff > 0:
                stole_some = False
                for x in fair_average:
                    if fair_average[x] > mincol:
                        fair_average[x] -= 1
                        total_diff -= 1
                if not stole_some:
                    break

        width = fair_average

    buffer = []
    if header:
        col = 0
        linebuffer = ""
        divider = ""
        for each in header:
            tmp=each
            if len(each) > width[col]:
                tmp = each[0:width[col]]
            linebuffer += splitter + pad(tmp, width[col])
            divider += cross + horiz * width[col]
            col += 1
        linebuffer += splitter
        divider += cross
        buffer.append(linebuffer)
        buffer.append(divider)

    for line in lines:
        linebuffer = ""
        col = 0
        for each in line:
            tmp = each
            if len(each) > width[col]:
                tmp = each[0:width[col]-2] + ".."


            linebuffer += splitter + pad(tmp, width[col])
            col += 1
        linebuffer += splitter
        buffer.append(linebuffer)

    return buffer