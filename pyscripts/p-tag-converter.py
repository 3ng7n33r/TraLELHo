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
output.append(tablehead)
for line in lines:
    line = line.strip()
    output.append("<tr> \n")
    if len(line) < 20:
        string = "<td><p>" + line + "</p></td> \n<td><p> {% translate \"" + line +"\" %} </p></td>\n"
    else:
        string = "<td><p>" + line + "</p></td> \n<td><p>{% blocktranslate %}\"" + line +"\"{% endblocktranslate %}</p></td>\n"
    output.append(string)
    output.append("</tr> \n")
output.append(tablefoot)

with open("./output/p_tags.txt", "w") as f:
    f.writelines(output)