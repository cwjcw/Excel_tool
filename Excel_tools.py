import pandas as pd

def breakdown(m,path,wb,sheet_name,Filter):
        # m：str,keyword for Filter 需要筛选的关键字
        # path: str, the path of target_excel,not include file name 筛选后的文件保存路径，不含文件名
        # wb: the full path of the source_excel,include file nmae 源文件完整路径，含文件名
        # sheet_name: str, incloud the Filter 需要筛选的工作表
        # Filter: str, the name of filter column 需要筛选的列
        try:
            target = f'{path}\\{m}.xlsx'
            with pd.ExcelWriter(target, engine='openpyxl') as writer:
                df = pd.read_excel(wb,sheet_name=sheet_name)
                x = df[df[Filter] == m]
                x.to_excel(excel_writer=writer, sheet_name=m, index=False)
        except:
            print('抱歉，出错了，请检查代码')


