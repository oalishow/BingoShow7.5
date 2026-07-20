import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""                    showMenuInBreak: true,
                    sponsorEditorReusableBg: '',
                    sponsorEditorReusableBgOpacity: 100,
                    cardGeneratorConfig: \{"""

good_replacement = """                    showMenuInBreak: true,
                    sponsorEditorReusableBg: '',
                    sponsorEditorReusableBgOpacity: 100,
                    cardGeneratorPin: '',
                    cardGeneratorConfig: {"""
                    
content = re.sub(bad_pattern, good_replacement, content)

with open('index.tsx', 'w') as f:
    f.write(content)
