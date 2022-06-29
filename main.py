import os
import shutil

inject_old = b'electron'
inject_new = b'electrom'
file_path = r"app.asar.unpacked\main.node"
if not os.path.exists(file_path + '.bak'):
    shutil.copyfile(file_path, file_path + '.bak')
node_file = file_path + '.bak'

crack_file = r"inject\crack.js"

with open(crack_file, 'rb') as f:
    inject_content = f.read()
    with open(node_file, 'rb') as f1:
        prog_content = f1.read()
        inject_path = os.path.join(os.path.dirname(node_file), '..', 'node_modules', inject_new.decode() + '.js')
        inject_content += b';\nmodule.exports = require(\"electron\");'
        with open(inject_path, 'wb') as f2:
            f2.write(inject_content)
        prog_content = prog_content.replace(inject_old, inject_new)
        with open(file_path, 'wb') as f3:
            f3.write(prog_content)
