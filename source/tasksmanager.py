import tasks
class TasksManager:
 def __init__(self):
     self.tasks=[]
 #创建TasksManager类
 def add_task(self,id,title,description,deadline,priority,status):
     task=tasks.Tasks(id,title,description,deadline,priority,status)
     self.tasks.append(task)
     print("任务已创建完毕！")
 #添加新文件
 def delete_task(self,id):
     new_tasks=[]
     for task in self.tasks:
         if task.id!=id:
             new_tasks.append(task)
     self.tasks=new_tasks
 #通过输入id选择要删除的文件
 def update_task(self,id,**kwargs):
     for task in self.tasks:
         if task.id==id:
           task.update(**kwargs)
           break
 #通过输入id选择要更改属性的文件
 #**kwargs:可变长度的关键字参数，允许传递任意数量的命名参数
 def show_tasks(self,sort_by=None):
     if sort_by=='priority':
      tasks_to_show=sorted(self.tasks,key=lambda x:(x.priority))
     else:
      tasks_to_show = sorted(self.tasks, key=lambda x: (x.deadline))
     for task in tasks_to_show:
         print(task)
 #显示文件
 #x:self.tasks列表中的每一个任务对象
 #sorted:按一定规则(key)进行排序
 def save_tasks(self,filename):
     with open(filename,"w") as file:
         for task in self.tasks:
             file.write(f'{task.id},{task.title},{task.description},{task.deadline},{task.priority},{task.status}'+'\n')
 #保存文件
 #with open(...,"w")打开文件并写入内容
 def load_tasks(self,filename):
     loaded_tasks=[]
     try:
         with open(filename,'r') as file:
             for line in file:
                 id,title,description,deadline,priority,*status=line.strip().split(',')
                 task=tasks.Tasks(id,title,description,deadline,priority,status)
                 loaded_tasks.append(task)
     except FileNotFoundError:
         print("文件没有找到，初始化空任务列表")
 #下载文件
 #with open(..."r")打开文件并读取内容