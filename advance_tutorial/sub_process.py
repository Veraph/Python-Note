import subprocess

# code below show how to run commond in python code like in commond-line
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# use communicate() to input if needed
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

'''上述代码相当于在命令行执行命令 nslookup 然后
输入：
set q=mx
python.org
exit
'''