from lunar_python import Lunar
from datetime import datetime, timedelta

def now_lunar(utc_offset: int = 8) -> Lunar:  # 8 is UTC+8 for China
    now = datetime.now() + timedelta(hours=utc_offset)
    lunar = Lunar.fromYmd(now.year, now.month, now.day)
    return lunar

def print_lunar_info():
    l = now_lunar()
    
    # 基本信息
    print("=== 农历基本信息 ===")
    print(f"农历年: {l.getYear()} ({l.getYearInChinese()}年)")
    print(f"农历月: {l.getMonth()} ({l.getMonthInChinese()}月)")
    print(f"农历日: {l.getDay()} ({l.getDayInChinese()})")
    print(f"星期: {l.getWeekInChinese()}")
    
    # 干支历信息
    print("\n=== 干支历信息 ===")
    print(f"年干支: {l.getYearInGanZhi()} (属{l.getYearShengXiao()})")
    print(f"月干支: {l.getMonthInGanZhi()} (属{l.getMonthShengXiao()})")
    print(f"日干支: {l.getDayInGanZhi()} (属{l.getDayShengXiao()})")
    print(f"时干支: {l.getTimeInGanZhi()} (属{l.getTimeShengXiao()})")
    
    # 纳音信息
    print("\n=== 纳音五行 ===")
    print(f"年纳音: {l.getYearNaYin()}")
    print(f"月纳音: {l.getMonthNaYin()}")
    print(f"日纳音: {l.getDayNaYin()}")
    print(f"时纳音: {l.getTimeNaYin()}")
    
    # 节日信息
    print("\n=== 节日信息 ===")
    print(f"农历节日: {', '.join(l.getFestivals())}")
    print(f"其他节日: {', '.join(l.getOtherFestivals())}")
    
    # 节气信息
    print("\n=== 节气信息 ===")
    print(f"当前节气: {l.getJieQi()}")
    next_jie = l.getNextJie()
    if next_jie:
        print(f"下一个节: {next_jie.getName()} ({next_jie.getSolar().toYmd()})")
    next_qi = l.getNextQi()
    if next_qi:
        print(f"下一个气: {next_qi.getName()} ({next_qi.getSolar().toYmd()})")
    
    # 传统历法信息
    print("\n=== 传统历法信息 ===")
    print(f"二十八宿: {l.getXiu()}")
    print(f"宿朝: {l.getZheng()}")
    print(f"宿动物: {l.getAnimal()}")
    print(f"宫位: {l.getGong()}")
    print(f"值神: {l.getShou()}")
    print(f"彭祖百忌: {l.getPengZuGan()} {l.getPengZuZhi()}")
    
    # 方位吉凶
    print("\n=== 方位吉凶 ===")
    print(f"喜神方位: {l.getDayPositionXi()} ({l.getDayPositionXiDesc()})")
    print(f"阳贵神方位: {l.getDayPositionYangGui()} ({l.getDayPositionYangGuiDesc()})")
    print(f"阴贵神方位: {l.getDayPositionYinGui()} ({l.getDayPositionYinGuiDesc()})")
    print(f"福神方位: {l.getDayPositionFu()} ({l.getDayPositionFuDesc()})")
    print(f"财神方位: {l.getDayPositionCai()} ({l.getDayPositionCaiDesc()})")
    
    # 冲煞信息
    print("\n=== 冲煞信息 ===")
    print(f"冲: {l.getChongDesc()}")
    print(f"煞: {l.getSha()}")
    
    # 时辰吉凶
    print("\n=== 时辰吉凶 ===")
    print(f"时辰宜: {', '.join(l.getTimeYi())}")
    print(f"时辰忌: {', '.join(l.getTimeJi())}")

    # full info
    print("\n=== 完整信息 ===")
    print(f"阴历: {l.toFullString()}")
    print(f"阳历: {l.getSolar().toFullString()}")

if __name__ == "__main__":
    print_lunar_info()
    
