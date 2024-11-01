class Tasks:
    def __init__(self,id,title,description,deadline,priority,status):    #初始化类的属性(标题、描述、截止日期、优先级、状态)
        self.id=id
        self.title=title
        self.description=description
        self.deadline=deadline
        self.priority=priority
        self.status=status
    #创建Tasks类
    def update(self, title=None, description=None, deadline=None, priority=None, status=None):
        # 更新属性，先使各个参数恢复到默认值None
        if title:
            self.title = title
        if description:
            self.description = description
        if deadline:
            self.due_date = deadline
        if priority:
            self.priority = priority
        if status:
            self.status = status
    # 实现文档的更新
    # if语句：条件检查，如果有新的值，则将此新的值赋予到对应属性中
    def __str__(self):
        return f'{self.id}—{self.title}:{self.description}|截止日期:{self.deadline}|优先级:{self.priority}|完成状态:{self.status}'
#定义对象的字符串表示，提高代码的可读性和可维护性