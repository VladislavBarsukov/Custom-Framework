$Title = "Открытие"
WinWaitActive($Title)
ControlSetText($Title, "", "Edit1", $CmdLine[1])
ControlClick($Title, "", "Button1")
Exit