# 使用Unix/Linux操作系统提供的fork()系统调用
# 它调用一次返回两次，原理为自动把当前进程（父进程）复制一份（子进程）
# 然后分别在父进程里返回子进程的id； 在子进程里返回0

import os # os模块中封装了fork

print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process %s.' % (os.getpid(), pid))