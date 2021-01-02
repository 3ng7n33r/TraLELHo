with open("./output/sections.txt", "r") as f:
    lines = f.readlines()

tablehead = '''
<nav>
    <button type="button" class="collapsible"></button>
    <div class="content">
   		<ul>
'''

tablefoot = '''
        </ul>
    </div>
</nav>
'''
output = []
sections = []
output.append(tablehead)
for line in lines:
    line = line.strip()
    output.append("             <li><a onclick='collapsenav()' href='#" + line + "'>" + line + "</a></li>\n")
output.append(tablefoot)

with open("./output/nav.txt", "w") as f:
    f.writelines(output)