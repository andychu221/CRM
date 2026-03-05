import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the innerHTML updates to map the index
content = content.replace(
    "else pDisplay.innerHTML = selectedPurposes.join('<br>');",
    "else pDisplay.innerHTML = selectedPurposes.map((p, idx) => `${idx + 1}. ${p}`).join('<br>');"
)
content = content.replace(
    "else display.innerHTML = selected.join('<br>');",
    "else display.innerHTML = selected.map((p, idx) => `${idx + 1}. ${p}`).join('<br>');"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
