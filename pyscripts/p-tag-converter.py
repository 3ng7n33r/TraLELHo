import re

with open("./input/input_ptag.txt", "r") as f:
    lines = f.readlines()

tablehead = '''
<table class="tg">
    <thead>
          <tr>
              <th>Origin</th>
              <th>Traduction</th>
          </tr>
    </thead>
    <tbody>
'''

tablefoot = '''
    </tbody>
</table>
'''
output = []
sections = []
output.append(tablehead)
for line in lines:
    line = line.strip()
    if re.search('[A-Z]{4,}', line):
        output.append(" </tbody>\n</table>\n<h2 id='" + line + "'>" + line + "</h2>\n<table class='tg'>\n <tbody>\n")
        sections.append(line + "\n")
    else:
        output.append("<tr> \n")
        if len(line) < 20:
            string = "<td><p>" + line + "</p></td> \n<td><p> {% translate \"" + line +"\" %} </p></td>\n"
        else:
            string = "<td><p>" + line + "</p></td> \n<td><p>{% blocktranslate %}" + line +"{% endblocktranslate %}</p></td>\n"
        output.append(string)
        output.append("</tr> \n")
output.append(tablefoot)

with open("./output/p_tags.txt", "w") as f:
    f.writelines(output)

with open("./output/sections.txt", "w") as f:
    f.writelines(sections)