$Outlook = New-Object -ComObject Outlook.Application
$createmail = $Outlook.CreateItem(0)
$createmail.To =  "raghuvel.sekar@karglobal.com"
$createmail.Subject = "File Not found"
$createmail.Body = "test"
## TDDAuctionInventoryEDI 

###List Files from a directory modified in last 30 min + send mail if count is less then 48



#######################################

$path = "Z:\"+(Get-Date).tostring("MM-dd-yyyy")
#$path 
$FileList = Get-ChildItem -Path $path
$FileLists = $FileList| Where-Object {$_.LastWriteTime -gt [datetime]::Now.AddMinutes(-30)}
#$FileLists

$currenttime = (Get-Date).ToString('HH:mm')
#$currenttime

$currenttime1 = (Get-Date).AddMinutes(1).ToString('HH:mm')
#$currenttimeplus1

$currenttime2 = (Get-Date).AddMinutes(2).ToString('HH:mm')
#$currenttimeplus2

$currenttime3 = (Get-Date).AddMinutes(3).ToString('HH:mm')
#$currenttimeplus3

$currenttime4 = (Get-Date).AddMinutes(4).ToString('HH:mm')
#$currenttimeplus4

$currenttime5 = (Get-Date).AddMinutes(5).ToString('HH:mm')
#$currenttimeplus5

$currenttime6 = (Get-Date).AddMinutes(6).ToString('HH:mm')
#$currenttimeplus6

$currenttime7= (Get-Date).AddMinutes(7).ToString('HH:mm')
#$currenttimeplus7
$currenttime8 = (Get-Date).AddMinutes(8).ToString('HH:mm')
#$currenttimeplus8
$currenttime9 = (Get-Date).AddMinutes(9).ToString('HH:mm')
#$currenttimeplus9
$currenttime10 = (Get-Date).AddMinutes(10).ToString('HH:mm')
#$currenttimeplus10

#Write-Host "in for loop"
#$filecreatedtime = $tomail.CreationTime.ToString('HH:mm')
#$filecreatedtime

$counter = 0     
foreach ($tomail in $FileLists)
{
<#
Write-Host "in for loop"
Write-Host ($tomail)
Write-Host ("----------------------------------------------------------")
Write-Host ($tomail.CreationTime.ToString('HH:mm'))
Write-Host ($currenttime)
Write-Host ("----------------------------------------------------------")
#>
$counter = 0
if ($tomail.Name -match '[0-9]{4}_INVENT')
{
#Write-Host $tomail.Name
if ($([DateTime]$tomail.CreationTime.ToString('HH:mm')) -match $([DateTime]$currenttime) -or $([DateTime]$currenttime1) -or $([DateTime]$currenttime2) -or $([DateTime]$currenttime3) -or $([DateTime]$currenttime4) -or $([DateTime]$currenttime5) -or $([DateTime]$currenttime6) -or $([DateTime]$currenttime7) -or $([DateTime]$currenttime8) -or $([DateTime]$currenttime9) -or $([DateTime]$currenttime10))

    {
        #Write-Host "File  found"

        $counter = $counter + 1

        $tomail.Name + "  Found  " + $tomail.CreationTime >> C:\Users\raghuvel.sekar\Desktop\TDDAUCTIONINVENTORYAUTOMATIONLOG.txt
		
		
    }
else
{
  #Write-Host "File not found"

  "  FileNotFound  " + $currenttime >> C:\Users\raghuvel.sekar\Desktop\TDDAUCTIONINVENTORYAUTOMATIONLOG.txt
  $createmail.Send()
}
}
else
{
  #Write-Host "file with name not found"
  #"filewithnamenotdound = "+$tomail.CreationTime >> C:\Users\Vamsi.Guttikonda\Desktop\test.txt
  
}
}
        #$counter
        Remove-Variable counter

####################################
####################################
####################################
####################################