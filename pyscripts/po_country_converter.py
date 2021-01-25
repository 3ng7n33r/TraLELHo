with open("./input/input_po.txt", "r") as f:
    lines = f.readlines()

header1 = " </tbody>\n</table>\n<h2 id='"
header2 ="'>"
header3 = "</h2>\n<table class='tg'>\n <tbody>\n"

tablefoot = '''
    </tbody>
</table>
'''
output = []
sections = []
#output.append(tablehead)
i = 0
for line in lines:
    line = line.strip()
    output.append('msgid "' + line + '"\nmsgstr ""\n\n')

with open("./output/po_countries.txt", "w") as f:
    f.writelines(output)