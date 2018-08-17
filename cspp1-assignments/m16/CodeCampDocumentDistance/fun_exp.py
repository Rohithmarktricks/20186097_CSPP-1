exp = "A string is - there ? \n"
print(exp.lower().strip())

#[^A-Za-z0-9]+

import re
new = re.sub('[^A-Za-z0-9]+', ' ', exp)
print(exp)
