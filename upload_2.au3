#include <AutoItConstants.au3>

$CmdLine[1]
$CmdLine[2]
$CmdLine[3]
$FolderPath = $CmdLine[1]
$TargetX = Int($CmdLine[2])
$TargetY = Int($CmdLine[3])
Run("explorer.exe /select," & $FolderPath)
Sleep(400)
$sPartialTitle = "temp_upload"
WinMove($sPartialTitle, "", 0, 0, 200, 200)
$hExplorer = WinGetHandle("temp_upload")
$aPos = WinGetPos($hExplorer)
Sleep(400)
Send("^+{2}")
Sleep(400)
$newWidth = $aPos[2] ;Ширина окна
$newHeight = $aPos[3] ;Высота окна
$clickX = $newWidth / 2
$clickY = $newHeight / 2
MouseMove($aPos[0] + $clickX, $aPos[1] + $clickY, 0) ;
Sleep(400)
MouseDown("left")
Sleep(50)
MouseMove($TargetX, $TargetY, 10)
Sleep(50)
MouseUp("left")
WinClose($hExplorer)
Exit