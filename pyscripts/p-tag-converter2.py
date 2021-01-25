import re

with open("./input/input_ptag.txt", "r") as f:
    lines = f.readlines()


base = "{% language base_language %}\n"
target = "{% language target_language %}\n"
end = "{% endlanguage %}\n"

header1 = " </tbody>\n</table>\n " + base + "<h2 id='"
header2 ="'>{% translate \""
header3 = "\" %} </h2>\n" + end + "<table class='tg'>\n <tbody>\n"

tr1 = "<tr id='"
tr2 = "' onclick='togglerow(\""
tr3 = "\")'> \n"

tdshort1 = base + "<td><p> {% translate \""
tdshort2 = "\" %} </p></td> \n" + end + target +"<td><p> {% translate \""
tdshort3 = "\" %} </p></td>\n" + end

tdlong1 = base + "<td><p>{% blocktranslate %}"
tdlong2 = "{% endblocktranslate %}</p></td> \n" + end + target +"<td><p>{% blocktranslate %}"
tdlong3 = "{% endblocktranslate %}</p></td>\n" + end


output = []
sections = []
i = 0
for line in lines:
    line = line.strip()
    if re.search('[A-Z]{4,}', line):
        output.append(header1 + line + header2 + line + header3)
        sections.append(line + "\n")
    else:
        output.append(tr1 + str(i) + tr2 + str(i) + tr3)
        if len(line) < 20:
            string = tdshort1 + line + tdshort2 + line + tdshort3
        else:
            string = tdlong1 + line + tdlong2 + line + tdlong3
        output.append(string)
        output.append("</tr> \n")
        i += 1

with open("./output/p_tags.txt", "w") as f:
    f.writelines(output)

with open("./output/sections.txt", "w") as f:
    f.writelines(sections)