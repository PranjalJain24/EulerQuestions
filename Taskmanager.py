import subprocess

cmd1="ps -ef >f1.txt"
cmd2="ps -p $sys.arg[0]"
ret_val = subprocess.call(cmd1, shell="True")
print("Tasks added to f1.txt", ret_val)
ret_value = subprocess.call(cmd2, shell="True")
print("Process info with PID entered: ",ret_value)
