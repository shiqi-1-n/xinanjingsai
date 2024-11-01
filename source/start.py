from tasksmanager import TasksManager
import menu
def main():
    mission = TasksManager()
    #创建mission对象
    mission.load_tasks('tasks.txt')
    #导入到文件tasks.txt
    while True:
        menu.menu()
        option = int(input("请选择要执行的功能:"))
        if option == 1:
           id=input("请输入ID(ex.001):")
           title=input("请输入标题:")
           description=input("请输入描述:")
           deadline=input("请输入截止日期(xxxx.xx.xx):")
           priority=input("请输入优先级(1/2/3):")
           status=input("请输入完成状态(未完成/进行中/已完成):")
           mission.add_task(id,title,description,deadline,priority,status)
        #选择1功能，进行添加文件操作
        elif option==2:
            id=input("请输入要删除的文件的ID:")
            mission.delete_task(id)
        #选择2功能，进行删除文件操作
        elif option==3:
            id=input("请输入要更新的文件的ID:")
            title = input("请输入新的标题（空白不修改）:")
            description = input("请输入新的描述（空白不修改）:")
            deadline = input("请输入新的截止日期(xxxx.xx.xx)（空白不修改）:")
            priority = input("请输入新的优先级(1/2/3)（空白不修改）:")
            status = input("请输入新的完成状态(未完成/进行中/已完成/)（空白不修改）:")
            mission.update_task(id,title=title or None,description=description or None,
                                deadline=deadline or None,priority=priority or None,status=status or None)
        #选择3功能，进行更新文件操作
        elif option==4:
            sort_by=input(f"请输入排序的依据:按优先级(priority)/按截止日期(deadline) ")
            mission.show_tasks(sort_by='priority' if sort_by.lower()=='priority' else None)
        #选择4功能，进行排序文件操作
        elif option==5:
            mission.save_tasks("tasks.txt")
        #选择5功能，进行保存文件操作
        else:
          print("您已经退出任务管理系统")
          break
        #退出系统
    #指令选择
