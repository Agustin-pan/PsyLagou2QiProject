# 动物父类
import yaml


class Animal:

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def call(self):
        print(f"{self.name} can be call")

    def run(self):
        print(f"{self.name} can be run")


# 猫的子类
class Cat(Animal):

    def __init__(self, name, color, age, sex, hair="短发"):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def CatchMouse(self):
        print(f"{self.name}会捉老鼠")

    def call(self):
        print("喵喵叫")


# 狗的子类
class Dog(Animal):

    def __init__(self, name, color, age, sex, hair="长毛"):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def CareHome(self):
        print(f"{self.name}会看家")

    def call(self):
        print("汪汪叫")


if __name__ == '__main__':
    with open("animal_data.yml", 'rb') as f:
        datas = yaml.safe_load(f)
    # 从配置文件读取猫的属性
    cat = datas["cat"]
    cat_name = cat["name"]
    cat_color = cat["color"]
    cat_age = cat["age"]
    cat_sex = cat["sex"]
    # 猫的实例
    cat1 = Cat(cat_name, cat_color, cat_age, cat_sex)
    # 调用猫桌老鼠的方法
    cat1.CatchMouse()
    # 打印猫的属性
    print(f"猫的名字叫{cat1.name}，颜色为{cat1.color}，年龄{cat1.age}岁，性别{cat1.sex}，毛发为{cat1.hair}，捉到了老鼠。")

    # 从配置文件读取狗的属性
    dog = datas["dog"]
    dog_name = dog["name"]
    dog_color = dog["color"]
    dog_age = dog["age"]
    dog_sex = dog["sex"]
    # 狗的实例
    dog1 = Dog(dog_name, dog_color, dog_age, dog_sex)
    # 狗看家
    dog1.CareHome()
    # 打印狗的属性
    print(f"狗的名字叫{dog1.name}，颜色为{dog1.color}，年龄{dog1.age}岁，性别{dog1.sex}，毛发为{dog1.hair}")
