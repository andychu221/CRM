with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update updateFormView
content = content.replace(
    "else pDisplay.innerHTML = selectedPurposes.map((p, idx) => `${idx + 1}. ${p}`).join('<br>');",
    "else if (selectedPurposes.length === 1 && selectedPurposes[0] !== '') pDisplay.innerHTML = selectedPurposes[0];\n        else pDisplay.innerHTML = selectedPurposes.map((p, idx) => `${idx + 1}. ${p}`).join('<br>');"
)

# Update togglePurpose
content = content.replace(
    "else display.innerHTML = selected.map((p, idx) => `${idx + 1}. ${p}`).join('<br>');",
    "else if (selected.length === 1 && selected[0] !== '') display.innerHTML = selected[0];\n        else display.innerHTML = selected.map((p, idx) => `${idx + 1}. ${p}`).join('<br>');"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
