import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove overflow: hidden from .paper-section
content = re.sub(r'(\.paper-section\s*\{[^}]*?)overflow:\s*hidden;\s*', r'\1', content)

# 2. Add border-radius: 4px 4px 0 0 to .paper-section-header
if 'border-radius: 4px 4px 0 0;' not in content:
    content = re.sub(r'(\.paper-section-header\s*\{[^}]*?)(?=})', r'\1    border-radius: 4px 4px 0 0;\n        ', content)

# 3. Change dropdown styling to allow multi-line instead of truncate
content = content.replace(
    '<span id="purpose-display" class="truncate flex-1 text-left mr-2">Select Purpose</span>',
    '<span id="purpose-display" class="break-words whitespace-normal self-start mt-1 flex-1 text-left mr-2">Select Purpose</span>'
)
content = content.replace(
    '<span id="purpose-display" class="truncate">Select Purpose</span>',
    '<span id="purpose-display" class="break-words whitespace-normal self-start mt-1 flex-1 text-left mr-2">Select Purpose</span>'
)
content = content.replace(
    '<span class="material-icons text-sm flex-shrink-0">arrow_drop_down</span>',
    '<span class="material-icons text-sm self-start mt-1 flex-shrink-0">arrow_drop_down</span>'
)
content = content.replace(
    '<span class="material-icons text-sm">arrow_drop_down</span>',
    '<span class="material-icons text-sm self-start mt-1 flex-shrink-0">arrow_drop_down</span>'
)
content = content.replace(
    '''<button class="dropdown-btn w-full" id="btn-purpose-dropdown" onclick="togglePurposeDropdown()">''',
    '''<button class="dropdown-btn w-full flex items-start" id="btn-purpose-dropdown" onclick="togglePurposeDropdown()">'''
)

# 4. Add "Others" to dropdown
others_item = """                                                     <div class="dropdown-item-check" onclick="togglePurpose('Others', this)">
                                                        <span class="material-icons text-sm">check_box_outline_blank</span> Others
                                                     </div>
                                                </div>"""
content = re.sub(r'(\s*</div>\s*</div>\s*<input type="hidden" id="frm-purpose">)', r'\n' + others_item + r'\1', content)
content = content.replace(
"""                                                     <div class="dropdown-item-check" onclick="togglePurpose('Others', this)">
                                                        <span class="material-icons text-sm">check_box_outline_blank</span> Others
                                                     </div>
                                                </div>                                                </div>""",
"""                                                     <div class="dropdown-item-check" onclick="togglePurpose('Others', this)">
                                                        <span class="material-icons text-sm">check_box_outline_blank</span> Others
                                                     </div>
                                                </div>"""
)

# 5. Add Others row in HTML
others_row = """                                    <div class="paper-field-row hidden" id="others-purpose-row">
                                        <div class="paper-label">Others Purpose</div>
                                        <div class="paper-value"><input type="text" id="frm-others-purpose" placeholder="Specify other purpose"></div>
                                    </div>"""
if 'id="others-purpose-row"' not in content:
    content = content.replace(
        '<div class="paper-field-row hidden" id="shared-purpose-row">',
        others_row + '\n                                    <div class="paper-field-row hidden" id="shared-purpose-row">'
    )

# 6. JS logic updates for multi-line and others
content = content.replace(
    "else pDisplay.innerText = selectedPurposes.join(', ');",
    "else pDisplay.innerHTML = selectedPurposes.join('<br>');"
)
content = content.replace(
    "else pDisplay.innerText = `${selectedPurposes.length} Purposes Selected`;",
    "else pDisplay.innerHTML = selectedPurposes.join('<br>');"
)

content = content.replace(
    "else display.innerText = selected.join(', ');",
    "else display.innerHTML = selected.join('<br>');"
)
content = content.replace(
    "else display.innerText = `${selected.length} Purposes Selected`;",
    "else display.innerHTML = selected.join('<br>');"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
