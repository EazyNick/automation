import win32gui
import win32api
import win32con

#파이썬 3.10버전에선 안됨. 아나콘다로 실행하자.

# #!. 디스플레이 해상도 가져오기
# win32api.GetSystemMetrics(0) #디바이스 가로 사이즈
# win32api.GetSystemMetrics(1) #디바이스 세로 사이즈

# #2. 가장 상위 윈도우 핸들 가져오기
# hwnd = win32gui.GetActiveWindow()

# #3. 윈도우 사이즈 변경
# win32gui.MoveWindow(hwnd, 0, 0, 800, 600, 0)

# #4 특정 윈도우 핸들 가져오기
# win = win32gui.FindWindow(None, '')

# #4-1 핸들 강제종료
# win32api.SendMessage(win, win32con.WM_CLOSE, 0, 0)


win = win32gui.FindWindow(None, 'BlueStacks App Player 5')
win32gui.MoveWindow(win, 0, 0, 1000, 600, 0)
