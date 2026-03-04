with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_next = False
for i, line in enumerate(lines):
    if "onclick=\"togglePurpose('Others', this)\"" in line:
        # We know lines[i+1] is the text span, lines[i+2] is </div>, lines[i+3] is </div>, lines[i+4] is </div>
        # Looking at lines 966-970 from grep
        pass

    if i == 969 and line.strip() == "</div>":
        print("Skipping line 970: ", line.strip())
        continue
    new_lines.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
