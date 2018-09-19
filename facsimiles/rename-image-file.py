import glob, re, os

for img in glob.glob('MS*.jpg'):
    new_name = re.sub(r'MS1515v2_', 'xom-', img)
    new_name = re.sub(r'r', '-s1', new_name)
    new_name = re.sub(r'v', '-s2', new_name)
    cmd = 'ln -s {} {}'.format(img, new_name)
    os.system(cmd)
    print(cmd)
