import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the incorrect text extraction in updateFormView
content = content.replace(
"""        const purposeItems = document.querySelectorAll('#purpose-dropdown-content .dropdown-item-check');
        purposeItems.forEach(item => {
            const text = item.innerText.trim();
            if (selectedPurposes.includes(text)) {""",
"""        const purposeItems = document.querySelectorAll('#purpose-dropdown-content .dropdown-item-check');
        purposeItems.forEach(item => {
            const text = item.innerText.replace('check_box_outline_blank', '').replace('check_box', '').trim();
            if (selectedPurposes.includes(text)) {"""
)

# And fix handlePurposeChange which also queries the text
content = content.replace(
"""    function handlePurposeChange() {
        const currentVal = document.getElementById('frm-purpose').value;
        let selected = currentVal ? currentVal.split(', ') : [];""",
"""    function handlePurposeChange() {
        const currentVal = document.getElementById('frm-purpose').value;
        let selected = currentVal ? currentVal.split(', ') : [];"""
) # Wait handlePurposeChange doesn't use the innerText loop

# Fix togglePurpose which also updates the text. Wait togglePurpose gets the value from arguments.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
